from django.shortcuts import render, get_object_or_404
from .models import News, Categories

def news_list(request):
     news_list = News.published.all()
     context = {
         "news_list": news_list
     }
     return render(request, 'news/news_list.html', context)
 
def news_detail(request, id):
    news_item = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        'news_item': news_item
    }
    return render(request, 'news/news_detail.html', context)

def homePage(request):
    news = News.published.all()
    categories = Categories.objects.all()
    context = {
        'news': news,
        'categories': categories
    }
    
    return render(request, 'news/index.html', context)