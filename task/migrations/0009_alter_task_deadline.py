# Generated by Django 4.1.1 on 2022-12-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]