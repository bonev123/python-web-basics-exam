from django import forms
from django.shortcuts import render

from exam_2022.main.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Enter age',
                }
            )
        }


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
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter an album name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Enter artist name',
                }
            ),
            'genre': forms.TextInput(
                attrs={
                    'placeholder': 'Enter album genre',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter album description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter album price',
                }
            ),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter an album name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Enter artist name',
                }
            ),
            'genre': forms.TextInput(
                attrs={
                    'placeholder': 'Enter album genre',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter album description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter album price',
                }
            ),
        }


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
