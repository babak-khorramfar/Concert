# Generated by Django 4.2.3 on 2023-07-18 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('LastName', models.CharField(max_length=100, null=True)),
                ('Gender', models.IntegerField(choices=[('Man', 'Man'), ('Woman', 'Woman')], default=1)),
                ('ProfileImage', models.ImageField(null=True, upload_to='profileimages/')),
                ('credit', models.FloatField(default=0.0, verbose_name='Credit')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Profile')),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
    ]
