from django import forms
from .models import Photo, Upload


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

    
class UploadForm(forms.ModelForm):

    class Meta: 

        model = Upload
        fields = []

    





    