# Generated by Django 4.1.2 on 2022-11-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ceo', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('ctype', models.CharField(max_length=100)),
            ],
        ),
    ]
