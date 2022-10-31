from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from dbmeta.utils.db_meta_data import DBMetaData 



# @api_view(["POST"])

@csrf_exempt
def get_pg_meta_data(request):
    """
    Get the database conn string in body of POST request
    Extract metadata of all tables
    Return as JSON
    """
    if request.method != "POST":
        return HttpResponse('please POST a payload with this format: { "db_conn_string" : "postgresql+psycopg2://postgres:postgres@localhost/secoda" } ')


    default_conn_string = "default_conn_string_will_raise_error"
    db_conn_string = json.loads(request.body).get('db_conn_string',default_conn_string)


    # Try connecting to DB
    db_meta_tools = DBMetaData()
    connection_status, log = db_meta_tools.connect_to_db(db_conn_string= db_conn_string)
    
    # Extract meta data if successful connection
    if connection_status == "successful_connection":
        pg_meta_data = db_meta_tools.extract_meta_data()
        return JsonResponse(pg_meta_data, safe=False) 

    elif connection_status == "connection_failure":
        return HttpResponse("connection_failure - error: " + log)

    