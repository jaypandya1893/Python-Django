# Generated by Django 4.1.7 on 2023-03-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('orderdate', models.DateField()),
                ('phoneno', models.PositiveIntegerField()),
                ('paymenttype', models.PositiveIntegerField()),
                ('tax', models.PositiveIntegerField()),
            ],
        ),
    ]
