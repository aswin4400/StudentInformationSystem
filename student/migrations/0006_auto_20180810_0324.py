# Generated by Django 2.0.5 on 2018-08-10 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20180810_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_code',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_code',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.ManyToManyField(to='student.Batch'),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.ManyToManyField(to='student.Branch'),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.ManyToManyField(to='student.Semester'),
        ),
    ]
