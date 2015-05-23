from django.conf.urls import include, url
from django.contrib import admin
from YoutubeLibrary import views
urlpatterns = [
    # Examples:
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^category/get/$', views.GetCategories.as_view(), name='category_get_view'),
    url(r'^category/videos/$', views.getVideosFromCategory, name='category_get_videos'),
    url(r'^category/add/$', views.addCategory, name='add_category_view'),
    url(r'^video/delete/$', views.deleteVideo, name='delete_video')
    # url(r'^blog/', include('blog.urls')),

]
