# Generated by Django 4.2 on 2023-04-07 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='Acount_Number',
            new_name='Account_Number',
        ),
    ]
