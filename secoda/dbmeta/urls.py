from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_pg_meta_data, name='get_pg_meta_data'),
]