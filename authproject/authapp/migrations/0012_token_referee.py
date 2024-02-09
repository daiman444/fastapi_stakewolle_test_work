# Generated by Django 5.0.1 on 2024-02-09 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_remove_token_referee_alter_token_referrer'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='referee',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referee_token', to='authapp.user'),
        ),
    ]
