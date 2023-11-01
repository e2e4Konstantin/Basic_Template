from openpyxl.worksheet import worksheet

from sqlite_tools import dbControl, sql_machines

from file_tools import output_message_exit, output_message
from items_tools import split_code_int
from excel_tools.machines.item_machines_output import item_machines_output, machine_line_output
from icecream import ic, DEFAULT_CONTEXT_DELIMITER


def _slaves_machines_output(sheet: worksheet, db: dbControl, master_id: int, start_row: int) -> int:
    """ Из БД таблицы tbl получает строки у которых FK_tblQuotes_tblCatalogs == master_id.
        Машины у которых внешний ключ равен искомому.
        Сортирует их по шифру, выводит.
    """
    result = db.run_execute(sql_machines["select_machines_catalog_id"], (master_id,))
    lines = result.fetchall()
    row = start_row
    if lines:
        group_level = 4
        machines = [x for x in lines]
        machines.sort(key=lambda x: split_code_int(x['code']))
        for machine in machines:
            row = machine_line_output(machine, sheet, row, group_number=group_level)
        # добавить пустую строку
        sheet.append([""])
        sheet.row_dimensions.group(row, row + 1, outline_level=group_level)
        row += 1
    return row


def _slaves_item_output(sheet: worksheet, db: dbControl, master_id: int, start_row: int) -> int:
    """ Рекурсивная функция. Из БД таблицы tblMachinesCatalog получает строки у которых родитель == master_id,
        сортирует их по шифру, выводит их и запрашивает вывод 'нижестоящей'.
    """
    result = db.run_execute(sql_machines["select_catalog_parent"], (master_id,))
    if result:
        lines = result.fetchall()
        row = start_row
        if lines:
            items = [x for x in lines]
            items.sort(key=lambda x: split_code_int(x['code']))
            for item in items:
                row = item_machines_output(sheet, item, row)
                item_id = item["ID_tblMachinesCatalog"]
                row = _slaves_machines_output(sheet, db, item_id, start_row=row)
                row = _slaves_item_output(sheet, db, item_id, start_row=row)
            return row
        else:
            output_message_exit(f"в каталоге МАШИН для для {master_id}", f"не найдено ни одного потомка.")
    else:
        output_message_exit(f"в каталоге МАШИН для для {master_id}", f"не найдено ни одного потомка.")
    return start_row


def chapter_machines_output(sheet: worksheet, db_file_name: str, start_line: int, chapter_code: str, period: int) -> bool:
    """
    Записывает информацию из каталога Машин главе chapter для периода period на лист sheet начиная со строки start_line.
    """
    with dbControl(db_file_name) as db:
        # ищем в БД главу с указанным кодом и периодом
        root_item = "глава"
        result = db.run_execute(sql_machines["select_catalog_period_code_item"], (period, chapter_code, root_item))
        if result:
            chapters = result.fetchall()
            if chapters:
                # берем первую найденную
                chapter = chapters[0]
                # выводим главу
                row = item_machines_output(sheet, chapter, start_line)
                chapter_id = chapter["ID_tblMachinesCatalog"]
                row = _slaves_machines_output(sheet, db, chapter_id, start_row=row)
                ic(chapter_id, tuple(chapter))
                row = _slaves_item_output(sheet, db, chapter_id, start_row=row)
                return True
            else:
                output_message_exit(f"в каталоге МАШИН для периода {period} не найдено главы:",
                                    f"шифр главы: {chapter_code!r}")
        else:
            output_message_exit(f"в каталоге МАШИН для периода {period} не найдено главы:", f"шифр главы: {chapter_code!r}")
    return False


