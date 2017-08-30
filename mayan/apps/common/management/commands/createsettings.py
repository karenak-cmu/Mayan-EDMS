from __future__ import unicode_literals

import os

from django.conf import settings
from django.core import management
from django.utils.crypto import get_random_string

from ...settings import setting_local_settings_filename

from .literals import SETTING_FILE_TEMPLATE


class Command(management.BaseCommand):
    help = 'Creates a local settings file with a random secret key.'

    @staticmethod
    def _generate_secret_key():
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        return get_random_string(50, chars)

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'settings', '{}.py'.format(setting_local_settings_filename.value))
        if os.path.exists(path):
            self.stdout.write(self.style.NOTICE('Existing settings file at: {0}. Backup, remove this file, and try again.'.format(path)))
        else:
            with open(path, 'w+') as file_object:
                file_object.write(
                    SETTING_FILE_TEMPLATE.format(Command._generate_secret_key())
                )
