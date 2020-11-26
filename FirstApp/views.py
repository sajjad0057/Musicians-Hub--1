from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Musician, Album
from FirstApp import forms
from django.db.models import Avg

# Create your views here.

def index(request):
    musician_list=Musician.objects.order_by('first_name')
    dict={'title':"Home Page",'musician_list':musician_list}
    return render(request,'FirstApp/index.html',context=dict)

def album_list(request,pk):
    artist_info = Musician.objects.get(pk=pk)
    album_info = Album.objects.filter(artist_id=pk).order_by('name')
    artist_rating = Album.objects.filter(artist_id=pk).aggregate(Avg('num_stars'))
    dict={'title':'List of Album','artist_info':artist_info,'album_info':album_info,'artist_rating':artist_rating}
    return render(request,'FirstApp/album_list.html',context=dict)

def musician_form(request):
    form=forms.MusicianForm()
    if request.method == 'POST':
        form=forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    dict={'title':'Add Musician','form':form}
    return render(request,'FirstApp/musician_form.html',context=dict)

def album_form(request):
    form = forms.AlbumForm()
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    dict={'title':'Add Album','form':form}
    return render(request,'FirstApp/album_form.html',context=dict)

def edit_artist(request,pk):
    artist_info = Musician.objects.get(pk=pk)
    form = forms.MusicianForm(instance=artist_info)
    if request.method  == 'POST':
        form = forms.MusicianForm(request.POST,instance=artist_info)
        if form.is_valid():
            form.save()
            return album_list(request,pk)

    dict={'form':form,'artist_info':artist_info}
    return render(request,'FirstApp/edit_artist.html',context=dict)

def edit_album(request,pk):
    album_info = Album.objects.get(pk=pk)
    form = forms.AlbumForm(instance=album_info)
    dict={'title':'Edit Album','form':form,'album_info':album_info}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST,instance=album_info)
        if form.is_valid():
            form.save()
            dict.update({'success':'Album is Updated Successfully !'})
    return render(request,'FirstApp/edit_album.html',context=dict)


def delete_album(request,pk):
    album = Album.objects.get(pk=pk).delete()
    dict={'title':'Delete Album','delete':'Album is deleted Successfully !'}
    return render(request,'FirstApp/edit_album.html',context=dict)

def delete_artist(request,pk):
    artist = Musician.objects.get(pk=pk).delete()
    dict = {'title':'Delete Artist','delete':'Album is deleted Successfully !'}
    return render(request,'FirstApp/edit_artist.html',context=dict)
