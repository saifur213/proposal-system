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
    path('addproposal/', views.AddProposal, name='addproposal'),
    path('proposaldetailsview/<int:proposal_id>/', views.ViewProposalDetails, name='proposaldetailsview'),
    # path('proposaldetailsview2/', views.ViewProposalDetails2, name='proposaldetailsview2'),
    # path('proposaldetailsview3/', views.ViewProposalDetails3, name='proposaldetailsview3'),
    path('generateproposal1/<int:proposal_id>/', views.GenerateProposal1, name='generateproposal1'),
    # path('generateproposal2/', views.GenerateProposal2, name='generateproposal2'),
    # path('generateproposal3/', views.GenerateProposal3, name='generateproposal3'),
    path('updateproposal/', views.UpdateProposal, name='updateproposal'),
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
