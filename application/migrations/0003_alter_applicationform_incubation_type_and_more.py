# Generated by Django 4.0 on 2021-12-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_applicationform_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='incubation_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/application'),
        ),
    ]
