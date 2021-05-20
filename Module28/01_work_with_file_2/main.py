from typing import TextIO


class FileManager:
    def __init__(self, file_name: str, file_method: str) -> None:
        self.file_name = file_name
        self.method = file_method

    def __enter__(self) -> TextIO:
        try:
            self.file = open(self.file_name, self.method)
        except FileNotFoundError:
            self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True
