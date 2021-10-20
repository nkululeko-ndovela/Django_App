# Generated by Django 3.2.8 on 2021-10-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Name', models.CharField(max_length=50, unique=True)),
                ('Upload_by', models.TextField()),
                ('dated', models.DateField(auto_now_add=True)),
            ],
        ),
    ]