# Generated by Django 4.2.6 on 2023-10-20 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='produto1',
            new_name='produto',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='produto2',
        ),
    ]
