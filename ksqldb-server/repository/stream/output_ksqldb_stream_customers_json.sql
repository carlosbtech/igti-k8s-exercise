CREATE OR REPLACE STREAM output_ksqldb_stream_customers_json
WITH (KAFKA_TOPIC='output-ksqldb-stream-customers-json', PARTITIONS=3, VALUE_FORMAT='JSON')
AS
SELECT
AS_VALUE("payload"->"id") as "business_key",
"payload"->"id" as "id",
"payload"->"nome",
"payload"->"sexo",
"payload"->"endereco",
"payload"->"telefone",
"payload"->"dt_update"
FROM ksql_stream_customers_json
EMIT CHANGES;