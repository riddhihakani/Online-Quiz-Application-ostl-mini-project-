# Generated by Django 3.0.3 on 2020-04-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0006_heading_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading',
            name='difficultylevel',
            field=models.CharField(choices=[('Beginner', 'BEGINNER'), ('Easy', 'EASY'), ('Medium', 'MEDIUM'), ('Hard', 'HARD')], max_length=12, verbose_name='Difficulty Level'),
        ),
    ]