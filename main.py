

from excel_tools import create_basic_template



if __name__ == '__main__':
    period = 68
    chapter = '6'
    excel_file_name = r".\output\template.xlsx"
    db_file_name = r".\src\Quotes.sqlite"


    print(f"Создание шаблона. Период: {period} Глава: {chapter!r}")
    create_basic_template(db_file_name, excel_file_name, chapter, period)




