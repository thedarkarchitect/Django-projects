# Generated by Django 4.1.7 on 2023-02-21 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='into',
            new_name='intro',
        ),
    ]
