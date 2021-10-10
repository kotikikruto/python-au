from file_reader import FileReaderResult


class MdGenerator:
    def __init__(self, file_reader_result: FileReaderResult):
        self.file_reader_result = file_reader_result

    def _generate_task_name(self) -> str:
        return f'# {self.file_reader_result.task_name}\n\n'

    def _generate_task_description(self) -> str:
        return f'{self.file_reader_result.task_text}\n\n'

    def _generate_task_link(self) -> str:
        return f'[{self.file_reader_result.task_name}]({self.file_reader_result.url})\n\n'

    def _generate_task_tests(self) -> str:
        return (f'<details><summary>Test cases</summary><blockquote>\n\n'
                + f'```python\n{self.file_reader_result.tests}```\n</blockquote></details>\n\n')

    def _generate_task_solution(self) -> str:
        return f'```python\n{self.file_reader_result.solution}```\n'

    def generate(self) -> str:
        result = ""

        result += self._generate_task_name()
        result += self._generate_task_description()
        result += self._generate_task_link()
        result += self._generate_task_tests()
        result += self._generate_task_solution()

        return result

