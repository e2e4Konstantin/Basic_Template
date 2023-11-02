from excel_tools.excel_settings import ExcelControl
from excel_tools.machines.excel_machines_layout import machines_styles
from excel_tools.machines.basic_machine_header_output import basic_machine_header_output
from excel_tools.machines.output_chapter_machines import output_chapter_machines
from excel_tools.machines.count_statistic_machines import output_statistic_machines_chapter


def create_basic_machines_template(db_file_name: str, excel_file_name: str, chapter_code: str, period: int, grid: bool = False):
    """ Создает шаблон для параметризации 'машин', глава 'chapter' периода 'period'. """

    with ExcelControl(excel_file_name) as exl:
        exl.create_sheets(["data", "statistics"])  # создать листы книги
        exl.set_sheet_grid(sheet_name="data", grid=False)  # убрать сетку
        exl.book['data'].sheet_properties.outlinePr.summaryBelow = False  # группировка сверху
        exl.styles_init(machines_styles.values())  # загрузить стили оформления
        exl.sheet = exl.book['data']
        basic_machine_header_output(exl.sheet)  # выводим в файл основную шапку

        start_chapter_row = 4
        output_chapter_machines(exl.sheet, db_file_name, start_chapter_row, chapter_code, period)

        exl.sheet = exl.book['statistics']
        output_statistic_machines_chapter(
            exl.sheet, db_file_name, start_line=5, chapter_code=chapter_code, period=period
        )

        # # вставляем один столбец
        # ex.sheet.insert_cols(1)
