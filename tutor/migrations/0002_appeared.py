# Generated by Django 3.0.3 on 2020-04-11 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeared',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tutor.Heading')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
