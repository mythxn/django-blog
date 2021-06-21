from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "myth",
        "title": "hello_world",
        "content": "first post content",
        "date_posted": "Aug 27, 2018",
    },
    {
        "author": "jasonbourne",
        "title": "post_2",
        "content": "hmm",
        "date_posted": "Aug 28, 2021",
    },
]


def home(request):
    context = {
        "posts": posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
