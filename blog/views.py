from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm



def home(request):
    return render(request, 'blog/home.html')

#def group_take(request):
#    return(str(request.user.groups.all())[19:-3] == "Moderators")
#???

def it(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/it.html', context)

def it_task(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/it_task.html', context)

def phisics(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/phisics.html', context)

def phisics_task(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/phisics_task.html', context)

def math(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/math.html', context)

def math_task(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/math_task.html', context)

def sandbox(request):
    return render(request, 'blog/sandbox.html')

def about(request):
    return render(request, 'blog/about.html')

@login_required
def delete_post(request, id):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=id)
    context = {'post': post}
    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html',context)

    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('posts')


@login_required
def edit_post(request, id):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=id)
    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request,'blog/post_form.html',context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('posts')

        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request,'blog/post_form.html',context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})