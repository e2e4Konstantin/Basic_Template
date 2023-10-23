from excel_tools import ExcelControl, styles

excel_file_name = "template.xlsx"

with ExcelControl(excel_file_name) as exl:
    exl.create_sheets(["data", "statistics"])  # создать листы книги
    exl.set_sheet_grid(sheet_name="data", grid=False)  # убрать сетку
    exl.book['data'].sheet_properties.outlinePr.summaryBelow = False  # группировка сверху


    exl.styles_init(styles.values())


    exl.book.active = exl.book['data']
    exl.sheet = exl.book['data']

    named_styles = exl.book.style_names
    print(f"{named_styles = }")

    column = 5

    for i, ns in enumerate(named_styles):
        exl.sheet.cell(row=i+1, column=column).value = ns
        exl.book.active.cell(row=i+1, column=column).style = ns
