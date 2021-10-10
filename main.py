from config import Config
from file_reader import FileReader
from md_generator import MdGenerator


def main():
    config = Config(path_to_task_text="test_data/task.txt", path_to_solution="test_data/solution.py",
                    path_to_result="test_data/task.md", url="https://leetcode.com/problems/squares-of-a-sorted-array/",
                    path_to_tests="test_data/tests.py", task_name="Squares of a Sorted Array")

    file_reader = FileReader(config)
    file_reader_result = file_reader.read()
    md_generator = MdGenerator(file_reader_result)
    md_file = md_generator.generate()

    with open(config.path_to_result, 'w') as f:
        f.write(md_file)


if __name__ == "__main__":
    main()
