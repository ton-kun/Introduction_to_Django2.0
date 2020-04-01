
from django.http import HttpResponse
# レンダリング用。直接テンプレートを呼び出しHTTPリスポンスとして返却できる
from django.shortcuts import render

from hashlib import md5

from random import random

def index(request):
    """
    return HttpResponse(
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8"/>
            <link rel="stylesheet" href="/static/style.css"/>
          </head>
          <body>
            <h1>Hello world</h1>
          </body>
        </html>
            )

    renderメソッドは、request、template_name、contextという3つの引数を取ります。（実際にはもっと沢山の引数を取ります。）
    そして、requestの中には、セッションの情報や、requestの種類（getかpost）の情報が入っています。
    template_nameには、表示するhtmlファイルの情報が入っています。
    contextには、データベースに入っているデータの情報が入っています。
    """
    
    # return render(request, 'index.html', {'title': 'Hello world'})
    # return render(request, 'index.html', {"obj": {"title": "hoge"}})
    # return render(request, 'index.html', {"unescaped": "<script>alert('hoge')</script>"})
    # return render(request, 'index.html', {"random": random()})
    # return render(request, 'index.html', {"l": [{"name":"hoge","value":"1"},{"name":"fuga","value": "2"},{"name":"foo","value":"3"}]})
    # return render(request, 'index.html')
    return render(request, 'index.html', {'title': "タイトル", "message": "メッセージ"})

def hoge(request):
    return HttpResponse("hoge")

# 投げられたfooを受け取る
def fuga(request, foo):
    """
    return HttpResponse('Fuga')
    """
    return render(request, 'index.html', {'title': foo})

# GETメソッド
def search(request):
    q = request.GET.get('q')
    return HttpResponse(q)

def render_form(request):
    return render(request, 'login.html')

def login(request):
    print(request)
    if request.POST['username'] and request.POST['email']:
        return render(request, 'check.html', 
          {"email": request.POST["username"], "username": request.POST['email']})
    else:
        return render(request, 'error.html')


def form(request):
    return render(request, 'form.html')




def upload(request):
    if request.method =='POST' and request.FILES and (request.FILES['image'].content_type == "image/png" or request.FILES['image'].content_type =="image/jpeg"):
        extention = ".jpg"
        if request.FILES['image'].content_type == "image/png":
            extention = '.png'
        print(request.FILES['image'].name)
        filepath ='static/' + md5(request.FILES['image'].name.encode('utf-8')).hexdigest() + extention


        image = open(filepath, 'wb')
        for chunk in request.FILES['image'].chunks():
            image.write(chunk)
        return render(request, 'result.html', {'filepath': filepath, 'name':'Hoge'})
    else:
        return HttpResponse('/form')