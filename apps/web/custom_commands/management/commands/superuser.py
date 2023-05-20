from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from decouple import config

User = get_user_model()

DJANGO_SUPERUSER_PASSWORD = config('DJANGO_SUPERUSER_PASSWORD', cast=str)
DJANGO_SUPERUSER_USERNAME = config('DJANGO_SUPERUSER_USERNAME', cast=str)
DJANGO_SUPERUSER_EMAIL = config('DJANGO_SUPERUSER_EMAIL', cast=str)

class Command(BaseCommand):
    help = 'Creates a superuser'

    def handle(self, *args, **options):
        try:
            user = User(
                email=DJANGO_SUPERUSER_EMAIL,
                username=DJANGO_SUPERUSER_USERNAME,
            )
            user.set_password(DJANGO_SUPERUSER_PASSWORD)
            user.is_superuser = True
            user.is_staff = True
            user.is_admin = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        except Exception as e:
            raise CommandError(e)