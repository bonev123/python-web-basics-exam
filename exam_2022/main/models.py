from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


from exam_2022.main.validators import validate_desired_chars


class Profile(models.Model):

    CHAR_MIN_LEN = 2
    CHAR_MAX_LEN = 15

    username = models.CharField(
        max_length=CHAR_MAX_LEN,
        validators=(MinLengthValidator(CHAR_MIN_LEN),
                    validate_desired_chars,
        )
    )
    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(0),
        )
    )

class Album(models.Model):

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip-Hop Music'
    OTHER = 'Other'
    GENRES = [(x, x) for x in (POP_MUSIC, JAZZ_MUSIC, RNB_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)]
    ALBUM_MAX_LEN = 30


    album_name = models.CharField(
        unique=True,
        max_length=ALBUM_MAX_LEN,
    )
    artist = models.CharField(
        max_length=ALBUM_MAX_LEN,
    )

    genre = models.CharField(
        max_length=ALBUM_MAX_LEN,
        choices=GENRES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )

