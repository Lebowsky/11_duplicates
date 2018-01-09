import os


def get_duplicate_files(path):

    list_files = []

    for path_dir, directories, files in os.walk(path):
        for file_name in files:
            full_path = os.path.join(path_dir, file_name)
            file_size = os.path.getsize(full_path)
            file_attributes = {
                'file_name': file_name,
                'file_size': file_size,
                'file_full_path': full_path,
            }
            list_files.append(file_attributes)


if __name__ == '__main__':
    path = 'D:\Temp'
    duplicates = get_duplicate_files(path)

