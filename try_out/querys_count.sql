SELECT  ID_tblCatalog, period, code, item.name AS item, item."rank" AS "rank" , description, raw_parent, ID_parent,  FK_tblCatalogs_tblCatalogItems
FROM tblCatalogs 
LEFT JOIN tblCatalogItems AS item ON item.ID_tblCatalogItem = FK_tblCatalogs_tblCatalogItems
WHERE id_parent <> ID_tblCatalog and id_parent = 2
ORDER BY "rank"

SELECT  count(code) FROM tblCatalogs 

SELECT *, COUNT(*) AS count FROM tblCatalogs GROUP BY FK_tblCatalogs_tblCatalogItems ;

SELECT COUNT(tc.code), * FROM tblCatalogItems ci
left join tblCatalogs tc on	tc.FK_tblCatalogs_tblCatalogItems = ci.ID_tblCatalogItem   
GROUP by ci.name 

SELECT COUNT(tc.code), ID_tblCatalog, period, code, description, tci.name AS item FROM tblCatalogs tc 
LEFT JOIN tblCatalogItems tci ON tci.ID_tblCatalogItem = tc.FK_tblCatalogs_tblCatalogItems 
WHERE id_parent <> ID_tblCatalog and id_parent = 2
GROUP by tci.name


SELECT ID_tblCatalog, period, code, description, tci.name AS item 
FROM tblCatalogs tc 
LEFT JOIN tblCatalogItems tci ON tci.ID_tblCatalogItem = tc.FK_tblCatalogs_tblCatalogItems 
WHERE tci.name = 'глава' and tc.code = 6 and tc.period = 68

---1
SELECT ID_tblCatalog, period, code, description, tci.name AS item, COUNT(*) AS count
FROM tblCatalogs tc 
LEFT JOIN tblCatalogItems tci ON tci.ID_tblCatalogItem = tc.FK_tblCatalogs_tblCatalogItems 
WHERE tc.period = 68 and tc.code LIKE '6.%'
GROUP by tci.name
ORDER BY tci."rank" DESC 

---2 tci.name = 'таблица' and 

SELECT ID_tblCatalog, period, code, description, tci.name AS item, COUNT(tc.code) 
FROM tblCatalogs tc 
LEFT JOIN tblCatalogItems tci ON tci.ID_tblCatalogItem = tc.FK_tblCatalogs_tblCatalogItems 
WHERE tc.id_parent <> tc.ID_tblCatalog and tc.id_parent = 2
GROUP by tci.name  

--3

SELECT ID_tblCatalog, period, code, description, tci.name AS item 
FROM tblCatalogs tc 
LEFT JOIN tblCatalogItems tci ON tci.ID_tblCatalogItem = tc.FK_tblCatalogs_tblCatalogItems 
WHERE tci.name = 'сборник' and tc.period = 68 and tc.code LIKE '6.%'


SELECT period, i.name AS item, COUNT(*) AS count
        FROM tblCatalogs AS c 
        LEFT JOIN tblCatalogItems AS i ON i.ID_tblCatalogItem = c.FK_tblCatalogs_tblCatalogItems 
        WHERE c.period = 68 and c.code LIKE '6.%'
        GROUP by i.name
        ORDER BY i."rank" DESC 



SELECT cc.ID_tblCatalog, cc.code, ii.name
FROM tblCatalogs cc
LEFT JOIN tblCatalogItems ii ON ii.ID_tblCatalogItem = cc.FK_tblCatalogs_tblCatalogItems
WHERE ii.name = 'таблица' AND cc.ID_parent IN
(SELECT ID_tblCatalog
FROM tblCatalogs c LEFT JOIN tblCatalogItems i ON i.ID_tblCatalogItem = c.FK_tblCatalogs_tblCatalogItems WHERE i.name = 'сборник')



