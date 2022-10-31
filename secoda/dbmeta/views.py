from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.decorators import action,api_view
from django.views.decorators.csrf import csrf_exempt


from dbmeta.utils.db_meta_data import DBMetaData 



# @api_view(["GET"])

@csrf_exempt
def get_pg_meta_data(request):
    """
    Get the database conn string in parameter
    Extract metadata of all tables
    Return as JSON
    """
    default_conn_string = 'postgresql+psycopg2://postgres:postgres@localhost/secoda'
    db_conn_string = request.POST.get('db_conn_string', default_conn_string)

    print(default_conn_string)
    db_meta_tools = DBMetaData(db_conn_string= db_conn_string )
    pg_meta_data = db_meta_tools.extract_meta_data()
    print(pg_meta_data)


    return JsonResponse(pg_meta_data, safe=False) 