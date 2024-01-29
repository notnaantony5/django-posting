from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Переопределенная модель пользователя
    """
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
