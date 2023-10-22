import re


def split_code(src_code: str) -> tuple:
    """ Разбивает шифр на части. '4.1-2-10' -> ('4', '1', '2', '10')"""
    return tuple(re.split('[.-]', src_code)) if src_code else tuple()


def split_code_int(src_code: str):
    """ Разбивает шифр на части из чисел. '4.1-2-10' -> (4, 1, 2, 10)"""
    return tuple(map(int, re.split('[.-]', src_code))) if src_code else tuple()