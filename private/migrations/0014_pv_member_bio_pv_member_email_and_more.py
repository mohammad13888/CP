# Generated by Django 4.1.6 on 2023-08-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0013_pv_member_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pv_member',
            name='bio',
            field=models.TextField(blank=True, max_length=1023),
        ),
        migrations.AddField(
            model_name='pv_member',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pv_member',
            name='display_name',
            field=models.CharField(max_length=256),
        ),
    ]