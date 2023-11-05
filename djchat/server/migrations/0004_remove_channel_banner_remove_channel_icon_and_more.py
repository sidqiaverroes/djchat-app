# Generated by Django 4.2.6 on 2023-11-05 06:29

from django.db import migrations, models
import server.models
import server.validators


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0003_channel_banner_channel_icon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="channel",
            name="banner",
        ),
        migrations.RemoveField(
            model_name="channel",
            name="icon",
        ),
        migrations.AddField(
            model_name="server",
            name="banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=server.models.server_banner_upload_path,
                validators=[server.validators.validate_image_file_extension],
            ),
        ),
        migrations.AddField(
            model_name="server",
            name="icon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=server.models.server_icon_upload_path,
                validators=[
                    server.validators.validate_icon_image_size,
                    server.validators.validate_image_file_extension,
                ],
            ),
        ),
    ]