'''
	bg_, bg: block group
	s_,  sb: superblock
	gd_, gd: group descriptor
	i_,   i: inode
	d_, dir: directory
'''

from os import path
from struct import unpack_from
from .superblock import Superblock
from .io import IO
from .inode import Inode
from .directory import Directory

class Ext2:
		SMALLEST_EXT2_SIZE = 58368
		EXT2_SUPER_MAGIC = b'\x53\xEF'
		
		def __init__(self, source):
				self.source = source
				self.io = IO(self.source)

				self._check_magic_number()
				self.sb = Superblock(0, self.io)

				self.shadow_gd_sb_indices = self._get_shadow_gd_sb_indices()
				self.cwd_i = 2
				self.cwd_entries = self._entries_from_inode()
				self.path_stack = []  

		def _check_magic_number(self):
				source_size = path.getsize(self.source)
				if source_size < self.SMALLEST_EXT2_SIZE: raise EOFError(f"Invalid file length, expected at least {self.SMALLEST_EXT2_SIZE} bytes but got {source_size} bytes")
				self.io.lock()
				magic_number = self.io.read_at(2, 1080)
				self.io.unlock()
				if not self.EXT2_SUPER_MAGIC == magic_number:
						raise ValueError(f"Invalid magic number: {magic_number.hex()} (expected '0x53EF')")

		def _get_shadow_gd_sb_indices(self):
				'''
				shadow gd & sb indices are 0, 1 and powers of 3, 5 and 7
				'''
				max_bg_limit = self.sb.s_blocks_count // self.sb.s_blocks_per_group
				if self.sb.s_rev_level > 0:
						gd_sb_groups = [0, 1]
						for i in [3, 5, 7]:
								n = 1
								while n <= max_bg_limit:
									gd_sb_groups.append(n)
									n *= i
						return sorted(set(gd_sb_groups))
				else:
						return [x for x in range(max_bg_limit // max_bg_limit)]

		def pwd(self):
				print('/'+'/'.join(self.path_stack))

		def _get_inode_number_by_name(self, name):
				for entry in self.cwd_entries:
						if entry['name'] == name:
								return entry['inode']
				return None

		def cd(self, directory):
				if directory == "/":
						self.cwd_i = 2
						self.cwd_entries = self._entries_from_inode()
						self.path_stack = []
				else:
						i_number = self._get_inode_number_by_name(directory)
						if not i_number:
							print(f"no directory {directory}")
						else:
								inode = Inode(i_number, self.sb, self.shadow_gd_sb_indices, self.io)
								if inode.i_mode['file_format'] == 'directory':
										self.cwd_i = i_number
										self.cwd_entries = self._entries_from_inode()
										if directory == "..":
												if len(self.path_stack) > 0:
														self.path_stack.pop()
										else:
												self.path_stack.append(directory)
								else:
										print(f"{directory} is not a directory")

		def _format_entry(self, entry_inode, entry_name):
				permissions = entry_inode.i_mode['one_line_permissions']
				links_count = entry_inode.i_links_count
				username = entry_inode.i_uid
				groupname = entry_inode.i_gid
				size = entry_inode.i_size
				mtime = entry_inode.i_mtime
				formatted_info = f"{permissions} {links_count:<3d} {username:<8} {groupname:<8} {size:>8} {mtime} {entry_name}"
				return formatted_info
				
		def _entries_from_inode(self):
				inode = Inode(self.cwd_i, self.sb, self.shadow_gd_sb_indices, self.io)
				entries = []
				# following check is for extra precaution since cd command ensures cwd is indeed a dir
				if inode.i_mode['file_format'] == 'directory':
						block_numbers = inode.block_numbers()
						for block_number in block_numbers:
								entries.extend(Directory(block_number, self.sb, self.io).entries)
				return entries

		def ls(self, long=False):
				entries = self._entries_from_inode()
				if long:
						for entry in entries:
								entry_inode = Inode(entry['inode'], self.sb, self.shadow_gd_sb_indices, self.io)
								print(self._format_entry(entry_inode, entry['name']))
				else: print(' '.join(entry['name'] for entry in entries))

		def dump(self, filename, destination):
				if not path.isdir(destination):
						print(f"destination {destination} does not exist or is not a directory.")
						return

				i_number = self._get_inode_number_by_name(filename)
				if not i_number:
					print(f"no file {filename}")
					return

				inode = Inode(i_number, self.sb, self.shadow_gd_sb_indices, self.io)
				if not inode.i_mode['file_format'] == 'regular file':
						print(f"{filename} is not a file")
						return
				
				block_numbers = inode.block_numbers()
				final_block_size = inode.i_size % self.sb.s_block_size 
				with open(path.join(destination, filename), 'wb') as file:
						for i, block_number in enumerate(block_numbers):
								block_data = self.io.read_block(block_number)
								if i == len(block_numbers) - 1:
										# trimming to avoid excess null values on last block
										block_data = block_data[:final_block_size]
								file.write(block_data)
				print(f"{filename} successfully dumped to {destination}")