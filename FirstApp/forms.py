from django import forms
from django.core import validators
from FirstApp.models import Musician,Album

#creating form......Each form like as class
class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields ='__all__'

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Album
        fields = '__all__'
