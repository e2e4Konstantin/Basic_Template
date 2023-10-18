import os


def file_unused(abs_file_name: str) -> bool:
    """ Проверяет что файл не занят - не используется другим приложением. """
    if abs_file_name:
        if os.path.exists(abs_file_name):
            try:
                os.rename(abs_file_name, abs_file_name)
                return True
            except IOError:
                return False
        else:
            return True
    return False
