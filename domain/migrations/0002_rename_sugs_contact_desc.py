# Generated by Django 4.0.1 on 2022-01-14 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='sugs',
            new_name='desc',
        ),
    ]
