# Postgres meta data rest API


First `docker-compose up` for the Postgres database, which is going to populate from the `populate_pg.sql` file.
For the django app, move under secoda subdir where manage.py is located and `python3 manage.py runserver`.


Call the /dbmeta endpoint, posting the connection string for the Postgres DB.

```
curl --location --request POST 'http://127.0.0.1:8000/dbmeta/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "db_conn_string" : "postgresql+psycopg2://postgres:postgres@localhost/secoda"
}'
```



Format of the return JSON payload follows this data structure:

```python

table_meta_data = {
    "columns": [schema_meta_data = { "col_name": column_name, "col_type": column_type} ],
    "num_rows": num_rows,
    "schema": schema_meta_data_string,
    "database": self.database,
}

```

Here's a sample of the return pyaload:
```json
 {
        "columns": [
            {
                "col_name": "wins",
                "col_type": "integer"
            },
            {
                "col_name": "draws",
                "col_type": "integer"
            },
            {
                "col_name": "losses",
                "col_type": "integer"
            },
            {
                "col_name": "mean_profits",
                "col_type": "double precision"
            },
            {
                "col_name": "trades_count",
                "col_type": "integer"
            },
            {
                "col_name": "total_profits",
                "col_type": "double precision"
            },
            {
                "col_name": "pnl",
                "col_type": "text"
            },
            {
                "col_name": "strategy",
                "col_type": "character varying"
            },
            {
                "col_name": "asset_id",
                "col_type": "character varying"
            },
            {
                "col_name": "timeframe",
                "col_type": "character varying"
            },
            {
                "col_name": "pair",
                "col_type": "character varying"
            },
            {
                "col_name": "state",
                "col_type": "character varying"
            },
            {
                "col_name": "duration_avg",
                "col_type": "character varying"
            },
            {
                "col_name": "stats",
                "col_type": "text"
            }
        ],
        "num_rows": 0,
        "schema": "[{\"col_name\": \"wins\", \"col_type\": \"integer\", \"col_nullable\": \"YES\"}, {\"col_name\": \"draws\", \"col_type\": \"integer\", \"col_nullable\": \"YES\"}, {\"col_name\": \"losses\", \"col_type\": \"integer\", \"col_nullable\": \"YES\"}, {\"col_name\": \"mean_profits\", \"col_type\": \"double precision\", \"col_nullable\": \"YES\"}, {\"col_name\": \"trades_count\", \"col_type\": \"integer\", \"col_nullable\": \"YES\"}, {\"col_name\": \"total_profits\", \"col_type\": \"double precision\", \"col_nullable\": \"YES\"}, {\"col_name\": \"pnl\", \"col_type\": \"text\", \"col_nullable\": \"YES\"}, {\"col_name\": \"strategy\", \"col_type\": \"character varying\", \"col_nullable\": \"NO\"}, {\"col_name\": \"asset_id\", \"col_type\": \"character varying\", \"col_nullable\": \"YES\"}, {\"col_name\": \"timeframe\", \"col_type\": \"character varying\", \"col_nullable\": \"NO\"}, {\"col_name\": \"pair\", \"col_type\": \"character varying\", \"col_nullable\": \"NO\"}, {\"col_name\": \"state\", \"col_type\": \"character varying\", \"col_nullable\": \"YES\"}, {\"col_name\": \"duration_avg\", \"col_type\": \"character varying\", \"col_nullable\": \"YES\"}, {\"col_name\": \"stats\", \"col_type\": \"text\", \"col_nullable\": \"YES\"}]",
        "database": "secoda"
    },
```