# Generated by Django 4.0.4 on 2022-06-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=50)),
                ('source_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_name', models.CharField(max_length=50)),
                ('dest_code', models.CharField(max_length=50)),
                ('source', models.ManyToManyField(to='main.source')),
            ],
        ),
    ]