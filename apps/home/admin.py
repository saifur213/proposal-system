# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Proposal

# Register your models here.
@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('Proposal_Id', 'Category', 'Title', 'Budget', 'Status')