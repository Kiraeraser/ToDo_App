# Generated by Django 2.2.1 on 2019-06-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_content',
            field=models.TextField(blank=True),
        ),
    ]