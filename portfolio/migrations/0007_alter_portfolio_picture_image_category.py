# Generated by Django 4.1 on 2022-12-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0006_alter_portfolio_picture_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio_picture",
            name="image_category",
            field=models.CharField(
                choices=[
                    ("city", "City"),
                    ("nature", "Nature"),
                    ("panorama", "Panorama"),
                    ("long_exposure", "Long Exposure"),
                ],
                max_length=19,
            ),
        ),
    ]