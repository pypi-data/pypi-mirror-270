from setuptools import setup, find_packages

setup(
    name='ext2term',
    version='0.2.0',
    author='William Guerrand',
    author_email='guerrandw@gmail.com',
    description='A CLI and library for navigating ext2 filesystems',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ext2term',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # No dependencies, but if this where I'd put them, e.g.:
        # 'requests >= 2.23.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Education',
        'Topic :: System :: Filesystems',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
    ],
    python_requires='>=3.4',
    entry_points={
        'console_scripts': [
            'ext2term=ext2term.cli:main',
        ],
    },
    keywords='ext2 filesystem',
    license='BSD 2-Clause License',
)