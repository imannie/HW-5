import glob
import markdown
import os
import requests

from django.http import HttpResponse
from django.shortcuts import render
from django.templates import templates, context
from utils import BlogPostBuild

blog_post_build = BlogPostBuild()


def index(request):
    content_html = open("templates/index.html").read()
    context = { "content": content_html}
    return render(request, 'base.html', context)


def about(request):
    content_html = open("templates/about.html").read()
    context = { "content": content_html}
    return render(request, 'about.html', context)

def work(request):
    content_html = open("templates/work.html").read()
    context = { "content": content_html}
    return render(request, 'work.html', context)

def contact(request):
    content_html = open("templates/contact.html").read()
    context = { "content": content_html}
    return render(request, 'contact.html', context)


def blog_post(request, post_id):
    context_html = open("templates/blog_post.html").read()
    context = { "content": content_html}
    return render(request, 'blog_post.html', context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

message = []

def contact(request):
    name = request.POST.get('myname')
    print('Name received', name)
    
    email = request.POST.get('email')
    print('Email received', email)
    
    message = request.POST.get('message')
    print('Message received:', message)

    if name and email and message:
        message_dict = {
            'message': message,
            'email': email,
            'name': name,
        }
        messages.append(message_dict)

    message_html = '<ol>'
    for message in messages:
        message_html += '<li>' +message['name'] + ': ' +
            message['message'] + '<li>'
    message_html += '<ol>'

    return HttpResponse('''
        <p class='subtitle'>I'd love to hear from you! <i class="fa fa-heart-o" aria-hidden="true"></i> Drop me a line.</p>
        
        ''' + message_html + '''
            
        <form class="form_edit">
        <div class="form-group">
        <input type="name" class="form-control" id="exampleInputName" placeholder="Name">
        </div>
        
        <div class="form-group">
        <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
        </div>
        
        <div class="form-group">
        <textarea class="form-control" rows="5" placeholder="Message"></textarea>
        </div>
        <button type="submit" class="btn btn-rabbit submit">Send Message</button>
        </form>
        ''')




