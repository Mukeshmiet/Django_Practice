from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , Http404
from django.urls import reverse
# Create your views here.

articles={
    "sports": "sports page",
    "finance": "finance page",
    "politics": "politics page",
}
def app_one_view(request, topic):
    try:
        res= articles[topic]
        return HttpResponse(res)
    except:
        raise Http404("Page Not Found")

def page_number_view(request, num_page):
    try:
        topics_list = list(articles.keys())
        topic = topics_list[num_page]
        webpage = reverse("topic_page", args=[topic])
    except:
        raise Http404("Page Not Found")
    else:
        return HttpResponseRedirect(webpage)