from django.shortcuts import render, redirect
from shortner.models import *
from django.http import HttpResponse
# Create your views here.


def createUrl(req):
    if req.method == "POST":
        long_url = req.POST.get("link")
        obj = Url.create(long_url)
        return render(req, "shortner/index.html", {
            "long_url": obj.long_url,
            "short_url": req.get_host() + '/' + obj.short_url
        })
    return render(req, "shortner/index.html")


def routeUrl(req, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.long_url)
    except:
        return redirect(createUrl)
