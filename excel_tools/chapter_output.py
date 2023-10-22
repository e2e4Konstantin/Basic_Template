from openpyxl.worksheet import worksheet

from sqlite_tools import dbControl, sql_selects
from excel_tools.excel_layout import item_index

from file_tools import output_message_exit, output_message
import sqlite3


from items_tools import split_code_int




def chapter_output(sheet: worksheet, db_file_name: str, start_line: int, chapter_code: str, period: int) -> bool:
    """
    Записывает информацию из каталога о главе chapter для периода period на лист sheet начиная со строки start_line.
    """

    with dbControl(db_file_name) as db:



        #
        result = db.run_execute(sql_selects["select_code_period_item_catalog"], (chapter_code, "глава", period))
        chapters = result.fetchall()
        # print(chapters)
        if chapters:
            chapter = chapters[0]
            chapter_id = chapter["ID_tblCatalog"]
            print(chapter, chapter_id, tuple(chapter))
            row = _chapter_line_output(chapter, sheet, start_line)
            # получить подчиненные объекты для
            result = db.run_execute(sql_selects["select_parent_catalog_extra"], (chapter_id,))
            slaves = result.fetchall()
            if slaves:
                print([tuple(x) for x in slaves])
            else:
                output_message_exit(f"для периода {period} главы {chapter_code!r}",
                                    f"не найдено ни одного починенного объекта")
            # row = slave_item_output()
        else:
            output_message_exit(f"в каталоге для периода {period} не найдено главы:", f"шифр главы: {chapter_code!r}")


    return False




def _slaves_output(db: dbControl, master_id: int, deep_number: int, start_row: int):
    """ Рекурсивная функция. Из БД таблицы tblCatalogs получает строки у которых родитель == master_id,
        сортирует их по шифру, выводит их и запрашивает вывод 'нижестоящей'.
    """
    result = db.run_execute(sql_selects["select_parent_catalog"], (master_id,))
    lines = result.fetchall()
    if lines:
        deep_number += 1
        items = [x for x in lines]
        items.sort(key=lambda x: split_code_int(x['code']))
        for item in items:
            x = (item['period'], item['code'], item['item'], item['description'])
            row = _item_output(x, deep_number, row)
            item_id = item['ID_tblCatalog']
            row = _slaves_output(db, item_id, deep_number, row)
        return row
    return start_row









    return row + size