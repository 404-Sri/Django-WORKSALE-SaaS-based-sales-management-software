# Generated by Django 4.0.1 on 2022-01-27 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
