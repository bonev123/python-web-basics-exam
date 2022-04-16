from django.core.exceptions import ValidationError


def validate_desired_chars(value):
    for ch in value:
        if not (ch.isalnum() or ch == '_'):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
