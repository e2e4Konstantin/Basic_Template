import re

import config


def split_code(src_code: str) -> tuple:
    """ Разбивает шифр на части. '4.1-2-10' -> ('4', '1', '2', '10')"""
    return tuple(re.split('[.-]', src_code)) if src_code else tuple()


def split_code_int(src_code: str):
    """ Разбивает шифр на части из чисел. '4.1-2-10' -> (4, 1, 2, 10) """
    return tuple(map(int, re.split('[.-]', src_code))) if src_code else tuple()


def split_code_name(src_code: str) -> config.ItemCode:
    """ Разбивает шифр на части из строк.
        '4.1-2-10' -> ('4', '1', '2', '10').
        Возвращает именованный кортеж.
     """
    return config.ItemCode(*split_code(src_code))


if __name__ == "__main__":
    table_code = "6.62-1-4-0-41"
    subsection_code = "6.54-1-2"
    chapter_code = "6"
    quote_code = "6.62-1-4-0-41-99"

    print(f"{table_code} -> {split_code_name(table_code)}")
    print(f"{subsection_code} -> {split_code_name(subsection_code)}")
    print(f"{chapter_code} -> {split_code_name(chapter_code)}")
    print(f"{quote_code} -> {split_code_name(quote_code)}")





