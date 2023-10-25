from openpyxl.worksheet import worksheet

from sqlite_tools import dbControl, sql_selects, sql_counts

from file_tools import output_message_exit, output_message
from items_tools import split_code_int
from excel_tools.items_output import item_output, quote_line_output
from icecream import ic, DEFAULT_CONTEXT_DELIMITER


def chapter_output(sheet: worksheet, db_file_name: str, start_line: int, chapter_code: str, period: int) -> bool:
    """
    Записывает информацию из каталога о главе chapter для периода period на лист sheet начиная со строки start_line.
    """
    with dbControl(db_file_name) as db:
        # ищем в БД главу с указанным кодом и периодом
        root_item = "глава"
        result = db.run_execute(sql_selects["select_code_period_item_catalog"], (chapter_code, root_item, period))
        if result:
            chapters = result.fetchall()
            if chapters:
                # берем первую найденную
                chapter = chapters[0]
                # выводим главу
                row = item_output(sheet, chapter, start_line)
                chapter_id = chapter["ID_tblCatalog"]
                row = _slaves_quotes(sheet, db, chapter_id, start_row=row)
                ic(chapter, chapter_id)
                ic(tuple(chapter))
                # print(chapter, chapter_id, tuple(chapter))
                row = _slaves_output(sheet, db, chapter_id, start_row=row)
                return True
            else:
                output_message_exit(f"в каталоге для периода {period} не найдено главы:",
                                    f"шифр главы: {chapter_code!r}")
        else:
            output_message_exit(f"в каталоге для периода {period} не найдено главы:", f"шифр главы: {chapter_code!r}")
    return False


def _slaves_output(sheet: worksheet, db: dbControl, master_id: int, start_row: int) -> int:
    """ Рекурсивная функция. Из БД таблицы tblCatalogs получает строки у которых родитель == master_id,
        сортирует их по шифру, выводит их и запрашивает вывод 'нижестоящей'.
    """
    result = db.run_execute(sql_selects["select_parent_catalog"], (master_id,))
    lines = result.fetchall()
    row = start_row
    if lines:
        items = [x for x in lines]
        items.sort(key=lambda x: split_code_int(x['code']))
        for item in items:
            row = item_output(sheet, item, row)
            item_id = item['ID_tblCatalog']
            row = _slaves_quotes(sheet, db, item_id, start_row=row)
            row = _slaves_output(sheet, db, item_id, start_row=row)
        return row
    return start_row


def _slaves_quotes(sheet: worksheet, db: dbControl, master_id: int, start_row: int) -> int:
    """ Из БД таблицы tblQuotes получает строки у которых FK_tblQuotes_tblCatalogs == master_id.
        Расценки у которых внешний ключ равен искомому.
        Сортирует их по шифру, выводит.
    """
    result = db.run_execute(sql_selects["select_quotes_for_id_table"], (master_id,))
    lines = result.fetchall()
    row = start_row
    if lines:
        group_level = 6
        quotes = [x for x in lines]
        quotes.sort(key=lambda x: split_code_int(x['code']))
        for quote in quotes:
            row = quote_line_output(quote, sheet, row, group_number=group_level)
        # добавить пустую строку
        sheet.append([""])
        sheet.row_dimensions.group(row, row + 1, outline_level=group_level)
        row += 1
    return row


