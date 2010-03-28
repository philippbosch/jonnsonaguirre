from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from jonnsonaguirre.works.models import Work

def work_details(request, slug):
    work = get_object_or_404(Work, slug=slug)
    return render_to_response('works/work-details.html', {'work':work}, context_instance=RequestContext(request))
