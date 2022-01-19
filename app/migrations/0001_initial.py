# Generated by Django 3.2.6 on 2022-01-18 19:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigIntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('type', models.TextField(db_column='type')),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), db_column='data', size=None)),
                ('date', models.DateTimeField(db_column='date')),
            ],
            options={
                'db_table': 'dashboards',
                'managed': True,
            },
        ),
    ]