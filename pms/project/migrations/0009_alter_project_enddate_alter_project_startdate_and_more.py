# Generated by Django 5.0.2 on 2024-03-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_delete_assigntask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='endDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='startDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='projectmodule',
            name='startDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
