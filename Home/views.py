from django.shortcuts import redirect, render
from django.contrib.auth import logout
# Create your views here.
from .form import *
import datetime

def home(request):
    #print("Timeeeeeeeeeeeeeee: ", datetime.datetime.now().strftime("%H:%M:%S"))
    tm=datetime.datetime.now()
    #print("tmmmmmm: ", tm)
    context={'blogs':BlogModel.objects.all()}
    context['tim']=tm
   #print("Context: ", context)
    return render(request, "index.html", context)

def register(request):
    context={}
    tm=datetime.datetime.now()
    context['tim']=tm
    return render(request, "register.html", context)
def login(request):
    context={}
    tm=datetime.datetime.now()
    context['tim']=tm
    return render(request, "login.html", context)

def blogdetail(request, slug):

    context={}
    print(f"Slug value is {slug}")
    try:
        print(f"Slug -- value is {slug}")
        blogobj=BlogModel.objects.filter(slug=slug).first()
        print(f"blogobj is {blogobj}")
        context['blogobj']=blogobj
    except Exception as e:
        print(e)
    tm=datetime.datetime.now()
    context['tim']=tm
    print("Context: ", context)
    return render(request, "blogdetail.html", context)


def seeblog(request):
    context={}
    try:
        blogall=BlogModel.objects.filter(user=request.user)
        print(f"blogall: {blogall}")
        context['blogall']=blogall
    except Exception as e:
        print(e)
    print(f"Context is: {context}")
    tm=datetime.datetime.now()
    context['tim']=tm
    return render(request, "seeblog.html", context)

def blogdelete(request, id):
    print(f"Id is: {id}")
    try:
        blogdel=BlogModel.objects.get(id=id)

        if blogdel.user==request.user:
            blogdel.delete()
            return redirect("seeblog")

    except Exception as e:
        print(e)
    context={}
    tm=datetime.datetime.now()
    context['tim']=tm
    return render(request, "seeblog.html", context)

def blogupdate(request, slug):
    context={}
    try:
        blogup=BlogModel.objects.get(slug=slug)
        print(f"blogup: {blogup}")

        if blogup.user!=request.user:
            return redirect("/")

        initialdict={'content':blogup.content, 'img':blogup.img}
        form=Blogform(initial=initialdict)
        #Content from Add Blog
        if request.method=='POST':
            form = Blogform(request.POST)
            title = request.POST.get("title")
            img = request.FILES['image']
            user = request.user
            print(f"form : {form} and title: {title} and img={img} and user={user}....")

            if form.is_valid():
                print("Forrmmmmmmm is Validddddd.")
                content=form.cleaned_data['content']

            # blogup =BlogModel.objects.create(
            #     user=user,
            #     title=title,
            #     img=img,
            #     content=content
            # )

            blogup =BlogModel.objects.filter(slug=slug).update(
                user=user,
                title=title,
                img=img,    
                content=content
            )
            return redirect("/")
        
        context['blog_obj']=blogup
        context['form']=form
        tm=datetime.datetime.now()
        context['tim']=tm
        #context['form']=content
    except Exception as e:
        print(e)
    return render(request, "updateblog.html", context)

def logoutview(request):
    logout(request)
    return redirect("/")

def addblog(request):
    context={'form':Blogform}
    try:
        if request.method=='POST':
            form = Blogform(request.POST)
            title = request.POST.get("title")
            img = request.FILES['image']
            user = request.user
            print(f"form : {form} and title: {title} and img={img} and user={user}....")

            if form.is_valid():
                print("Forrmmmmmmm is Validddddd.")
                content=form.cleaned_data['content']

            bobj=BlogModel.objects.create(
                user=user,
                title=title,
                img=img,
                content=content
            )
            print(f"BlogModel: {bobj}")
            return redirect('/')
    except Exception as e:
        print(e)

    tm=datetime.datetime.now()
    context['tim']=tm
    return render(request, "addblog.html", context)

