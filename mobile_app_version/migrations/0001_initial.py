# Generated by Django 3.2.7 on 2021-10-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileAppVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufactor', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('release_notes', models.TextField(blank=True)),
                ('link', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Mobile App Version',
                'verbose_name_plural': 'Mobile App Version',
            },
        ),
        migrations.AddConstraint(
            model_name='mobileappversion',
            constraint=models.UniqueConstraint(fields=('manufactor',), name='unique manufactor'),
        ),
    ]
