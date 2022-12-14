# Generated by Django 4.1.1 on 2022-12-13 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_task_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['category', 'task_name']},
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, choices=[('WORK', 'Work'), ('SELF-CARE', 'Self-care'), ('CHORES', 'Chores'), ('PET', 'Pets'), ('PLANT', 'Plants')], max_length=50, null=True),
        ),
    ]
