from dataclasses import dataclass


@dataclass
class Config:
    """Class which contains config for FileReader"""
    path_to_task_text: str
    path_to_solution: str
    path_to_tests: str

    path_to_result: str

    task_name: str
    url: str
