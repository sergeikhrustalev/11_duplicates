import os
import sys


def get_walked_data(searchpath):
    filelist = []
    for dirpath, dirnames, filenames in os.walk(searchpath):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):

                filelist.append(
                    (filepath, (filename, os.path.getsize(filepath)))
                )

    return filelist


def find_duplicate_files(filelist):
    fileinfo_list = [fileinfo[1] for fileinfo in filelist]

    duplicates_only = [
        fileinfo for fileinfo in fileinfo_list
        if fileinfo_list.count(fileinfo) > 1
    ]

    found_duplicates = []
    for filepath, fileinfo in filelist:
        if fileinfo in duplicates_only:
            found_duplicates.append((filepath, fileinfo[0], fileinfo[1]))
    return found_duplicates


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Syntax: duplicates.py <directory_path>')

    filelist = get_walked_data(sys.argv[1])
    found_duplicates = find_duplicate_files(filelist)
    if not found_duplicates:
        sys.exit('Path not exist or directory is empty')

    found_duplicates.sort(key=lambda file_item: file_item[1])
    current_filename = found_duplicates[0][1]
    current_filesize = found_duplicates[0][2]

    print('{} - {} bites found on the following path: '.format(
        current_filename, current_filesize)
    )

    for filepath, filename, filesize in found_duplicates:
        if filename != current_filename:
            current_filename = filename
            current_filesize = filesize

            print('{} - {} bites found on the following path: '.format(
                current_filename, current_filesize)
            )

        print('\t{}'.format(filepath))
