# Generated by Django 4.0.3 on 2022-10-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_room', models.CharField(max_length=255, verbose_name='Кол-во комнат')),
            ],
        ),
    ]
