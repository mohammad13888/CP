# Generated by Django 4.1 on 2023-03-10 17:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("private", "0002_pv_member"),
    ]

    operations = [
        migrations.AddField(
            model_name="pv_member",
            name="others_rooms",
            field=models.ManyToManyField(
                blank=True, related_name="pvrs", to="private.pv_room"
            ),
        ),
        migrations.AlterField(
            model_name="pv_member",
            name="others",
            field=models.ManyToManyField(
                blank=True, related_name="pvs", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
