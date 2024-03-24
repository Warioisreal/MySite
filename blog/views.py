from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
from .models import Post, Task, Solution, Comment, Course
from .forms import PostForm, TaskForm, SolutionForm, CommentForm, CourseForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'blog/home.html')

def it(request):
    posts = Post.objects.filter(index='i')
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/it.html', context)

def it_task(request):
    posts = Post.objects.filter(index='i')
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/it_task.html', context)

def phisics(request):
    posts = Post.objects.filter(index='p')
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/phisics.html', context)

def phisics_task(request):
    posts = Post.objects.filter(index='p')
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/phisics_task.html', context)

def math(request):
    posts = Post.objects.filter(index='m')
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/math.html', context)

def math_task(request):
    posts = Post.objects.filter(index='m')
    context = {
        'posts': posts,
        'group': request.user.groups.all()
    }
    return render(request, 'blog/math_task.html', context)

def sandbox(request):
    return render(request, 'blog/sandbox.html')

def about(request):
    return render(request, 'blog/about.html')

def task_list(request):
    template = 'blog/task_list.html'
    template_page = 'blog/task_list_page.html'
    sub = request.GET.get('s')
    clas = request.GET.get('c')
    theme = request.GET.get('n')
    tasks = Task.objects.filter(index = sub, clas = clas, chapter_title = theme)
    paginator = Paginator(tasks, 8)
    page = request.GET.get('page')
    tasks_only = request.GET.get('tasks_only')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        if tasks_only:
            return HttpResponse('')
        tasks = paginator.page(paginator.num_pages)
    context = {
    'tasks': tasks,
    'group': request.user.groups.all(),
    'sub': sub,
    'clas': clas,
    'theme': theme
    }
    if tasks_only:
        return render(request, template_page, context)
    return render(request, template, context)

def task(request, id):
    queryset = Task.objects.all()
    task = get_object_or_404(queryset, pk=id)
    solutions = Solution.objects.all()
    comments = Comment.objects.all()
    value = request.GET.get('value')
    context = {
    'task': task,
    'solutions': solutions,
    'comments': comments,
    'group': request.user.groups.all(),
    'value': value
    }
    return render(request, 'blog/task.html', context)

@login_required
def delete_post(request, id):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=id)
    context = {
    'post': post,
    'group': request.user.groups.all()
    }
    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)

    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('posts')


@login_required
def edit_post(request, id):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=id)
    if request.method == 'GET':
        context = {
        'form': PostForm(instance=post), 'id': id,
        'group': request.user.groups.all(),
        'title': post.title,
        'content': post.content,
        'lesson': post.index
        }
        return render(request, 'blog/post_form.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('posts')

        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form':form})


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {
        'form': PostForm(),
        'group': request.user.groups.all()
        }
        return render(request, 'blog/post_form.html', context)
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
            return render(request, 'blog/post_form.html', {'form':form})

@login_required
def delete_task(request, id):
    queryset = Task.objects.all()
    task = get_object_or_404(queryset, pk=id)
    context = {
    'task': task,
    'group': request.user.groups.all()
    }
    if request.method == 'GET':
        return render(request, 'blog/task_confirm_delete.html', context)

    elif request.method == 'POST':
        task.delete()
        messages.success(request, 'The task has been deleted successfully.')
        return redirect('posts')

@login_required
def edit_task(request, id):
    queryset = Task.objects.all()
    task = get_object_or_404(queryset, pk=id)
    if request.method == 'GET':
        context = {
        'form': TaskForm(instance=post), 'id': id,
        'group': request.user.groups.all(),
        'title': task.title,
        'chapter_title': task.chapter_title,
        'content': task.content,
        'upload': task.upload,
        'author': task.author,
        'lesson': task.index
        }
        return render(request, 'blog/task_form.html', context)

    elif request.method == 'POST':
        form = TaskForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The task has been updated successfully.')
            return redirect('posts')

        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/task_form.html', {'form':form})


@login_required
def create_task(request):
    if request.method == 'GET':
        context = {
        'form': TaskForm(),
        'group': request.user.groups.all()
        }
        return render(request, 'blog/task_form.html', context)
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, 'The task has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/task_form.html', {'form':form})

@login_required
def delete_course(request, id):
    queryset = Course.objects.all()
    course = get_object_or_404(queryset, pk=id)
    context = {
    'course': course,
    'group': request.user.groups.all()
    }
    if request.method == 'GET':
        return render(request, 'blog/course_confirm_delete.html', context)

    elif request.method == 'POST':
        course.delete()
        messages.success(request, 'The course has been deleted successfully.')
        return redirect('posts')

@login_required
def edit_course(request, id):
    queryset = Course.objects.all()
    course = get_object_or_404(queryset, pk=id)
    if request.method == 'GET':
        context = {
        'form': CourseForm(instance=post), 'id': id,
        'group': request.user.groups.all(),
        'title': course.title,
        'chapter_title': course.chapter_title,
        'content': course.content,
        'upload': course.upload,
        'author': course.author,
        'lesson': course.index
        }
        return render(request, 'blog/course_form.html', context)

    elif request.method == 'POST':
        form = CourseForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The course has been updated successfully.')
            return redirect('posts')

        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/course_form.html', {'form':form})


@login_required
def create_course(request):
    if request.method == 'GET':
        context = {
        'form': CourseForm(),
        'group': request.user.groups.all()
        }
        return render(request, 'blog/course_form.html', context)
    elif request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, 'The course has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/course_form.html', {'form':form})

@login_required
def delete_solution(request, id):
    queryset = Solution.objects.all()
    solution = get_object_or_404(queryset, pk=id)
    context = {
    'solution': solution,
    'group': request.user.groups.all()
    }
    if request.method == 'GET':
        return render(request, 'blog/solution_confirm_delete.html', context)

    elif request.method == 'POST':
        solution.delete()
        messages.success(request, 'The solution has been deleted successfully.')
        return redirect('posts')

@login_required
def edit_solution(request, id):
    queryset = Solution.objects.all()
    solution = get_object_or_404(queryset, pk=id)
    if request.method == 'GET':
        context = {
        'form': SolutionForm(instance=post), 'id': id,
        'group': request.user.groups.all(),
        'title': solution.title,
        'chapter_title': solution.chapter_title,
        'content': solution.content,
        'upload': solution.upload,
        'author': solution.author,
        'lesson': solution.index
        }
        return render(request, 'blog/solution_form.html', context)

    elif request.method == 'POST':
        form = SolutionForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The solution has been updated successfully.')
            return redirect('posts')

        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/solution_form.html', {'form':form})


@login_required
def create_solution(request):
    if request.method == 'GET':
        context = {
        'form': SolutionForm(),
        'group': request.user.groups.all()
        }
        return render(request, 'blog/solution_form.html', context)
    elif request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, 'The solution has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/solution_form.html', {'form':form})