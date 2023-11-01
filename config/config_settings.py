from collections import namedtuple

ItemQuoteCode = namedtuple(
    typename='ItemQuoteCode',
    field_names=['chapter', 'collection', 'section', 'subsection', 'table_one', 'table_two', 'quote'],
    defaults=['', '', '', '', '', '', '']
)


ItemMachineCode = namedtuple(
    typename='ItemMachineCode',
    field_names=['chapter', 'subsection', 'group', 'machine'],
    defaults=['', '', '', '']
)




if __name__ == "__main__":
    from items_tools import split_code





    quote_code = "6.62-1-4-0-41-99"
    table_code = "6.62-1-4-0-41"
    subsection_code = "6.54-1-2"

    tab_dev_code = split_code(table_code)

    tc = ItemQuoteCode(*tab_dev_code)
    print(tc)

    ss_dev_code = split_code(subsection_code)
    ssc = ItemQuoteCode(*ss_dev_code)
    print(ssc)

    print(tc.chapter, ssc.collection)

    print(ItemQuoteCode._fields)
    print(len(ItemQuoteCode._fields))
