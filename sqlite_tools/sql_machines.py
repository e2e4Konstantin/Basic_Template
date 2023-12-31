sql_machines = {

    "select_catalog_period_code_item": """
        SELECT c.ID_tblMachinesCatalog, c.period, c.code, i.name AS item, c.description
        FROM tblMachinesCatalog AS c
        LEFT JOIN tblMachineItems AS i ON i.ID_tblMachineItem = ID_tblMachinesCatalog_tblMachineItems
        WHERE c.period = ? AND c.code = ? AND i.name = ?;
        """,

    "select_catalog_parent":  """
        SELECT c.ID_tblMachinesCatalog, c.period, c.code, i.name AS item, c.description, c.raw_parent, c.ID_parent, c.ID_tblMachinesCatalog_tblMachineItems
        FROM tblMachinesCatalog AS c 
        LEFT JOIN tblMachineItems AS i ON i.ID_tblMachineItem = ID_tblMachinesCatalog_tblMachineItems
        WHERE c.ID_parent <> c.ID_tblMachinesCatalog and c.ID_parent = ?;
        """,

    "select_machines_catalog_id": """
        SELECT * FROM tblMachines WHERE FK_tblMachines_tblMachinesCatalog = ?;
        """,

    "count_catalog_period_code_mask": """
        SELECT c.period, c.code, i.name AS item, COUNT(*) AS count
        FROM tblMachinesCatalog AS c 
        LEFT JOIN tblMachineItems AS i ON i.ID_tblMachineItem = ID_tblMachinesCatalog_tblMachineItems 
        WHERE c.period = ? and c.code LIKE ?
        GROUP by i.name
        ORDER BY i.rating DESC;
        """,
    "count_machines_period_code": """
        SELECT COUNT(*) AS count FROM tblMachines AS m  WHERE period = ? and code LIKE ?;  
        """
}
