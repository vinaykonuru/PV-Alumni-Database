# Generated by Django 4.0.5 on 2022-06-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniprof', '0008_alter_alumniprof_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumniprof',
            name='degrees',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
