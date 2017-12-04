# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from models import mainpage
# Create your views here.
def index(req):
	if req.method == 'GET':
		iid = req.GET.get('id')
		rep = mainpage.objects.filter(id__exact=iid)
		# print rep[0].url
		return HttpResponse(rep[0].url)