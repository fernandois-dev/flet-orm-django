
import django
from django.core.management import call_command
import settings  # Importa la configuración
from django.conf import settings
import os


django.setup()

# Generar y aplicar migraciones
call_command("makemigrations", "inventory")
call_command("migrate")