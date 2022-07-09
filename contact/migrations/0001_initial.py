# Generated by Django 3.2 on 2021-04-30 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=13)),
                ('phonePerson', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('emailPerson', models.TextField()),
                ('location', models.TextField(blank=True)),
                ('map', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
