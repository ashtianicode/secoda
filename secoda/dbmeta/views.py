from django.shortcuts import render
from django.http import HttpResponse


def get_pg_meta_data(request):
    """
    Get the database conn string in parameter
    Extract metadata of all tables
    Return as Json
    """
    return HttpResponse("table meta data")