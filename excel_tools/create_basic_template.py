from excel_tools.excel_settings import ExcelControl
from excel_tools.excel_layout import styles
from excel_tools.basic_header_output import basic_header_output
from excel_tools.chapter_output import chapter_output


def create_basic_template(db_file_name: str, excel_file_name: str, chapter_code: str, period: int, grid: bool = False):
    """ Создает шаблон для параметризации расценок для главы 'chapter' периода 'period'. """

    with ExcelControl(excel_file_name) as exl:
        exl.create_sheets(["data", "statistics"])  # создать листы книги
        exl.set_sheet_grid(sheet_name="data", grid=False)  # убрать сетку
        exl.book['data'].sheet_properties.outlinePr.summaryBelow = False  # группировка сверху
        exl.styles_init(styles.values())    # загрузить стили оформления
        exl.sheet = exl.book['data']
        basic_header_output(exl.sheet)      # выводим в файл основную шапку

        start_chapter_row = 4
        chapter_output(exl.sheet, db_file_name, start_chapter_row, chapter_code, period)

        # # вставляем один столбец
        # ex.sheet.insert_cols(1)
