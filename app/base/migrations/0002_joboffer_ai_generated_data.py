# Generated by Django 4.2.2 on 2023-06-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="joboffer",
            name="ai_generated_data",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]