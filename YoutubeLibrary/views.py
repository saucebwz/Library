from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from YoutubeLibrary.models import Category, VideoModel
import requests
import json

YOUTUBE_LINKS = [
    "https://www.googleapis.com/youtube/v3/search?part=snippet&",
    "https://www.googleapis.com/youtube/v3/videos?part=snippet&",
]

def buildUrl(url, key, **arguments):
    result = url
    for k, v in arguments.items():
        op = '&'
        result += k + '=' + v + op
    return result + 'key' + '=' + key





API_KEY = "AIzaSyDIRBEKUBShPlDHeoROErwZBaicb3wwNH8"


# Create your views here.

class HomeView(View):

    def get(self, request):
        videos = VideoModel.objects.all()
        categories = Category.objects.all()
        return render_to_response('index.html', {'videos': videos, 'categories': categories}, context_instance=RequestContext(request))

    def post(self, request):
        req = request.POST.copy()
        if req['isDBAdd'] == 'false':
            link = req['link']
            url = buildUrl(YOUTUBE_LINKS[1], API_KEY, **{'id': link})

            r = requests.get(url)
            data = json.loads(r.text)
            json_result = data["items"][0]['snippet']
            return HttpResponse(json.dumps({'information': json_result}), content_type="application/json")
        else:
            title = req['title']
            description = req['description']
            thumb_url = req['thumb_url']
            category_name = req['category']
            link = req['link']
            if VideoModel.objects.filter(title=title).count() > 0:
                return HttpResponse("false")
            category_model = Category.objects.get(name=category_name)
            video = VideoModel.objects.create(title=title, description=description, thumb_url=thumb_url, link=link, category=category_model)
            return HttpResponse(video.pk)

class GetCategories(View):
    def post(self, request):
        categories = Category.objects.all()
        return render_to_response('get_categories.html', {'categories': categories},
                                  context_instance=RequestContext(request))

def getVideosFromCategory(request):
    if request.method == "POST" and request.is_ajax():
        req = request.POST.copy()
        category = req['category']
        if category == 'All':
            return render_to_response('get_videos.html', {'videos': VideoModel.objects.all()}, context_instance=RequestContext(request))
        videos = VideoModel.objects.filter(category__name=category)
        return render_to_response('get_videos.html', {'videos': videos}, context_instance=RequestContext(request))

def deleteVideo(request):
    if request.method == "POST" and request.is_ajax():
        req = request.POST.copy()
        id = req['id']
        get_object_or_404(VideoModel, pk=id).delete()
        return HttpResponse("OK!")

def addCategory(request):
    req = request.POST.copy()
    category_name = req['category_name']
    if Category.objects.filter(name=category_name):
        return HttpResponse("Already in DB!")
    _c = Category.objects.create(name=category_name)
    return HttpResponse(_c.name)
