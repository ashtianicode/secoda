from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.decorators import action,api_view

from dbmeta.utils.db_meta_data import DBMetaData 



# @api_view(["GET"])
def get_pg_meta_data(request):
    """
    Get the database conn string in parameter
    Extract metadata of all tables
    Return as Json
    """

    db_meta_tools = DBMetaData(database="secoda")
    pg_meta_data = db_meta_tools.extract_meta_data()
    print(pg_meta_data)


    return JsonResponse(pg_meta_data, safe=False) 