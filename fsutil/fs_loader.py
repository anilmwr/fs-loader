import os
import os.path
import logging
import random
import string
import itertools
import time
import threading


# set logging format
logging_format = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=logging_format)

# get logger instance
logger = logging.getLogger('FS-Loader')


class FileSystemLoader:
    def __init__(self, mount_directory: str, sub_directory_depth: int, file_count_per_directory: int,
                 sub_directory_count: int = 10, block_size: int = 4096, min_block_count: int = 1,
                 max_block_count: int = 256, directory_prefix='dir') -> None:
        # check if mount directory exists
        if os.path.isdir(mount_directory):
            # check if mount directory is writable
            if os.access(mount_directory, os.W_OK | os.X_OK):
                self.mount_directory = mount_directory
            else:
                raise ValueError(f'Mount directory exists but not writable: {mount_directory}')
        else:
            raise ValueError(f'Mount directory doesn\'t exist: {mount_directory}')

        if directory_prefix == '':
            raise ValueError('Directory prefix is empty')
        
        # check if rest of the arguments are positive integers
        for parameter in [sub_directory_depth, file_count_per_directory, sub_directory_count,
                          block_size, min_block_count, max_block_count]:
            if not isinstance(parameter, int) or parameter <= 0:
                raise ValueError(f'Positive integer expected, received: {repr(parameter)}')
        
        self.sub_directory_depth = sub_directory_depth
        self.file_count_per_directory = file_count_per_directory
        self.sub_directory_count = sub_directory_count
        self.block_size = block_size
        self.min_block_count = min_block_count
        self.max_block_count = max_block_count
        self.directory_prefix = directory_prefix
        self.current_file_count = 0

    def load_fs(self) -> None:
        # start a daemon thread to display progress
        t = threading.Thread(target=self.display_progress, daemon=True)
        t.start()

        for directory_ids in itertools.product(range(1, self.sub_directory_count + 1), repeat=self.sub_directory_depth):
            # recursive call to create sub directory tree
            current_directory_path = self.mount_directory

            # generate path for sub directory with all in-between directories
            for i in range(1, len(directory_ids) + 1):
                sub_dir_name = os.path.join(current_directory_path, self.directory_prefix + '_'.join(map(str, directory_ids[:i])))
                current_directory_path = os.path.join(current_directory_path, sub_dir_name)

            try:
                os.makedirs(current_directory_path)
            except IOError as e:
                logging.error(f'Unable to create directory {current_directory_path}: {str(e)}')
                return

            # repeat for number of files to be created in sub directory
            for file_index in range(1, self.file_count_per_directory + 1):
                current_file_path = os.path.join(current_directory_path, str(file_index) + '.txt')

                # get random integer in the range min_block_count and max_block_count inclusive
                file_block_count = random.randint(self.min_block_count, self.max_block_count)

                try:
                    # open, write and close file
                    with open(current_file_path, 'w', encoding='utf-8') as file_handle:
                        # repeat for number of blocks
                        for _ in range(file_block_count):
                            # create random text of block size
                            text_block = ''.join(random.choice(
                                    string.ascii_uppercase + string.ascii_lowercase + string.digits
                                ) for _ in range(self.block_size))
                            
                            # write text block to file handle
                            file_handle.write(text_block)
                    
                    # increment file count for progress
                    self.current_file_count += 1
                except IOError as e:
                    logging.error(f'Unable to create file {current_file_path}: {str(e)}')
                    return
        
        print('\x1b[1K\rCompleted')
    
    def display_progress(self) -> None:
        progress_percent = 0
        file_count_tobe_created = self.get_file_count_tobe_created()
        print(f'\rFiles created: {self.current_file_count:10d} Completed: {progress_percent:3d}%', end='')

        while (progress_percent < 100):
            print(f'\rFiles created: {self.current_file_count:10d} Completed: {progress_percent:3d}%', end='')
            current_progress_percent = int((self.current_file_count / file_count_tobe_created) * 100)
            if (current_progress_percent > progress_percent):
                progress_percent = current_progress_percent
            
            time.sleep(1)
    
    def get_file_count_tobe_created(self) -> int:
        return (self.sub_directory_count ** self.sub_directory_depth) * self.file_count_per_directory
