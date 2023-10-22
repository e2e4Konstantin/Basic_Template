from openpyxl.worksheet import worksheet
from openpyxl.utils.cell import column_index_from_string
from openpyxl.styles import numbers
import sqlite3

from file_tools import output_message


def _range_decorating(sheet: worksheet, row, columns: list[str], style_name: str):
    """ Устанавливает стиль style_name для ячеек из списка columns """
    for column in columns:
        sheet.cell(row=row, column=column_index_from_string(column)).style = style_name


def _chapter_line_output(data: sqlite3.Row, sheet: worksheet, row: int, group_number: int) -> int:
    """ Записывает данные о главе на лист sheet в строку row. """
    sheet.cell(row=row, column=column_index_from_string('A')).value = data['code']
    title = f"Глава {data['code']}. {data['description']}"
    sheet.cell(row=row, column=column_index_from_string('G')).value = title
    # ставим группировку
    sheet.row_dimensions.group(row, row + 2, outline_level=group_number)
    # ставим стили
    _range_decorating(sheet, row, ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'chapter_line')
    return row + 1


def _collection_line_output(data: sqlite3.Row, sheet: worksheet, row: int, group_number: int) -> int:
    """ Записывает данные data 'Сборника' на лист sheet в строку row, с группировкой group_number. """

    sheet.cell(row=row, column=column_index_from_string('A')).value = parent_code
    sheet.cell(row=row, column=column_index_from_string('B')).value = data['code']
    title = f"Сборник {data['code']}. {data['description']}"
    sheet.cell(row=row, column=column_index_from_string('G')).value = title
    # ставим группировку
    sheet.row_dimensions.group(row, row + 1, outline_level=group_number)
    # ставим стили
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for column in columns:
        sheet.cell(row=row, column=column_index_from_string(column)).style = 'chapter_line'
        sheet.cell(row=row, column=column_index_from_string(column)).number_format = numbers.FORMAT_TEXT
    return row + 1


def _section_line_output(data: sqlite3.Row, sheet: worksheet, row: int, group_number: int) -> int:
    """ Записывает данные о _____ на лист sheet в строку row. """
    return row + 1


def _subsection_line_output(data: sqlite3.Row, sheet: worksheet, row: int, group_number: int) -> int:
    """ Записывает данные о _____ на лист sheet в строку row. """
    return row + 1


def _table_line_output(data: sqlite3.Row, sheet: worksheet, row: int, group_number: int) -> int:
    """ Записывает данные о _____ на лист sheet в строку row. """
    return row + 2


def _quote_line_output(data: sqlite3.Row, sheet: worksheet, row: int, group_number: int) -> int:
    """ Записывает данные о _____ на лист sheet в строку row. """
    return row + 1


def _item_output(data: sqlite3.Row, sheet: worksheet, start_row: int) -> int:
    """ Выводит данные об объекте каталога"""
    size = 1
    match data['item']:
        case "глава":
            return _chapter_line_output(data, sheet, start_row, group_number=1)
        case "сборник":
            row = _collection_line_output(data, sheet, start_row, group_number=2)
        case "отдел":
            row = _section_line_output(data, sheet, start_row, group_number=3)
        case "раздел":
            row = _subsection_line_output(data, sheet, start_row, group_number=1)
        case "таблица":
            row = _table_line_output(data, sheet, start_row, group_number=1)
        case "расценка":
            row = _quote_line_output(data, sheet, start_row, group_number=1)
        case _:  # непонятно
            output_message(f"непонятная единица каталога:", f"-- ?? --> {tuple(data)}")
