from django.shortcuts import render
from django.shortcuts import render_to_response
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
    print("test")
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
        return render_to_response('index.html', {'videos': videos}, context_instance=RequestContext(request))

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
                return HttpResponse("Already in DB!")
            category_model = Category.objects.get(name=category_name)
            VideoModel.objects.create(title=title, description=description, thumb_url=thumb_url, link=link, category=category_model)
            return HttpResponse("OK!")

class GetCategories(View):
    def post(self, request):
        categories = Category.objects.all()
        return render_to_response('get_categories.html', {'categories': categories},
                                  context_instance=RequestContext(request))