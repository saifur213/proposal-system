# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('proposals/', views.ViewProposals, name='proposals'),
    path('createproposals/', views.CreateProposals, name='createproposals'),
    path('proposaldetailsview/', views.ViewProposalDetails, name='proposaldetailsview'),
    path('proposaldetailsview2/', views.ViewProposalDetails2, name='proposaldetailsview2'),
    path('generateproposal1/', views.GenerateProposal1, name='generateproposal1'),
    path('generateproposal2/', views.GenerateProposal2, name='generateproposal2'),
    path('updateproposal/', views.UpdateProposal, name='updateproposal'),
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
