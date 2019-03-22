from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from Post.views import all_posts
from Post.views import  post


urlpatterns = [
    path('admin/', admin.site.urls),
    path(' ',include('Quap.urls',namespace='GP')),
    path('',all_posts),
    path('',post),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

