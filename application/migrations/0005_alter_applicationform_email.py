# Generated by Django 4.0 on 2021-12-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_applicationform_incubation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]