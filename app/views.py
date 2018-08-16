from django.shortcuts import render
from django.http import HttpResponse
from app.models import Picture

# Create your views here.
def index(request):
    images = Picture.objects.all().order_by('-id')[:20]
    return render(request, "index.html", {'images':images})

def getimg(request,page):
    pagenumber = ((int(page)-1)*20)+1
    images = Picture.objects.all().order_by('-id')[pagenumber:int(page)*20]
    img={'title':'','filename':''}
    json_text=""
    for image in images:
        img['filename'] = image.filename
        img['title'] = image.title
        json_text += str(img).replace("'",'"')+","
    jsondata = '{"data":[%s]}' % json_text[:-1]
    return HttpResponse(str(jsondata))