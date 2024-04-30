from .terminal import Terminal
from argparse import ArgumentParser

def main():
		parser = ArgumentParser(prog = 'ext2term', description = 'A CLI tool to navigate an ext2 filesystem through a virtual terminal', epilog = 'Thanks for using ext2term by William Guerrand')
		parser.add_argument('-v', '--verbose', action='store_true', default=True, help='Makes ext2term verbose during the operation.')
		parser.add_argument('-s', '--source', type=str, required=True, help='The file system image you wish to use with this tool.')
		args = parser.parse_args()

		Terminal(args.source, args.verbose).cmdloop()

if __name__ == '__main__':
		main()