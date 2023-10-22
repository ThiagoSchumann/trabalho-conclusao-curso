import os

path = r'C:\Projects\trabalho-conclusao-curso\project\LaTeX-project'
trash_files = ['.aux',
               '.gz',
               '.bbl',
               '.blg',
               '.brf',
               '.fdb_latexmk',
               '.fls',
               '.idx',
               '.ilg',
               '.ind',
               '.log',
               '.lof',
               '.lot',
               '.toc']
exclude_directories = [path + r'\Compile',
                       path + r'\Scripts']
directories = []


def find_directories():
    directories.append(path)
    for file in os.scandir(path):
        split_tup = os.path.splitext(file.path)
        file_extension = split_tup[1]
        if file_extension == '':
            directories.append(file.path)


def clear_trash():
    find_directories()
    for directory in directories:
        if directory not in exclude_directories:
            for file in os.scandir(directory):
                split_tup = os.path.splitext(file.path)
                file_extension = split_tup[1]
                if file_extension in trash_files:
                    os.remove(file.path)


if __name__ == '__main__':
    clear_trash()
