# Generated by Django 4.1 on 2022-11-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0004_alter_portfolio_picture_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio_picture",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
