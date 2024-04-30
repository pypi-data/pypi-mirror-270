from struct import unpack_from

class Directory:
		def __init__(self, block_number, sb, io):
				self.block_number = block_number
				self.sb = sb
				self.io = io
				self.entries = self._parse()

		def _parse(self):
				self.io.lock()
				block_data = self.io.read_block(self.block_number)
				self.io.unlock()
				
				pointer = 0
				parsed_directory_block = []
				while pointer < self.sb.s_block_size:
					inode, entry_length, name_length = unpack_from('<IHB', block_data, pointer)
					if inode == 0:
						pointer += entry_length	
						continue
					name = block_data[pointer + 8:pointer + 8 + name_length].decode('utf-8')
					parsed_directory_block.append({'inode': inode, 'name': name})
					pointer += entry_length
					if entry_length == 0:
						break

				return parsed_directory_block