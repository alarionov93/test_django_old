import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Person
from django.urls import reverse
# Create your views here.


def index(request):

	return HttpResponse(json.dumps({'a': 'b'}), content_type='application/json')


class PersonsList(generic.ListView):
	model = Person
	template_name = 'persons.html'

	def get_queryset(self, *args, **kwargs):
		qs = super(PersonsList, self).get_queryset(*args, **kwargs)
		qs = qs.filter(age__gte=0)

		return qs


class PersonDetail(generic.DetailView):
	model = Person
	context_object_name = 'person'
	template_name = 'person.html'


class PersonUpdate(generic.UpdateView):
	model = Person
	context_object_name = 'person'
	template_name = 'person_update.html'
	fields = ['name', 'sec_name', 'voice', 'age' ]

	def get_success_url(self):
		return reverse('person', args=(self.object.id))

	
	# def get_queryset(self, request, *args, **kwargs):
	# 	qs = super(PersonsList, self).get_queryset(self.request, *args, **kwargs)
	# 	qs = qs.get(pk=int(self.kwargs['p_id']))

	# 	return qs

	# def dispatch(self, request, *args, **kwargs):
	# 	super(PersonDetail, self).dispatch(request, *args, **kwargs)