# Generated by Django 4.1.4 on 2023-05-04 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_korzina_remove_userphoto_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='korzina',
            old_name='id_userdata',
            new_name='user',
        ),
    ]