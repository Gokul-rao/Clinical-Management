# Generated by Django 5.0.6 on 2024-05-23 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalsApp', '0004_alter_mymodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='time',
            field=models.TimeField(max_length=30, null=True),
        ),
    ]