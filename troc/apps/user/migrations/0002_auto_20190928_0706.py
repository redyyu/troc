# Generated by Django 2.2.5 on 2019-09-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wxappuser',
            name='unionid',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
