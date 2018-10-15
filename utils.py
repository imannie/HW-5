

import glob
import os
from jinja2 import Template
import markdown

pages = []

def main():
    for page in pages:
        filename = page['filename']
        title = page['title']
        output = page['output']
        footer = '<p>Learn To Code. Code Away</p>'
        page_html = open(filename).read()
        if filename.endwith('md'):
            page_html = md_converted(page_html)
        template_html = open('templates/base.html').read()
        index_page = Template(template_html)
        rendered = index_page.render(
                                       title = title,
                                       footer = footer,
                                       content = page_html,
                                       )
        open(output, 'w+').write(rendered)



def dict():
    all_html_files = glob.glob("content/*.html")
    for file in all_html_files:
        file_path = file
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        list_dict = {}
        list_dict['filename'] = filename
        list_dict['title'] = name_only
        list_dict['output'] = 'docs/' + file_name
        pages.append(list_dict)

    
    
def md_converted(page):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    data = open(page['filename']).read()
    html = md.convert(data)
    return html


main()




