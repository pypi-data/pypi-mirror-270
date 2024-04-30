from struct import unpack
from uuid import UUID
from datetime import datetime

class Superblock:
		SUPERBLOCK_FORMAT = (
				"<"  # Little-endian byte order
				"I"  # s_inodes_count (4 bytes)
				"I"  # s_blocks_count (4 bytes)
				"I"  # s_r_blocks_count (4 bytes)
				"I"  # s_free_blocks_count (4 bytes)
				"I"  # s_free_inodes_count (4 bytes)
				"I"  # s_first_data_block (4 bytes)
				"I"  # s_log_block_size (4 bytes)
				"I"  # s_log_frag_size (4 bytes)
				"I"  # s_blocks_per_group (4 bytes)
				"I"  # s_frags_per_group (4 bytes)
				"I"  # s_inodes_per_group (4 bytes)
				"I"  # s_mtime (4 bytes)
				"I"  # s_wtime (4 bytes)
				"H"  # s_mnt_count (2 bytes)
				"H"  # s_max_mnt_count (2 bytes)
				"H"  # s_magic (2 bytes)
				"H"  # s_state (2 bytes)
				"H"  # s_errors (2 bytes)
				"H"  # s_minor_rev_level (2 bytes)
				"I"  # s_lastcheck (4 bytes)
				"I"  # s_checkinterval (4 bytes)
				"I"  # s_creator_os (4 bytes)
				"I"  # s_rev_level (4 bytes) 0 is EXT2_GOOD_OLD_REV, EXT2_DYNAMIC_REV is 1
				"H"  # s_def_resuid (2 bytes)
				"H"  # s_def_resgid (2 bytes)
			# -- EXT2_DYNAMIC_REV Specific --
				"I"  # s_first_ino (4 bytes)
				"H"  # s_inode_size (2 bytes)
				"H"  # s_block_group_nr (2 bytes)
				"I"  # s_feature_compat (4 bytes)
				"I"  # s_feature_incompat (4 bytes)
				"I"  # s_feature_ro_compat (4 bytes)
				"16s"  # s_uuid (16 bytes)
				"16s"  # s_volume_name (16 bytes)
				"64s"  # s_last_mounted (64 bytes)
				"I"  # s_algo_bitmap (4 bytes)
			# -- Performance Hints --
				"B"    # s_prealloc_blocks (1 byte)
				"B"    # s_prealloc_dir_blocks (1 byte)
				"2x"   # alignment (2 bytes)
			# -- Journaling Support --
				"16s"  # s_journal_uuid (16 bytes)
				"I"    # s_journal_inum (4 bytes)
				"I"    # s_journal_dev (4 bytes)
				"I"    # s_last_orphan (4 bytes)
			# -- Directory Indexing Support --
				"4I"   # s_hash_seed (4 x 4 bytes = 16 bytes)
				"B"    # s_def_hash_version (1 byte)
				"3x"   # padding - reserved for future expansion (3 bytes)
			# -- Other options --
				"I"    # s_default_mount_options (4 bytes)
				"I"    # s_first_meta_bg (4 bytes)
				"760x" # Unused - reserved for future revisions (760 bytes)
		)
		SUPERBLOCK_KEYS = [
				"s_inodes_count",
				"s_blocks_count",
				"s_r_blocks_count",
				"s_free_blocks_count",
				"s_free_inodes_count",
				"s_first_data_block",
				"s_log_block_size",
				"s_log_frag_size",
				"s_blocks_per_group",
				"s_frags_per_group",
				"s_inodes_per_group",
				"s_mtime",
				"s_wtime",
				"s_mnt_count",
				"s_max_mnt_count",
				"s_magic",
				"s_state",
				"s_errors",
				"s_minor_rev_level",
				"s_lastcheck",
				"s_checkinterval",
				"s_creator_os",
				"s_rev_level",
				"s_def_resuid",
				"s_def_resgid",
				"s_first_ino",
				"s_inode_size",
				"s_block_group_nr",
				"s_feature_compat",
				"s_feature_incompat",
				"s_feature_ro_compat",
				"s_uuid",
				"s_volume_name",
				"s_last_mounted",
				"s_algo_bitmap",
				"s_prealloc_blocks",
				"s_prealloc_dir_blocks",  # 'alignment' field is not listed as it's padding
				"s_journal_uuid",
				"s_journal_inum",
				"s_journal_dev",
				"s_last_orphan",
				"s_hash_seed_0",
				"s_hash_seed_1",
				"s_hash_seed_2",
				"s_hash_seed_3",
				"s_def_hash_version",  # 'padding' field is not listed as it's padding
				"s_default_mount_options",
				"s_first_meta_bg",
				# 'Unused' reserved fields not included
		]
		PRIMARY_SB_OFFSET = 1024
		SUPERBLOCK_SIZE = 1024

		def __init__(self, bg_number, io=None):
				'''
				bg_number: target sb you wish to parse, the primary sb at bg 0 or shadow copies
				'''
				self.io = io
				self.bg_number = bg_number
				self.sb = self._parse()
				
				for k, v in self.sb.items():
						setattr(self, k, v)
				
				self.s_block_size = 1024 << self.s_log_block_size
				self.s_inode_size = self.s_inode_size if self.s_rev_level > 0 else 128
				if self.io: self.io.set_s_block_size(self.s_block_size)

		def _parse(self):
				offset = self.PRIMARY_SB_OFFSET if self.bg_number == 0 else self.bg_number * self.s_blocks_per_group * self.s_block_size
				self.io.lock()
				superblock = self.io.read_at(self.SUPERBLOCK_SIZE, offset)
				self.io.unlock()
				unpacked_superblock = unpack(self.SUPERBLOCK_FORMAT, superblock)
				parsed_superblock = {}
				for key, value in zip(self.SUPERBLOCK_KEYS, unpacked_superblock):
						if key in {'s_uuid', 's_journal_uuid'}:
								parsed_superblock[key] = str(UUID(bytes=value))
						elif key in {'s_mtime', 's_wtime', 's_lastcheck'}:
								parsed_superblock[key] = datetime.fromtimestamp(value).strftime('%Y/%m/%d %I:%M:%S %p')
						elif key in {'s_volume_name', 's_last_mounted'}:
								parsed_superblock[key] = value.decode('latin1').rstrip('\x00')
						else:
								parsed_superblock[key] = value
				return parsed_superblock