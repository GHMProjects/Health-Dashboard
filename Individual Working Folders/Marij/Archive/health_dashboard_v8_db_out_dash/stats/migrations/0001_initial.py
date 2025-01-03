# Generated by Django 5.1.2 on 2024-12-28 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManualData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('metric', models.CharField(max_length=100)),
                ('value', models.FloatField()),
            ],
            options={
                'db_table': 'manual',
            },
        ),
        migrations.CreateModel(
            name='UserCalories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('calories', models.FloatField()),
            ],
            options={
                'unique_together': {('user_id', 'date')},
            },
        ),
        migrations.CreateModel(
            name='UserHR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('average_hr', models.FloatField()),
            ],
            options={
                'unique_together': {('user_id', 'date')},
            },
        ),
        migrations.CreateModel(
            name='UserSleep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('sleep_minutes', models.IntegerField()),
            ],
            options={
                'unique_together': {('user_id', 'date')},
            },
        ),
        migrations.CreateModel(
            name='UserSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('steps', models.IntegerField()),
            ],
            options={
                'unique_together': {('user_id', 'date')},
            },
        ),
    ]
