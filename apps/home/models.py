# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proposal(models.Model):
    Proposal_Id = models.AutoField(primary_key=True)
    #Logo = models.ImageField(upload_to='proposal_logos/', null=True, blank=True)
    Category = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Budget = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return f"Proposal {self.Proposal_Id}: {self.Title}"

class ProposalField(models.Model):
    Proposal_Field_ID = models.AutoField(primary_key=True)
    Proposal_Id = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    Topic = models.CharField(max_length=255)
    Member1 = models.CharField(max_length=255)
    Member2 = models.CharField(max_length=255)
    Member3 = models.CharField(max_length=255)

    def __str__(self):
        return self.Topic