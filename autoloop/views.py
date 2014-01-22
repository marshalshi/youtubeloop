from django.shortcuts import render

def loopone(request, id):
    return render(request, 'loopone.html', {'the_id':id})

from django import forms
from django.utils.html import mark_safe
import urllib, urllib2, os

class Search(forms.Form):
    search = forms.CharField()

def search(request):
    if request.method == "POST":
        print 123
        form = Search(request.POST)
        if form.is_valid():
            name = form.cleaned_data['search']
            name = urllib.quote(name)
            name = name.replace('%20','+')
            req = urllib2.Request('http://www.youtube.com/results?search_query=' + name)
            response = urllib2.urlopen(req)
            the_page = response.read()
            the_page = addMyJSCode(the_page)
            tmp_directory = os.chdir('templates')
            tmp_file = open('tmp.html','w')
            tmp_file.write(the_page)
            tmp_file.close()
            tmp_directory = os.chdir('..')
            return render(request, 'tmp.html')
    else:
        print 321123
        form = Search()
    return render(request, 'search.html', {
        'form': form,
    })

import lxml.html as lh
import io
from BeautifulSoup import BeautifulSoup

def addMyJSCode(file):
    root = lh.fromstring(file)
    scriptString1 = mark_safe("<script src='//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js'>")
    scriptString2 = mark_safe("</script><script type='text/javascript' src='http://127.0.0.1:8000/static/js/myjs.js' ></script>")
    link = lh.fromstring(scriptString2).find('.//script')
    head = root.find('.//head')
    title = head.find('script')
    if title == None:
        where = 0
    else:
        where = head.index(title) + 1
    head.insert(where, link)
    link = lh.fromstring(scriptString1).find('.//script')
    if title == None:
        where = 0
    else:
        where = head.index(title) + 1
    head.insert(where, link)
    return lh.tostring(root)
