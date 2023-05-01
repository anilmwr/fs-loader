#!/usr/bin/env python3

import sys
import argparse
from fsutil.fs_loader import FileSystemLoader


def main(mount_directory, sub_directory_depth, file_count_per_directory, sub_directory_count, directory_prefix,
         block_size, min_block_count, max_block_count):
    try:
        fs_loader = FileSystemLoader(mount_directory, sub_directory_depth, file_count_per_directory,
                                  sub_directory_count=sub_directory_count, directory_prefix=directory_prefix,
                                  block_size=block_size, min_block_count=min_block_count, max_block_count=max_block_count)
        fs_loader.load_fs()
    except KeyboardInterrupt:
        print('Interrupted by user')
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mount-directory', type=str, help='Mount directory path', required=True)
    parser.add_argument('--sub-directory-depth', type=int, help='Sub directory tree depth', required=False, default=5)
    parser.add_argument('--file-count-per-directory', type=int, help='File count per directory', required=False, default=10)
    parser.add_argument('--sub-directory-count', type=int, help='Sub-directory count', required=False, default=10)
    parser.add_argument('--directory-prefix', type=str, help='Directory name prefix', required=False, default='dir')
    parser.add_argument('--block-size', type=int, help='Block size for write', required=False, default=4096)
    parser.add_argument('--min-block-count', type=int, help='Minimum number of blocks to write to each file', required=False, default=1)
    parser.add_argument('--max-block-count', type=int, help='Maximum number of block to write to each file', required=False, default=256)
    
    args = parser.parse_args()
    mount_directory = args.mount_directory
    sub_directory_depth = args.sub_directory_depth
    file_count_per_directory = args.file_count_per_directory
    sub_directory_count = args.sub_directory_count
    directory_prefix = args.directory_prefix
    block_size = args.block_size
    min_block_count = args.min_block_count
    max_block_count = args.max_block_count

    if directory_prefix == '':
        print('Directory prefix is empty')
        sys.exit(1)
    
    if any(i <= 0 for i in [sub_directory_depth, file_count_per_directory, sub_directory_count, block_size,
                            min_block_count, max_block_count]):
        print('Positive integer argument expected')
        sys.exit(1)
    
    if max_block_count < min_block_count:
        print('Max block count cannot be less than min block count')
        sys.exit(1)

    main(mount_directory, sub_directory_depth, file_count_per_directory, sub_directory_count, directory_prefix,
         block_size, min_block_count, max_block_count)
