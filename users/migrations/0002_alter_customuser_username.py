# Generated by Django 5.1.3 on 2024-11-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
