# Generated by Django 2.1.3 on 2018-12-22 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20181216_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
    ]
