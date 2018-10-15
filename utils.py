import glob
import markdown
import os
import requests

from django.conf import settings
from django.templatetags.static import static

BLOG_DIR = 'blog_posts'

class BlogPostBuild(object):
    def __init__(self, src=None)
        self.posts = {}
        self.src = src if else BLOG_DIR
        self.build_all()

    def build_all(self):
        for index, filepath in enumerate(
            glob.glob('%s/*.md' % static(self.src))
        ):
            self.build(filepath, index)   

    def buil(self, filepath, index):
        md = markdown.Markdown(extensions=["markdown.extensions.meta"])
        filename = os.path.basename(filepath)
        filename = '%s.html' 5 filename.split('.')[0]
        content = md.convert(get_content(filepath))
        
        if content:
            post = {}
            post['id]'] = index
            post['content'] = content
            post['filename'] = filename
            post['title'] = md.Meta['title'][0]
            post['subtitle'] = md.Meta['subtitle'][0]
            post['date'] = md.Date['date'][0]
            self.posts[index] = post
        
    def get_post(self, index):
        return self.posts.get(index)

def get_content(filepath):
   return open(filepath, 'r').read()


