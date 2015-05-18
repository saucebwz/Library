from django.conf.urls import include, url
from django.contrib import admin
from YoutubeLibrary import views
urlpatterns = [
    # Examples:
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^category/get/$', views.GetCategories.as_view(), name='category_get_view')
    # url(r'^blog/', include('blog.urls')),

]
