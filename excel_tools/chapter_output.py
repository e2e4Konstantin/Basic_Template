from openpyxl.worksheet import worksheet

from sqlite_tools import dbControl, sql_selects
from excel_tools.excel_layout import item_index

from file_tools import output_message_exit, output_message
import sqlite3
from openpyxl.utils.cell import column_index_from_string


def _range_decorating(sheet: worksheet, row, columns: list[str], style_name: str):
    """ Устанавливает стиль style_name для ячеек из списка columns """
    for column in columns:
        sheet.cell(row=row, column=column_index_from_string(column)).style = style_name


def _chapter_line_output(chapter_data: sqlite3.Row, sheet: worksheet, row: int) -> int:
    """ Записывает данные о главе на лист sheet в строку row. """

    sheet.cell(row=row, column=column_index_from_string('A')).value = chapter_data['code']
    title = f"Глава {chapter_data['code']}. {chapter_data['description']}"
    sheet.cell(row=row, column=column_index_from_string('G')).value = title
    # группировка 1
    group_number = item_index['chapter'] + 1
    sheet.row_dimensions.group(row, row + 2, outline_level=group_number)

    _range_decorating(sheet, row, ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'chapter_line')
    return row + 1


def chapter_output(sheet: worksheet, db_file_name: str, start_line: int, chapter_code: str, period: int) -> bool:
    """
    Записывает информацию из каталога о главе chapter для периода period на лист sheet начиная со строки start_line.
    """

    with dbControl(db_file_name) as db:
        # chapter_id = db.get_id(sql_selects["select_name_catalog_items"], ("chapter", ))

        db.run_execute(sql_selects["select_code_period_item_catalog"], (chapter_code, "глава", period))
        rows = db.cursor.fetchall()
        if rows:
            print(rows)
            print(tuple(rows[0]))
            row = _chapter_line_output(rows[0], sheet, start_line)
            # вывести подчиненные объекты
            """
            SELECT *, item.name FROM tblCatalogs 
	            LEFT JOIN tblCatalogItems AS item ON item.ID_tblCatalogItem = FK_tblCatalogs_tblCatalogItems
	            WHERE ID_parent = 2
            """


            row = slave_item_output()


        else:
            output_message_exit(f"в каталоге для периода {period} не найдено главы:", f"шифр главы: {chapter_code!r}")

    # chapters = _get_chapters(catalog)
    # if chapters:
    #     if 0 < limit <= len(chapters):
    #         chapters = chapters[: limit]
    #     # print(f"главы ({len(chapters)}): {chapters}")
    #     row = start_line
    #     for chapter in chapters:
    #         row = _chapter_line_output(chapter, catalog, sheet, row)
    #         # print(f"{catalog.chapters[chapter].code!r} {catalog.chapters[chapter].title}")
    #         row = quotes_output(sheet, catalog, row, chapter=chapter)
    #         row = tables_output(sheet, catalog, row, chapter=chapter)
    #         row = subsections_output(sheet, catalog, row, chapter=chapter)
    #         row = sections_output(sheet, catalog, row, chapter=chapter)
    #         row = collection_output(sheet, catalog, row, chapter=chapter)
    #         # row += 1
    #     return True
    # # print(f"нет ни одной Главы")
    return False
