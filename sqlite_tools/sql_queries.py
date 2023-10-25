sql_selects = {

    "select_name_catalog_items":    """SELECT ID_tblCatalogItem FROM tblCatalogItems WHERE name IS ?;""",
    "select_all_catalog_items":     """SELECT * FROM tblCatalogItems;""",
    "select_root_catalog_items":    """SELECT * FROM tblCatalogItems WHERE ID_tblCatalogItem = parent_item;""",

    "select_quotes_all":    """SELECT * FROM tblQuotes;""",


    "select_period_code_catalog":   """SELECT ID_tblCatalog FROM tblCatalogs WHERE period = ? and code = ?;""",
    "select_period_catalog":        """SELECT * FROM tblCatalogs WHERE period IS ?;""",
    "select_code_period_item_catalog":   """
            SELECT ID_tblCatalog, period, code, itm.name AS item, description 
            FROM tblCatalogs 
            LEFT JOIN tblCatalogItems AS itm ON itm.ID_tblCatalogItem = FK_tblCatalogs_tblCatalogItems
            WHERE code = ? AND itm.name = ? AND period = ?;
        """,
    "select_parent_catalog":        """
        -- выбирает все записи для родителя '?' исключая корневую запись
        SELECT 
            ID_tblCatalog, period, code, item.name AS item, description, raw_parent, ID_parent, 
            FK_tblCatalogs_tblCatalogItems
        FROM tblCatalogs 
        LEFT JOIN tblCatalogItems AS item ON item.ID_tblCatalogItem = FK_tblCatalogs_tblCatalogItems
        WHERE id_parent <> ID_tblCatalog and id_parent = ?;
        """,

    "select_parent_catalog_extra": """
        SELECT
            ID_tblCatalog, period, code, item.name AS item, item.rank AS "rank" , description, raw_parent, ID_parent,  FK_tblCatalogs_tblCatalogItems
            FROM tblCatalogs 
            LEFT JOIN tblCatalogItems AS item ON item.ID_tblCatalogItem = FK_tblCatalogs_tblCatalogItems
            WHERE id_parent <> ID_tblCatalog and id_parent = ?
            ORDER BY rank;
        """,

    "select_quotes_for_id_table": """SELECT * FROM tblQuotes WHERE FK_tblQuotes_tblCatalogs = ?;""",

}

sql_counts = {
    "count_items_period_code": """
        SELECT period, i.name AS item, COUNT(*) AS count
        FROM tblCatalogs AS c 
        LEFT JOIN tblCatalogItems AS i ON i.ID_tblCatalogItem = c.FK_tblCatalogs_tblCatalogItems 
        WHERE c.period = ? and c.code LIKE ?
        GROUP by i.name
        ORDER BY i."rank" DESC;
    """,

    "count_quotes_period_code": """
        SELECT COUNT(*) AS count FROM tblQuotes WHERE period = ? and code LIKE ?;
    """,

}