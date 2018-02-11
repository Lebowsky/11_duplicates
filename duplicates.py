import os
import sys
from collections import Counter


def get_duplicate_files(path):

    dict_files = {}
    counter = Counter()
    for path_dir, directories, files in os.walk(path):
        for file_name in files:
            full_path = os.path.join(path_dir, file_name)
            file_size = os.path.getsize(full_path)
            key = (file_name, file_size)

            file_paths = dict_files.get(key, [])
            file_paths.append(full_path)
            dict_files[key] = file_paths
            counter[key] += 1

    duplicates = [dict_files[key] for key, count in counter.items() if count > 1]
    return duplicates


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You can use: $ python duplcates.py <path to find duplicates>')
        exit(-1)
    path = sys.argv[1]
    duplicates = get_duplicate_files(path)

    for file_duplicate in duplicates:
        for path_to_file in file_duplicate:
            print(path_to_file)
        print()
