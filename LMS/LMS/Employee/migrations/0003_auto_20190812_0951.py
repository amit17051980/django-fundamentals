# Generated by Django 2.2.4 on 2019-08-12 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_employee_lm_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emp_id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='lm_id',
            new_name='_lm_id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emp_name',
            new_name='_name',
        ),
    ]
