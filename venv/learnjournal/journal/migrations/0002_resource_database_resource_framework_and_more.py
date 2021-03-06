# Generated by Django 4.0.3 on 2022-03-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='database',
            field=models.CharField(choices=[('MySQL', 'MySQL'), ('PostgreSQL', 'PostgreSQL'), ('MongoDB', 'MongoDB'), ('SQLite', 'SQLite')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resource',
            name='framework',
            field=models.CharField(choices=[('Flask', 'Flask'), ('Django', 'Flask'), ('Angular', 'Angular'), ('React', 'React'), ('Vue', 'Vue'), ('Spring Boot', 'Spring Boot')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resource',
            name='language',
            field=models.CharField(choices=[('Java', 'JAVA'), ('Python', 'Python'), ('Typescript', 'Typescript'), ('Javascript', 'Javascript'), ('Go', 'Go')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resource',
            name='technology',
            field=models.CharField(choices=[('AWS', 'AWS'), ('Git', 'Git'), ('Azure', 'Azure')], default='', max_length=20),
        ),
    ]
