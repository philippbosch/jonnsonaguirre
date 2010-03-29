from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from urllib import urlopen

from jonnsonaguirre.works.models import Work

def work_details(request, slug):
    work = get_object_or_404(Work, slug=slug)
    return render_to_response('works/work-details.html', {'work':work}, context_instance=RequestContext(request))

@cache_page(60*15)
def issuu_documents_json(request):
    url = urlopen('http://api.issuu.com/1_0?action=issuu.documents.list&access=public&apiKey=qmym5codqqfmyygnbke1l5ekesglow8b&format=json&signature=9eafd71e0f0271ccda92300927331bbd')
    return HttpResponse(url.read(), content_type='application/json')