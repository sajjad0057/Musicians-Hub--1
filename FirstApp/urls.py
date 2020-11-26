from django.conf.urls import url
from django.urls import path
from FirstApp import views


app_name='FirstApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_album/', views.album_form, name='album_form'),
    path('add_musician/', views.musician_form, name='musician_form'),
    path('album_list/<pk>/', views.album_list, name='album_list'),
    path('edit_artist/<pk>/', views.edit_artist, name='edit_artist'),
    path('edit_album/<pk>/', views.edit_album, name='edit_album'),
    path('delete_album/<pk>/', views.delete_album, name='delete_album'),
    path('delete_artist/<pk>/', views.delete_artist, name='delete_artist'),


]
