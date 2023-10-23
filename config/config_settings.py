from collections import namedtuple

ItemCode = namedtuple(
    typename='ItemCode',
    field_names=['chapter', 'collection', 'section', 'subsection', 'table_one', 'table_two', 'quote'],
    defaults=['', '', '', '', '', '', '']
)

if __name__ == "__main__":
    from items_tools import split_code

    quote_code = "6.62-1-4-0-41-99"
    table_code = "6.62-1-4-0-41"
    subsection_code = "6.54-1-2"

    tab_dev_code = split_code(table_code)

    tc = ItemCode(*tab_dev_code)
    print(tc)

    ss_dev_code = split_code(subsection_code)
    ssc = ItemCode(*ss_dev_code)
    print(ssc)

    print(tc.chapter, ssc.collection)

    print(ItemCode._fields)
    print(len(ItemCode._fields))
