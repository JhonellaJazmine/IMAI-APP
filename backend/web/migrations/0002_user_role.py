# Generated by Django 4.2.6 on 2023-11-10 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('superuser', 'Superuser'), ('branch_admin', 'Branch Admin'), ('branch_personnel', 'Branch Personnel')], default='branch_personnel', max_length=30),
        ),
    ]
