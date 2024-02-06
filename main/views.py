from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm
# Create your views here.

menu = [{"title": "Посты", "url_name": "main:post_list"},
        {"title": "Добавить пост", "url_name": "main:post_add"},
        {"title": "О сайте", "url_name": "main:about"},
        {"title": "Контакты", "url_name": "main:contacts"},
]
# главная страница сайта
def index_root(request):
    return redirect(post_list)

# главная страница приложения main
def index(request):
    return HttpResponsePermanentRedirect("/blog/posts/")

def about(request):
    title = "О сайте"
    context = {"menu": menu, "title": title}
    return render(request, 'main/about.html', context=context)

def contacts(request):
    title = "Контакты"
    context = {"menu": menu, "title": title}
    return render(request, 'main/contacts.html', context=context)

 # отображение списка постов
def post_list(request):
    # получвем все объекты таблицы(модели) Post
    posts = Post.objects.all()
    posts = Post.objects.filter()
    # заносим их в объект контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name='main/post_list.html', context=context)

@login_required
def post_add(request):
    title = "Создать пост"
    if request.method == "GET":
        form = PostForm()
        context = {"title": title, "menu": menu, "form": form}
        return render(request, "main/post_add.html", context)
    
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = Post()
            post.author = request.user
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            # post.image.url = post_form.cleaned_data['image.url']
            post.save()

            return post_list(request)
        
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    title = "Информация с посте"
    context = {"post": post, "title": title, "menu": menu}
    return render(request, template_name="main/post_detail.html", context=context)

def post_update(request, pk):
    # получаем объект модели Пост
    post = Post.objects.get(pk=pk)
    title = "Изменнить пост"

    # При отправки формы методом POST
    if request.method == "POST":
        # Заполняем объект формы из запроса 
        form = PostForm(request.POST, request.FILES, instance=post)
        # Сохраняем форму
        if form.is_valid():
            form.save()
            return redirect("main:post_detail", pk=pk)
    # Если методь GET
    form = PostForm(instance=post)
    return render(request, "main/post_update.html", context={"form": form, "title": title, "menu": menu})

def post_delete(request, pk):
    post = Post.objects.filter(pk=pk).first()

    if request.method == "POST":
        if "delete" in request.POST:
            post.delete()
            return redirect("main:post_list")
        if "cancel" in request.POST:
            return redirect("main:post_list")
    
    form = PostForm(instance=post)
    return render(request, "main/post_delete.html", {"form": form, "menu": menu})


# def post_update(request, pk):
#     # получаем объект модели Пост
#     post = Post.objects.get(pk=pk)
#     title = "Изменнить пост"

    # # При отправки формы методом POST
    # if request.method == "POST":
    #     # Заполняем объект формы из запроса 
    #     form = PostForm(request.POST, request.FILES, instance=post)
    #     # Сохраняем форму
    #     if form.is_valid():
    #         form.save()
    #         return redirect("main:post_detail", pk=pk)
    # # Если методь GET
    # form = PostForm(instance=post)
    # return render(request, "main/post_update.html", context={"form": form, "title": title, "menu": menu})   


    