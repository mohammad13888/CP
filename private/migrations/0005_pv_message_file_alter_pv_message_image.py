# Generated by Django 4.1 on 2023-05-31 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("private", "0004_pv_message_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="pv_message",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="pv_message",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
