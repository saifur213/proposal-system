# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
def ViewProposals(request):
        return render(request, 'home/view-proposals.html')
def CreateProposals(request):
        return render(request, 'home/create-proposal.html')
def ViewProposalDetails(request):
        return render(request, 'home/proposal-details-1.html')
def ViewProposalDetails2(request):
        return render(request, 'home/proposal-details-2.html')
def UpdateProposal(request):
        return render(request, 'home/update-proposal.html')
def GenerateProposal1(request):
        return render(request, 'home/generate-proposal-template-1.html')
def GenerateProposal2(request):
        return render(request, 'home/generate-proposal-template-2.html')
