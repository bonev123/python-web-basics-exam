from django import forms
from django.shortcuts import render

from exam_2022.main.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        #image_path = self.instance.image.path
        self.instance.delete()
        Album.objects.all().delete()
        #os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')


class AlbumDetails(forms.ModelForm):
    def get_album(self, request, pk):
        album = Album.objects.get(pk=pk)
        return render(request, "album-details.html", {"album": album})
