# Generated by Django 4.1.2 on 2022-12-30 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='sale',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
