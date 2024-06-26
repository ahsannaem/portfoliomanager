# Generated by Django 5.0.6 on 2024-06-01 13:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_alter_portfolio_name_alter_portfolio_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='name',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='total_investment',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
