# Generated by Django 3.1.5 on 2021-01-18 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_manage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='name',
            new_name='employee_name',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='name',
            new_name='job_name',
        ),
        migrations.RemoveField(
            model_name='joballocation',
            name='jobs',
        ),
        migrations.AddField(
            model_name='joballocation',
            name='job_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job_manage.jobs'),
        ),
    ]
