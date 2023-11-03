# Generated by Django 4.2.6 on 2023-11-01 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0010_remove_cliente_user_remove_produto_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='user',
        ),
        migrations.AddField(
            model_name='produto',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
