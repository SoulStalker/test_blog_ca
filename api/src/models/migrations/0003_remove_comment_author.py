# Generated by Django 5.1.1 on 2024-09-16 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
