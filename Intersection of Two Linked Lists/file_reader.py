from dataclasses import dataclass

from config import Config


@dataclass
class FileReaderResult:
    task_text: str
    url: str
    task_name: str
    solution: str
    tests: str


class FileReader:
    def __init__(self, config: Config):
        self.config = config

    def read(self) -> FileReaderResult:
        with open(self.config.path_to_task_text, 'r') as f:
            task_text = f.read()
        with open(self.config.path_to_solution, 'r') as f:
            solution = f.read()
        with open(self.config.path_to_tests, 'r') as f:
            tests = f.read()

        return FileReaderResult(task_text=task_text, solution=solution, tests=tests, url=self.config.url,
                                task_name=self.config.task_name)
