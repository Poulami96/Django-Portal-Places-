# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import Http404

#from django.http import HttpResponse
#from django.template import loader(for template)

from .models import State

def index(request):
	all_states=State.objects.all()
	#If templates were not there
	#html= ''
	#for state in all_states:
		#url= '/Country' + str(state.id) + '/'
		#html += '<a href="' + url +'">' + state.state_name + '</a><br>'
	#template=loader.get_template('Country/index.html')
	#context={'all_states': all_states}

	#return HttpResponse(html)
	#return HttpResponse(template.render(context,request))(for templates)
	return render(request,'Country/index.html',{'all_states': all_states})

#def detail(request,state_id):
#	return HttpResponse("detail for state:" + str(state_id))


def detail(request,state_id):
	try:
		state=State.objects.get(pk=state_id)
	except State.DoesNotExist:
		raise Http404("State does not exist")
	return render(request,'Country/detail.html',{'state': state})
