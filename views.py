import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    content_html = open("templates/index.html").read()
    context = { "content": content_html}
    return render(request, "base.html", context)


def about(request):
    content_html = open("templates/about.html").read()
    context = { "content": content_html}
    return render(request, 'base.html', context)

def work(request):
    content_html = open("templates/work.html").read()
    context = { "content": content_html}
    return render(request, 'base.html', context)   

def contact(request):
    content_html = open("templates/contact.html").read()
    context = { "content": content_html}
    return render(request, 'base.html', context) 

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

