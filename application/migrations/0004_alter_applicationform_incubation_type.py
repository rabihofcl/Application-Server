# Generated by Django 4.0 on 2021-12-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_applicationform_incubation_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='incubation_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
