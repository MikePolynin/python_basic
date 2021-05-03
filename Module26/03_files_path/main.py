import os


def gen_files_path(looking_dir: str, address: str = os.path.abspath(os.sep)) -> None:
    for elem in os.listdir(address):
        if os.path.isdir(os.path.join(address, elem)):
            if elem == looking_dir:
                print('Find')
            else:
                directory = os.path.join(address, elem)
                all_file_path = (os.path.join(directory, file) for file in os.listdir(directory))

                for file_path in all_file_path:
                    print(file_path)

                gen_files_path(looking_dir, os.path.join(address, elem))


gen_files_path('asd', 'D:\\SkillBox\\python_basic\\Module26\\03_files_path')
