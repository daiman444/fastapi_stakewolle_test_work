# Generated by Django 5.0.1 on 2024-02-09 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_token_referee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='referee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referee_token', to='authapp.user'),
        ),
    ]
