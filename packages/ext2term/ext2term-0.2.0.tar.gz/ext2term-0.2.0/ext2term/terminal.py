import cmd
from .ext2 import Ext2

class Terminal(cmd.Cmd):
		prompt = "ext2terminal$ "
		
		def __init__(self, source, verbose):
				super().__init__()
				self.ext2 = Ext2(source)

		def do_ls(self, arg):
				long = '-l' in arg.split()
				self.ext2.ls(long)
	
		def do_cd(self, arg):
				self.ext2.cd(arg)

		def do_pwd(self, arg):
				self.ext2.pwd()

		def do_dump(self, arg):
				"""copy a file from the file system to the local file system."""
				parts = arg.split()
				if len(parts) != 2:
						print("Usage: dump <file> <destination_path>")
						return
				file, destination = parts
				self.ext2.dump(file, destination)

		def do_exit(self, arg):
				print("Exiting mini-terminal.")
				self.ext2.io.close()
				return True  # signals cmd.Cmd to stop the Cmd instance loop

		def default(self, line):
				print(f"Command '{line}' not recognized.") 