from icecream import ic
from itertools import chain

from sqlite_tools import dbControl

db_file = r"C:\Users\kazak.ke\PycharmProjects\development\Basic_Template\src\Quotes_machines.sqlite"

with dbControl(db_file) as db:
    # r = db.connection.execute("""SELECT * FROM tblMachinesCatalog WHERE ID_parent = 5;""")
    # ic(r, type(r)) # , r.description
    #
    # try:
    #     first_row = next(r)
    #     for row in chain((first_row,), r):
    #         ic(tuple(row))
    # except StopIteration as e:
    #     ic('StopIteration')

    #
    # # rows = r.fetchall()
    # # ic(rows)
    # # ic([tuple(x) for x in rows])
    # print()



    c = db.connection.execute("""SELECT count(*) FROM tblMachinesCatalog WHERE ID_parent = 100;""")
    ic(c, type(c)) # , c.description
    rw = c.fetchall()
    ic(rw)
    ic(tuple(rw[0]))

    res = db.connection.execute("SELECT name FROM sqlite_master WHERE name='tblMachinesCatalog'")
    ic(res.fetchone() is None)