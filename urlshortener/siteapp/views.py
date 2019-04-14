from django.shortcuts import render, render_to_response, get_object_or_404
import random, string, json, requests
from .models import Urls
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest


# Create your views here.
def home(request):
    return render(request, 'siteapp/index.html')


def redirect_url(request):
    url = get_object_or_404(Urls, pk=request.path.strip("/"))
    return HttpResponseRedirect(url.long_url)

def handler404(request):
    return render(request, 'siteapp/404.html', status=404)

def handler500(request):
    return render(request, 'siteapp/500.html', status=500)

def new_url(request):
    if request.POST:
        url = request.POST['shorturl']
        length = 6
        char = string.ascii_uppercase + string.digits + string.ascii_lowercase
        short_id = ''
        while True:
            short_id = ''.join(random.choice(char) for x in range(length))
            try:
                temp = Urls.objects.get(pk=short_id)
            except:
                break
        saveurl = Urls(long_url=url, short_id=short_id)
        saveurl.save()
        return render(request, 'siteapp/index.html', {'msg': short_id})

    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")
