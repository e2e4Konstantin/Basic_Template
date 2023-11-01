import re

import config


def split_code(src_code: str) -> tuple:
    """ Разбивает шифр на части. '4.1-2-10' -> ('4', '1', '2', '10')"""
    return tuple(re.split('[.-]', src_code)) if src_code else tuple()


def split_code_int(src_code: str):
    """ Разбивает шифр на части из чисел. '4.1-2-10' -> (4, 1, 2, 10) """
    return tuple(map(int, re.split('[.-]', src_code))) if src_code else tuple()


def split_code_quote(src_code: str) -> config.ItemQuoteCode:
    """ Разбивает шифр расценки на части из строк.
        '4.1-2-10' -> ('4', '1', '2', '10').
        Возвращает именованный кортеж.
     """
    return config.ItemQuoteCode(*split_code(src_code))


def split_code_machine(src_code: str) -> config.ItemMachineCode:
    """ Разбивает шифр расценки на части из строк.
        '4.1-2-10' -> ('4', '1', '2', '10').
        Возвращает именованный кортеж.
     """
    return config.ItemMachineCode(*split_code(src_code))


if __name__ == "__main__":
    table_code = "6.62-1-4-0-41"
    subsection_code = "6.54-1-2"
    chapter_code = "6"
    quote_code = "6.62-1-4-0-41-99"

    machine_code = "2.1-1-12"
    print(f"{machine_code} -> {split_code_machine(machine_code)}")

    print(f"{table_code} -> {split_code_quote(table_code)}")
    print(f"{subsection_code} -> {split_code_quote(subsection_code)}")
    print(f"{chapter_code} -> {split_code_quote(chapter_code)}")
    print(f"{quote_code} -> {split_code_quote(quote_code)}")
