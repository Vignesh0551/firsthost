# Generated by Django 4.2.2 on 2023-06-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(default=0, upload_to='picture'),
            preserve_default=False,
        ),
    ]
