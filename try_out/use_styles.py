from excel_tools import ExcelControl, styles

excel_file_name = "template.xlsx"

with ExcelControl(excel_file_name) as exl:
    exl.create_sheets(["data", "statistics"])  # создать листы книги
    exl.set_sheet_grid(sheet_name="data", grid=False)  # убрать сетку
    exl.book['data'].sheet_properties.outlinePr.summaryBelow = False  # группировка сверху
    exl.styles_init(styles, )  # прописать стили оформления

    exl.book.active = exl.book['data']
    exl.sheet = exl.book['data']

    exl.sheet.cell(row=2, column=2).value = "Hello guys!"
    exl.book.active.cell(row=2, column=2).style = 'title_basic'
