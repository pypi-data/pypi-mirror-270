from struct import calcsize, unpack

class GroupDescriptor:
		BGDT_FORMAT = (
				"<"   # Little-endian byte order
				"I"   # bg_block_bitmap (4 bytes)
				"I"   # bg_inode_bitmap (4 bytes)
				"I"   # bg_inode_table (4 bytes)
				"H"   # bg_free_blocks_count (2 bytes)
				"H"   # bg_free_inodes_count (2 bytes)
				"H"   # bg_used_dirs_count (2 bytes)
				"H"   # bg_pad (2 bytes, padding)
				"12s" # bg_reserved (12 bytes, reserved space)
		)
		BGDT_SIZE = calcsize(BGDT_FORMAT)
		BGDT_KEYS = [
				"bg_block_bitmap",
				"bg_inode_bitmap",
				"bg_inode_table",
				"bg_free_blocks_count",
				"bg_free_inodes_count",
				"bg_used_dirs_count",
				"bg_pad",  # Padding, typically doesn't carry information
				# "bg_reserved" is not unpacked into a key as it's reserved for future use
		]
		
		def __init__(self, bg_number, sb, shadow_gd_sb_indices, io):
				self.sb = sb
				self.io = io
				self.shadow_gd_sb_indices = shadow_gd_sb_indices
				self.bg_number = bg_number

				self.gd = self._parse()
				for k, v in self.gd.items():
						setattr(self, k, v)

		def _parse(self, shadow_gd_sb_index=0):
				if self.sb.s_rev_level > 0:
						if shadow_gd_sb_index not in self.shadow_gd_sb_indices:
								raise ValueError("Invalid block group, revision 1+ have block descriptor tables at 0, 1 and powers of 3, 5 and 7.")
				offset = (shadow_gd_sb_index * self.sb.s_blocks_per_group * self.sb.s_block_size) + self.sb.s_block_size + self.bg_number * self.BGDT_SIZE
				self.io.lock()
				gd = self.io.read_at(self.BGDT_SIZE, offset)
				self.io.unlock()
				unpacked_gd = unpack(self.BGDT_FORMAT, gd)
				parsed_gd = {}
				for key, value in zip(self.BGDT_KEYS, unpacked_gd):
						parsed_gd[key] = value
				return parsed_gd