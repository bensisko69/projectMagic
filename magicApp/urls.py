from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('import', views.importCard, name='importCard'),
]