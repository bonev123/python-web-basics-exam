from django.urls import path

from exam_2022.main.views import show_home, create_album, album_details, edit_album, delete_album, profile_details, \
    delete_profile, create_profile

urlpatterns = [
    path('', show_home, name='index'),

    path('album/add/', create_album, name='create album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),

    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/create/', create_profile, name='create profile'),


]
