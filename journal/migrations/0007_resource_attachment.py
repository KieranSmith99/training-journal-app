# Generated by Django 4.0.3 on 2022-03-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_alter_resource_database_alter_resource_framework_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='attachment',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]