from openpyxl.worksheet import worksheet
from icecream import ic


from sqlite_tools import dbControl, sql_counts
from excel_tools.statistic_output import statistic_header_output, statistic_item_output, statistic_quote_output


def count_statistic_output(sheet: worksheet, db_file_name: str, start_line: int, chapter_code: str, period: int) -> bool:
    """ Записывает статистику для периода period на лист sheet начиная со строки start_line. """
    # ic.disable()
    with dbControl(db_file_name) as db:
        like_template = f"{chapter_code}.%"
        row = start_line
        result = db.run_execute(sql_counts["count_items_period_code"], (period, like_template))
        if result:
            lines = result.fetchall()
            row = statistic_header_output(chapter_code, period, sheet, row)+1
            for line in lines:
                ic(dict(line))
                row = statistic_item_output(line, sheet, row)
        result = db.run_execute(sql_counts["count_quotes_period_code"], (period, like_template))
        if result:
            line = result.fetchone()
            ic(dict(line))
            statistic_quote_output(line, sheet, row)


    return False
