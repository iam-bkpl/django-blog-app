# Generated by Django 3.2 on 2021-04-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='views',
            field=models.IntegerField(default=True),
        ),
    ]