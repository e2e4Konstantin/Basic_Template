import os
from file_tools.message import output_message_exit


def check_file_location(path_name: str, file_name: str) -> str:
    """ Создает маршрут к файлу. Проверяет что такой файл и папка существуют."""
    abs_file = os.path.join(path_name, file_name)
    if not os.path.isdir(path_name):
        output_message_exit(f"папка не найдена", f"{path_name!r}")
    if not os.path.exists(abs_file):
        output_message_exit(f"фал не найден:", f"{abs_file!r}")
    return abs_file
