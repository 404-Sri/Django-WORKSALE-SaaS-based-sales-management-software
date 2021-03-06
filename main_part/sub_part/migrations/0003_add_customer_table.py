# Generated by Django 4.0.1 on 2022-02-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_contact_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_customer_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
            ],
        ),
    ]
