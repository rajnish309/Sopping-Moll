# Generated by Django 4.2.3 on 2024-03-17 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=26)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('desc', models.TextField(max_length=200)),
            ],
        ),
    ]
