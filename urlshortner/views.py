from django.shortcuts import render, redirect
import uuid
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(request):
    return render(request, "index.html")


def create(request):
    if request.method == "POST":

        link = request.POST.get("link")
        linkId = str(uuid.uuid4())[:5]
        newLink = Url(link=link, linkId=linkId)
        newLink.save()
        return HttpResponse(linkId)


def go(request, pk):
    try:
        newLink = Url.objects.get(linkId=pk)
        if "https://" in newLink.link.lower():
            return redirect(newLink.link)
        if "http://" in newLink.link.lower():
            return redirect(newLink.link)

        return redirect("http://"+newLink.link)
    except:
        return HttpResponse("Worng url")
