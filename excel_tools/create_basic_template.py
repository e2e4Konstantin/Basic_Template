

def create_basic_template(db_file_name: str, output_file_name: str, chapter: int, period: int, grid: bool = False):
    """ Создает шаблон для параметризации расценок для главы 'chapter' периода 'period'. """

    output = ExcelControl(output_file_name)
    with output as ex:
        sheets_name = ["name", "stat"]
        ex.create_sheets(sheets_name)
        ex.styles_init()
        ex.sheet = ex.book['name']
        ex.set_sheet_grid(grid=grid)
        ex.sheet.sheet_properties.outlinePr.summaryBelow = False  # группировка сверху

        create_basic_header(ex.sheet)
        start_chapter_row = 4
        chapters_output(ex.sheet, catalog, start_chapter_row)
        # # вставляем один столбец
        # ex.sheet.insert_cols(1)