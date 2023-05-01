# FS-Loader

FS-Loader is a program implemented in Python 3 for recursively creating a large number of directories and files.

Below are the command line parameters for the script:
- `--mount-directory`
  - Required
  - This is the root directory path under which you want to create sub-directories and files
- `--sub-directory-depth`
  - Optional, default=5
  - This is the sub-directory depth to be created
- `--sub-directory-count`
  - Optional, default=10
  - This is the count of sub-directories to create under each directory
- `--file-count-per-directory`
  - Optional, default=10
  - This is the count of files to be created under each sub-directory
- `--directory-prefix`
  - Optional, default='dir'
  - This is the directory name prefix
- `--block-size`
  - Optioal, default=4096
  - This is the number of bytes to write in one write operation
- `--min-block-count`
  - Optional, default=1
  - This is the minimum number of blocks to write to a file
  - With default block size of 4096 bytes and minimum block count of 1, 4kB data will be written to the file
- `--max-block-count`
  - Optioal, default=256
  - This is the maximum number of blocks to write to a file
  - With default block size of 4096 bytes and maximum block count of 256, 1MB data will be written to the file


## Features
- The script displays progress percentage


## Sample Cmmand

`./fs_loader_main.py --mount-directory '/mnt/test/' --sub-directory-depth 3 --file-count-per-directory 5`


## Sample Directory Structure Created By The Script

```
$ tree /mnt/test
.
└── dir1
    └── dir1_1
        └── dir1_1_1
            ├── dir1_1_1_1
            │   ├── dir1_1_1_1_1
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   ├── dir1_1_1_1_10
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   ├── dir1_1_1_1_2
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   ├── dir1_1_1_1_3
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   ├── dir1_1_1_1_4
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   ├── dir1_1_1_1_5
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   ├── dir1_1_1_1_6
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   ├── dir1_1_1_1_7
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   ├── dir1_1_1_1_8
            │   │   ├── 1.txt
            │   │   ├── 10.txt
            │   │   ├── 2.txt
            │   │   ├── 3.txt
            │   │   ├── 4.txt
            │   │   ├── 5.txt
            │   │   ├── 6.txt
            │   │   ├── 7.txt
            │   │   ├── 8.txt
            │   │   └── 9.txt
            │   └── dir1_1_1_1_9
            │       ├── 1.txt
            │       ├── 10.txt
            │       ├── 2.txt
            │       ├── 3.txt
            │       ├── 4.txt
            │       ├── 5.txt
            │       ├── 6.txt
            │       ├── 7.txt
            │       ├── 8.txt
            │       └── 9.txt
.
.
.
```

