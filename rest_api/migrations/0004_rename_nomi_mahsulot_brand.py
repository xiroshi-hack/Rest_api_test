# Generated by Django 4.1.1 on 2022-10-03 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_mahsulot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mahsulot',
            old_name='nomi',
            new_name='brand',
        ),
    ]
