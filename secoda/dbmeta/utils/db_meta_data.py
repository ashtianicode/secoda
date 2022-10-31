

# TableMetadata = {
# 	columns: List[ColumnMetadata]
# 	num_rows: int
# 	schema: str
# 	database: str
# }

# ColumnMetadata = {
# 	col_name: str
# 	col_type: str
# }


class DBMetaData():
    def __init__(self,database):
        import psycopg2
        self.conn = psycopg2.connect(database='carto', user=..., password=...)


    def exectute_query(self,q):
        cur = self.conn.cursor()
        cur.execute(q, ('BADGES_SFR',)) 
        results = cur.fetchall()
        return results

    def get_tables(self):
        pass


    def get_schema(self,table):
        q = f"""                              
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = {table};
        """
        result = self.exectute_query(q)
        return result


    def get_columns(self,table):
        pass

    def get_num_rows(self,table):
        pass


    def extract_meta_data(self):
        table_meta_data_list = []
    
        tables = self.get_tables()
        for table in tables:
            
            ## create the columns meta data for the table
            column_meta_data_list = []
            columns = self.get_columns(table)
            for column in columns:
                column_meta_data = {
                    "col_name": "str",
                    "col_type": "str"
                }
                column_meta_data_list.append(column_meta_data)


            ## create table metadata
            table_meta_data = {
                "columns": column_meta_data_list,
                "num_rows": 42,
                "schema": "str",
                "database": "str",
             }

            table_meta_data_list.append(table_meta_data)

        return table_meta_data_list 
        
