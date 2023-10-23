SELECT q.ID_tblQuote, q.code, q.description, c.code, c.description, c.FK_tblCatalogs_tblCatalogItems, i.name  FROM tblQuotes AS q
LEFT JOIN tblCatalogs AS c ON c.ID_tblCatalog = q.FK_tblQuotes_tblCatalogs
LEFT JOIN tblCatalogItems AS i ON i.ID_tblCatalogItem = c.FK_tblCatalogs_tblCatalogItems
WHERE c.ID_tblCatalog = 158  and c.period = 68;


-- SELECT q.ID_tblQuote, q.period, q.code, q.description, q.measure, q.statistics FROM tblQuotes AS q
-- WHERE q.FK_tblQuotes_tblCatalogs = 158;

SELECT * FROM tblQuotes WHERE FK_tblQuotes_tblCatalogs = 158;