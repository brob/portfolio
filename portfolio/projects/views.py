from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.template import RequestContext
from projects.models import Project


def home(request):
	try:
		featuredProject = Project.objects.filter(featured=True)
	except Project.DoesNotExist:
		featuredProject = ''

	return render_to_response("home.html", {
		'projects': featuredProject
	}, context_instance=RequestContext(request))
	
	
	
def projectList(request):
	featuredProject = Project.objects.filter(featured=True)
	regularProject = Project.objects.all()
	return render_to_response("projects/project_list.html", {
		'featured': featuredProject,
		'projects': regularProject,
		
	
	}, context_instance=RequestContext(request))
	
def projectDetail(request, slug):
	slugValue = slug
	project = get_object_or_404(Project, slug=slugValue)
	return render_to_response("projects/project_detail.html", {
		'project': project
	
	}, context_instance=RequestContext(request))