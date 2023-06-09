from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class JobOffer(models.Model):
    APPLIED = "AP"
    CONTACTED = "CO"
    INTERVIEWED = "IV"
    INTERVIEWED = "IV"
    EVALUATED = "EV"
    JOB_PROPOSISTION = "JP"
    DENIED = "DE"
    ACCEPPTED = "AC"
    REJECTED = "RE"
    APPLICATION_STATUS_CHOICES = [
        (APPLIED, "APPLIED"),
        (CONTACTED, "CONTACTED"),
        (INTERVIEWED, "INTERVIEWED"),
        (EVALUATED, "EVALUATED"),
        (JOB_PROPOSISTION, "JOB_PROPOSISTION"),
        (DENIED, "DENIED"),
        (ACCEPPTED, "ACCEPPTED"),
        (REJECTED, "REJECTED"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posistion = models.CharField(max_length=250, null=True, blank=True)
    company = models.ForeignKey(
        "Company", blank=False, null=False, on_delete=models.CASCADE
    )
    company_personalized_info = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        choices=APPLICATION_STATUS_CHOICES, default=APPLIED, max_length=2
    )
    apply_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    link = models.CharField(max_length=1000, null=False, blank=False)
    salary = models.CharField(
        max_length=100, null=True, blank=True, default="Not specified"
    )
    ai_generated_data = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.posistion} - {self.company} - {self.status} updated: {self.update_date}"


class Company(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=False, null=False)
    general_info = models.TextField(null=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Companies"
