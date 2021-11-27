from config import Config
from file_reader import FileReader
from md_generator import MdGenerator


def main():
    config = Config(path_to_task_text="test_data/task.txt", path_to_solution="test_data/solution.py",
                    path_to_result="task.md", url="https://leetcode.com/problems/sort-list/",
                    path_to_tests="test_data/tests.py", task_name="Sort List")

    file_reader = FileReader(config)
    file_reader_result = file_reader.read()
    md_generator = MdGenerator(file_reader_result)
    md_file = md_generator.generate()

    with open(config.path_to_result, 'w') as f:
        f.write(md_file)


if __name__ == "__main__":
    main()
