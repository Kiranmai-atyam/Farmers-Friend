# Generated by Django 4.1.1 on 2022-10-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='croprec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil', models.CharField(max_length=30)),
                ('season', models.CharField(max_length=20)),
               
            ],
        ),
    ]
