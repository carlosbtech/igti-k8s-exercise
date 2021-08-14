-- QUERY 1
SELECT
"sexo",
count("business_key") AS "qtd_por_sexo"
FROM output_ksqldb_stream_customers_json
GROUP BY "sexo"
EMIT CHANGES;

-- QUERY 2

SELECT
"id",
"nome",
"endereco",
"telefone",
"dt_update"
FROM output_ksqldb_stream_customers_json
EMIT CHANGES;