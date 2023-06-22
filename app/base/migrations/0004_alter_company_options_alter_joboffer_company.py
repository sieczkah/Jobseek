# Generated by Django 4.2.2 on 2023-06-17 18:58

import django.db.models.deletion
from django.db import migrations, models


def map_company_names_to_ids(apps, schema_editor):
    """Mapping existing companies to Company model"""
    JobOffer = apps.get_model("base", "JobOffer")
    Company = apps.get_model("base", "Company")
    for job_offer in JobOffer.objects.all():
        try:
            company = Company.objects.get(name=job_offer.company)
            job_offer.company = company.id
            job_offer.save()
        except Company.DoesNotExist:
            new_company = Company(name=job_offer.company)
            new_company.save()
            job_offer.company = new_company.id
            job_offer.save()


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_company"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name_plural": "Companies"},
        ),
        migrations.RunPython(map_company_names_to_ids),
        migrations.AlterField(
            model_name="joboffer",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="base.company"
            ),
        ),
    ]