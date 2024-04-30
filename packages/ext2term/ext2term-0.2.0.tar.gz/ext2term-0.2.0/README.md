# ext2term

`ext2term` is a Python CLI tool and library designed to help users learn about the ext2 file system. It simulates a terminal environment, allowing users to interact with the ext2 file system without the need to mount it on their system.

## Features

- **Navigate Directories**: Use familiar commands like `ls` and `cd` to explore the file structure.
- **View File Contents**: Draft ext2-formatted files to your own file system by using `dump`. 
- **Extensibility**: `ext2term` serves as a Python library, making it possible for other developers to include ext2 functionality in their own Python programs.

## Installation

`pip install ext2term`

## Usage

`ext2term <ext2fs.img>`

This will launch a virtual terminal session where you can start interacting with your ext2 file system. Here are some of the commands available:

- `ls [-l]`: List the contents of the cwd.
- `cd DIRECTORY`: Change into the specified directory.
- `pwd`: Display the current working directory.
- `dump FILE DESTINATION_PATH`: Copy a file from the file system to the local file system.
- `exit`: Close the session and exit the virtual terminal.

## As a Python Library

In addition to being a CLI tool, `ext2term` is also usable as a library. You can import its classes and utilize them in your own Python code to manipulate or analyze an ext2 file system programmatically.

Here's a snippet showing how you could use `ext2term` in your code:

```python
from ext2term import Ext2

# Initialize an Ext2 object with the path to your ext2 filesystem
ext2_fs = Ext2('/path/to/ext2fs.img')

# List the contents of the root directory
ext2_fs.ls()

# Change the directory
ext2_fs.cd('some_directory')

# Print the current working directory
ext2_fs.pwd()
```

## Contributing
I'm open to contributions.

## License
ext2term is released under the BSD 2-Clause License.

## Disclaimer
This tool is for educational purposes only and should not be used on a production environment or to manipulate critical data.