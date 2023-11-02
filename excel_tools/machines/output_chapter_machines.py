from openpyxl.worksheet import worksheet

from sqlite_tools import dbControl, sql_machines

from file_tools import output_message_exit, output_message
from items_tools import split_code_int
from excel_tools.machines.item_machines_output import output_machine_catalog_object, machine_line_output
from icecream import ic, DEFAULT_CONTEXT_DELIMITER


def _output_slave_machines(sheet: worksheet, db: dbControl, parent_id: int, start_row: int) -> int:
    """ Из БД таблицы Машин получает строки у которых ссылка на каталог равна parent_id.
        Машины у которых внешний ключ равен parent_id.
        Сортирует их по шифру, выводит в excel файл.
    """
    result = db.run_execute(sql_machines["select_machines_catalog_id"], (parent_id,))
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


def _output_slave_catalog_object(sheet: worksheet, db: dbControl, master_id: int, start_row: int) -> int:
    """ Рекурсивная функция. Из БД таблицы tblMachinesCatalog получает строки у которых родитель == master_id,
        сортирует их по шифру, выводит их и запрашивает вывод 'нижестоящей'.
    """
    # получить подчиненные объекты каталога, у которых ID_parent = master_id
    result = db.run_execute(sql_machines["select_catalog_parent"], (master_id,))
    if result:
        lines = result.fetchall()
        row = start_row
        if lines:
            #
            items = [x for x in lines]
            items.sort(key=lambda x: split_code_int(x['code']))
            for item in items:
                row = output_machine_catalog_object(sheet, item, row)
                item_id = item["ID_tblMachinesCatalog"]
                row = _output_slave_machines(sheet, db, item_id, start_row=row)
                row = _output_slave_catalog_object(sheet, db, item_id, start_row=row)
            return row
    #     else:
    #         output_message(f"в каталоге МАШИН для для ID_parent = {master_id}", f"не найдено ни одного потомка.")
    # else:
    #     output_message(f"в каталоге МАШИН для для {master_id}", f"не найдено ни одного потомка.")
    return start_row


def output_chapter_machines(sheet: worksheet, db_file_name: str, start_line: int, chapter_code: str, period: int) -> bool:
    """
    Выводит информацию по главе chapter из таблиц по Машинам,
    Для периода period на лист sheet начиная со строки start_line.
    """
    with dbControl(db_file_name) as db:
        # ищем в БД главу с указанным кодом и периодом
        root_item = "глава"
        result = db.run_execute(sql_machines["select_catalog_period_code_item"], (period, chapter_code, root_item))
        if result:
            chapters = result.fetchall()
            if chapters:
                # берем первую найденную главу
                chapter = chapters[0]
                # выводим главу
                row = output_machine_catalog_object(sheet, chapter, start_line)
                chapter_id = chapter["ID_tblMachinesCatalog"]
                # выводим Машины у которых родитель эта глава
                row = _output_slave_machines(sheet, db, chapter_id, start_row=row)
                # ic(chapter_id, tuple(chapter))
                # выводим подчиненные объекты каталога
                row = _output_slave_catalog_object(sheet, db, chapter_id, start_row=row)
                return True
            else:
                output_message_exit(f"в каталоге МАШИН для периода {period} не найдено главы:",
                                    f"шифр главы: {chapter_code!r}")
        else:
            output_message_exit(f"в каталоге МАШИН для периода {period} не найдено главы:", f"шифр главы: {chapter_code!r}")
    return False


