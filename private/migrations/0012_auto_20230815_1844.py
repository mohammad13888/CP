# Generated by Django 3.2.12 on 2023-08-15 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('private', '0011_remove_pv_member_bio_remove_pv_member_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel_message',
            options={'ordering': ('-date_added',)},
        ),
        migrations.RemoveField(
            model_name='pv_member',
            name='display_name',
        ),
        migrations.AddField(
            model_name='channel_message',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='channel_room',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='channel_message',
            name='file',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='pv_member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]