# Generated by Django 2.0.5 on 2018-08-10 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='student',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='semester',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
