from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def generate_url_outer():
    # generated = []
    counter = 0
    def inner():
        nonlocal counter
        counter += 1
        return str(counter)
    return inner
generate_url = generate_url_outer()
urls = {}

@csrf_exempt
def shorter(request):
    global urls
    url = json.loads(request.body.decode('utf-8'))['full_url']
    short_url = generate_url()
    urls[short_url] = url
    return JsonResponse({'short_url': short_url})
@csrf_exempt
def redirect_user(request, key):
    if key in urls:
        return redirect(urls[key])
    
