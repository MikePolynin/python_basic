import os


def gen_files_path(looking_dir: str, address: str = os.path.abspath(os.sep)) -> str:
    for elem in os.listdir(address):
        yield os.path.join(address, elem)

    for elem in os.listdir(address):
        if os.path.isdir(os.path.join(address, elem)):
            if elem == looking_dir:
                print('Find')
            else:
                for element in gen_files_path(looking_dir, os.path.normpath(os.path.join(address, elem))):
                    yield element


for _ in gen_files_path('asd', 'F:\\SkillBox\\python_basic\\Module26\\03_files_path'):
    print(_)
