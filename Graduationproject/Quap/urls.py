from django.conf.urls import url,include
from .import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="Quap"
urlpatterns = [
    url(r'^$',views.all_posts,name='all_posts'),
    #url(r'^(?P<id>\d+)$',views.post,name='post'),
url(r'^$',views.post,name='post'),
   # url(r'^admin/',admin.site.urls),
    #url(r'^all_posts/',include('Quap.urls')),
   # url(r'^about/$',views.about),
    #url(r'^$',views.all_posts),

]
urlpatterns+=staticfiles_urlpatterns()

