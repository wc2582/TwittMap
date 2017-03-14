from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/search/', views.search, name='search')
    url(r'^ajax/update/', views.update, name='update')
]
