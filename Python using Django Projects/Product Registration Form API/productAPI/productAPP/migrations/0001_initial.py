# Generated by Django 4.1.7 on 2023-03-28 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
