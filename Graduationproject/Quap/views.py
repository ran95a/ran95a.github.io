from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import Post
#def p1(request):

  #  return render(request,'all_posts.html', {})

'''class HomePageViews(TemplateView):
    template_name = 'HT.hrml'''

def homeView(request):
    print(request.GET)
    return render ( request , "all_posts.html")

# Create your views here.
'''def all_posts(request):

     all_posts=Post.objects.all()

     context = {
         'all_posts': all_posts ,
     }
     return render(request,'all_posts.html',context)



def post(request,id):
    # post=get_object_or_404(Quap,id=id)

     post = Post.objects.all()
     context = {
         'detail': post ,
     }
     return render(request,'detail.html',context)'''

