# Generated by Django 4.1 on 2022-09-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-added_city']},
        ),
        migrations.AddField(
            model_name='city',
            name='added_city',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
