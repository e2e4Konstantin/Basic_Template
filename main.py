import os
import datetime
from excel_tools import create_basic_template, create_basic_machines_template

if __name__ == '__main__':
    # period = 68
    # chapter = '10'
    # output_file_name = r".\output\template.xlsx"
    # root, ext = os.path.splitext(output_file_name)
    # excel_file_name = f"{root}_{chapter}_{period}-{datetime.date.today().strftime('%d-%m-%Y')}{ext}"
    #
    # db_file_name = r".\src\Quotes.sqlite"
    #
    # print(f"Создание шаблона. Период: {period} Глава: {chapter!r} Файл: {excel_file_name}")
    # create_basic_template(db_file_name, excel_file_name, chapter, period)

    period = 68
    chapter = '2'
    output_file_name = r".\output\template.xlsx"
    root, ext = os.path.splitext(output_file_name)
    excel_file_name = f"{root}_{chapter}_{period}-{datetime.date.today().strftime('%d-%m-%Y')}{ext}"

    db_file_name = r".\src\Quotes_machines.sqlite"

    print(f"Создание шаблона. Период: {period} Глава: {chapter!r} Файл: {excel_file_name}")
    create_basic_machines_template(db_file_name, excel_file_name, chapter, period)



