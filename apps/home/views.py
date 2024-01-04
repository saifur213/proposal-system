# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect, get_object_or_404

from .services.gpt_driver import gpt_driver

from .models import Proposal,ProposalField



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
        proposals = Proposal.objects.all()
        return render(request, 'home/view-proposals.html', {'proposals': proposals})
def CreateProposals(request):
        return render(request, 'home/create-proposal.html')
def AddProposal(request):
        if request.method == 'POST':
                category = request.POST.get('category')
                title = request.POST.get('title')
                budget = request.POST.get('budget')
                status = request.POST.get('status')

                proposal = Proposal(Category=category,Title=title, Budget=budget, Status=status)
                proposal.save()
                return render(request, 'home/create-proposal.html')
        
        
def ViewProposalDetails(request, proposal_id):
        proposal = get_object_or_404(Proposal, Proposal_Id=proposal_id)
        return render(request, 'home/proposal-details-1.html',{'proposal': proposal})
# def ViewProposalDetails2(request):
#         return render(request, 'home/proposal-details-2.html')
# def ViewProposalDetails3(request):
#         return render(request, 'home/proposal-details-3.html')
def UpdateProposal(request):
        return render(request, 'home/update-proposal.html')
def GenerateProposal1(request, proposal_id):
        if request.method == 'POST':
                proposal_instance = get_object_or_404(Proposal, Proposal_Id=proposal_id)
                topic = request.POST.get('topic')
                member1 = request.POST.get('member_1_name')
                member2 = request.POST.get('member_2_name')
                member3 = request.POST.get('member_3_name')

                proposal_field = ProposalField(Proposal_Id=proposal_instance,Topic=topic, Member1=member1, Member2=member2, Member3=member3)
                proposal_field.save()
        text = gpt_driver()
        print(text)
        context = {
        'generated_text': text,
        }
        return render(request, 'home/generate-proposal-template-1.html', context)
# def GenerateProposal2(request):
#         return render(request, 'home/generate-proposal-template-2.html')
# def GenerateProposal3(request):
#         text = gpt_driver()
#         print(text)
#         context = {
#         'generated_text': text,
#         }
#         return render(request, 'home/generate-proposal-template-3.html',context)
