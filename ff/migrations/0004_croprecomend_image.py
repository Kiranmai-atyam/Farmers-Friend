# Generated by Django 4.1.1 on 2022-11-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ff', '0003_alter_croprecomend_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='croprecomend',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]