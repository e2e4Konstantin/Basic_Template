# https://htmlcolorcodes.com/
# https://htmlcolorcodes.com/color-chart/

from openpyxl.styles import (Border, Side, Color, PatternFill, Font, Alignment, NamedStyle, )

items = ['chapter', 'collection', 'section', 'subsection', 'table', 'quote']

item_index = {item: i for i, item in enumerate(items)}

headers = {
    'A:O': ['глава', 'сборник', 'отдел', 'раздел', 'таблица', 'расценка', 'Наименование ', 'Измеритель',
            'стат.', 'парам.', 'основная', 'родитель', 'алгоритм', 'элемент', 'материал'],

    'P:T': ['от', 'до', 'ед.изм.', 'шаг', 'тип'],

    'K1': 'Дополнительные расценки',
    'N1': 'Атрибуты',
    'P1': 'Название_параметра',

    'K': 'основная',
    'L': 'родитель',
    'M': 'алгоритм',
    'N': 'элемент',
    'O': 'материал',
}

width_columns = {'A': 6, 'B': 6, 'C': 6, 'D': 6, 'E': 10, 'F': 9, 'G': 50, 'H': 7, 'I': 7, 'J': 7,
                 'K': 8, 'L': 8, 'M': 8}

fonts = {
    "title_basic": Font(name="Calibri", sz=8, family=2, b=False, i=False, color=Color(theme=1), scheme="minor"),
    "chapter_line": Font(name="Calibri", sz=8, family=2, b=False, i=False, color=Color(rgb='00D35400'), scheme="minor"),
}

borders = {
    "title_basic": Border(left=Side(border_style="thin", color=Color(rgb='00A0A0A0')),
                          right=Side(border_style="thin", color=Color(rgb='00A0A0A0')),
                          top=Side(border_style="thin", color=Color(rgb='00A0A0A0')),
                          bottom=Side(border_style="thin", color=Color(rgb='00A0A0A0')), ),
    "chapter_line": Border(left=None, right=None, top=None, bottom=None),
}

fills = {
    "title_basic": PatternFill(patternType="solid", fill_type="solid", fgColor=Color(rgb="00FAFAF4")),
    "chapter_line": PatternFill(patternType=None, fill_type=None, fgColor=Color(rgb="00FFFFFF"))
}


aligments = {
    "chapter_line": Alignment(horizontal='left', vertical='bottom', wrap_text=False, shrink_to_fit=False, indent=0),
}



styles = {
    "title_basic": NamedStyle(name="title_basic", font=fonts["title_basic"],
                              border=borders["title_basic"], fill=fills["title_basic"]),
    'chapter_line': NamedStyle(name="chapter_line", font=fonts["chapter_line"], border=borders["chapter_line"],
                               fill=fills["chapter_line"], alignment=aligments["chapter_line"]),
}



