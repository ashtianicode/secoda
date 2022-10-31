import json 
from sqlalchemy import create_engine


class DBMetaData():
    def __init__(self,):
       pass

    
    def connect_to_db(self,db_conn_string):
        try:
            self.database = db_conn_string.split("/")[-1]
            self.engine = create_engine(db_conn_string)
            return "successful_connection", "no logs"
        except Exception as e:
            print(e)
            return "connection_failure" , str(e)


    def exectute_query(self,q):
        results = self.engine.execute(q, ('BADGES_SFR',))
        return results.fetchall()

    def get_tables(self):
        q = "select * from information_schema.tables"
        results = self.exectute_query(q)   
        tables_list =  [ table[2] for table in  results]
        return tables_list

    def get_schema_list(self,table):
        """
        Example Output 
        [('column_a', 'integer', 'YES'),
        ('column_b', 'boolean', 'NO'),
        ...,
        ]
        """
        
        q = f"""                              
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = '{table}';
        """
        result = self.exectute_query(q)        
        return result


    def get_num_rows(self,table):
        q = "select count(*) from public.backtests"
        result = self.exectute_query(q)
        print(result)
        row_count = int(result[0][0]) if len(result) > 0 else None
        return row_count


    def extract_meta_data(self):
        table_meta_data_list = []
    
        tables = self.get_tables()
        for table in tables:
            
            ## create the columns and schema meta data for the table
            schema_meta_data_list = []
            column_meta_data_list = []
        
            columns_schema_list = self.get_schema_list(table)
            for column in columns_schema_list:
                column_name =     column[0]
                column_type =     column[1]
                column_nullable = column[2]

                schema_meta_data = {
                    "col_name": column_name,
                    "col_type": column_type,
                    "col_nullable": column_nullable
                }
                schema_meta_data_list.append(schema_meta_data)

            column_meta_data_list = [ {"col_name": col["col_name"], "col_type": col["col_type"]} for col in schema_meta_data_list]
            schema_meta_data_string = json.dumps(schema_meta_data_list)

            
            ## get number of rows
            num_rows = self.get_num_rows(table)
            
            ## create table metadata
            table_meta_data = {
                "columns": column_meta_data_list,
                "num_rows": num_rows,
                "schema": schema_meta_data_string,
                "database": self.database,
             }

            table_meta_data_list.append(table_meta_data)

        return table_meta_data_list 
        






