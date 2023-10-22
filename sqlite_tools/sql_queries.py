sql_selects = {

    "select_name_catalog_items":    """SELECT ID_tblCatalogItem FROM tblCatalogItems WHERE name IS ?;""",
    "select_all_catalog_items":     """SELECT * FROM tblCatalogItems;""",
    "select_root_catalog_items":    """SELECT * FROM tblCatalogItems WHERE ID_tblCatalogItem = parent_item;""",

    "select_quotes_all":    """SELECT * FROM tblQuotes;""",


    "select_period_code_catalog":   """SELECT ID_tblCatalog FROM tblCatalogs WHERE period = ? and code = ?;""",
    "select_period_catalog":        """SELECT * FROM tblCatalogs WHERE period IS ?;""",
    "select_code_period_item_catalog":   """
            SELECT ID_tblCatalog, period, code, item.name, description 
            FROM tblCatalogs 
            LEFT JOIN tblCatalogItems AS item ON item.ID_tblCatalogItem = FK_tblCatalogs_tblCatalogItems
            WHERE code = ? AND item.name = ? AND period = ?;
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

}