from struct import calcsize, unpack, unpack_from
from datetime import datetime
from .group_descriptor import GroupDescriptor

class Inode:
		INODE_KEYS = [
				"i_mode",
				"i_uid",
				"i_size",
				"i_atime",
				"i_ctime",
				"i_mtime",
				"i_dtime",
				"i_gid",
				"i_links_count",
				"i_blocks",
				"i_flags",
				"i_osd1",
				"i_block_0",
				"i_block_1",
				"i_block_2",
				"i_block_3",
				"i_block_4",
				"i_block_5",
				"i_block_6",
				"i_block_7",
				"i_block_8",
				"i_block_9",
				"i_block_10",
				"i_block_11",
				"i_block_12",  # Indirect block pointer
				"i_block_13",  # Double-indirect block pointer
				"i_block_14",  # Triple-indirect block pointer
				"i_generation",
				"i_file_acl",
				"i_dir_acl",
				"i_faddr",
				"i_osd2",
		]
		INODE_FORMAT = (
				"<"       # Little-endian byte order
				"H"       # i_mode (2 bytes)
				"H"       # i_uid (2 bytes)
				"I"       # i_size (4 bytes)
				"I"       # i_atime (4 bytes)
				"I"       # i_ctime (4 bytes)
				"I"       # i_mtime (4 bytes)
				"I"       # i_dtime (4 bytes)
				"H"       # i_gid (2 bytes)
				"H"       # i_links_count (2 bytes)
				"I"       # i_blocks (4 bytes)
				"I"       # i_flags (4 bytes)
				"I"       # i_osd1 (4 bytes)
				# i_block: 12 direct (4x12), 1 indirect (4), 1 double-indirect (4), 1 triple-indirect (4)
				"4I"      # i_block (direct blocks)
				"4I"      # i_block (direct blocks)
				"4I"      # i_block (direct blocks)
				"I"       # i_block (indirect block)
				"I"       # i_block (double-indirect block)
				"I"       # i_block (triple-indirect block)
				"I"       # i_generation (4 bytes)
				"I"       # i_file_acl (4 bytes)
				"I"       # i_dir_acl (4 bytes)
				"I"       # i_faddr (4 bytes)
				"12s"     # i_osd2 (12 bytes)
				# "128x"	used for extended attributes, higher timestamp resolution, versioning, or reserved for future features.
		)

		def __init__(self, i_number, sb, shadow_gd_sb_indices, io):
				self.io = io
				self.sb = sb
				self.shadow_gd_sb_indices = shadow_gd_sb_indices
				self.i_number = i_number
				self.INODE_FORMAT += f"{self.sb.s_inode_size - calcsize(self.INODE_FORMAT)}x" if self.sb.s_inode_size > 128 else ""
				
				self.i = self._parse()
				for k, v in self.i.items():
						setattr(self, k, v)

		def _parse_inode_mode(self, i_mode):
				file_formats = {
						0xC000: "socket",
						0xA000: "symbolic link",
						0x8000: "regular file",
						0x6000: "block device",
						0x4000: "directory",
						0x2000: "character device",
						0x1000: "FIFO",
				}

				file_type = i_mode & 0xF000
				file_format_description = file_formats.get(file_type, "unknown")

				is_setuid = bool(i_mode & 0x0800)
				is_setgid = bool(i_mode & 0x0400)
				is_sticky = bool(i_mode & 0x0200)

				permissions = {
						'user_read': bool(i_mode & 0x0100),
						'user_write': bool(i_mode & 0x0080),
						'user_execute': bool(i_mode & 0x0040),
						'group_read': bool(i_mode & 0x0020),
						'group_write': bool(i_mode & 0x0010),
						'group_execute': bool(i_mode & 0x0008),
						'others_read': bool(i_mode & 0x0004),
						'others_write': bool(i_mode & 0x0002),
						'others_execute': bool(i_mode & 0x0001),
				}
				
				one_line_perms = ''.join([
						file_formats.get(i_mode & 0xF000, '-')[0].lower(),
						'r' if i_mode & 0x0100 else '-',
						'w' if i_mode & 0x0080 else '-',
						'x' if i_mode & 0x0400 else 'S' if i_mode & 0x0800 else '-',
						'r' if i_mode & 0x0020 else '-',
						'w' if i_mode & 0x0010 else '-',
						'x' if i_mode & 0x0200 else 'S' if i_mode & 0x0400 else '-',
						'r' if i_mode & 0x0004 else '-',
						'w' if i_mode & 0x0002 else '-',
						'x' if i_mode & 0x0001 else 'T' if i_mode & 0x0200 else '-'
				])

				return {
						'file_format': file_format_description,
						'is_setuid': is_setuid,
						'is_setgid': is_setgid,
						'is_sticky': is_sticky,
						'permissions': permissions,
						'one_line_permissions': one_line_perms
				}

		def _parse(self):
				bg_number = self.i_number // self.sb.s_inodes_per_group
				gd = GroupDescriptor(bg_number, self.sb, self.shadow_gd_sb_indices, self.io)
				inode_index = (self.i_number - 1) % self.sb.s_inodes_per_group
				inode_byte_offset = inode_index * self.sb.s_inode_size
				absolute_byte_offset = (gd.bg_inode_table * self.sb.s_block_size) + inode_byte_offset
				self.io.lock()
				inode = self.io.read_at(self.sb.s_inode_size, absolute_byte_offset)
				self.io.unlock()
				unpacked_inode = unpack(self.INODE_FORMAT, inode)
				parsed_inode = {}
				for key, value in zip(self.INODE_KEYS, unpacked_inode):
						if key in {'i_atime', 'i_ctime', 'i_mtime'}:
								parsed_inode[key] = datetime.fromtimestamp(value).strftime('%Y/%m/%d %I:%M:%S %p')
						elif key == "i_mode":
								parsed_inode[key] = self._parse_inode_mode(value)
						else:
								parsed_inode[key] = value
				return parsed_inode
		
		def _parse_pointer_block(self, block_number):
				block_pointers = []
				self.io.lock()
				block_data = self.io.read_block(block_number)
				self.io.unlock()

				for i in range(0, len(block_data), 4):
					ptr = unpack_from('<I', block_data, i)[0]
					if ptr == 0: break
					block_pointers.append(ptr)
				return block_pointers

		def _blocks_numbers_from_indirect_blocks(self, block_numbers, depth):
				if depth == 0: return block_numbers
				all_blocks = []
				for block_number in block_numbers:
						if block_number == 0: continue
						all_blocks.extend(self._block_numbers_from_indirect_blocks(self._parse_pointer_block(block_number), depth - 1))
				return all_blocks

		def block_numbers(self):
				i_blocks = [getattr(self, f'i_block_{i}') for i in range(15)]
				direct_block_numbers = [i_block for i_block in i_blocks[0:12] if i_block != 0]
				indirect_block_numbers = self._blocks_numbers_from_indirect_blocks(i_blocks[12:13], 1)
				double_block_numbers = self._blocks_numbers_from_indirect_blocks(i_blocks[13:14], 2)
				triple_block_numbers = self._blocks_numbers_from_indirect_blocks(i_blocks[14:15], 3)
				return direct_block_numbers + indirect_block_numbers + double_block_numbers + triple_block_numbers