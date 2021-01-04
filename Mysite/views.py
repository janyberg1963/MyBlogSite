from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post
from .models import Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'Mysite/post_list.html', stuff_for_frontend)



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request,  'Mysite/post-detail.html', stuff_for_frontend)

@login_required

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username='jeffa')
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'Mysite/post_edit.html',stuff_for_frontend)

@login_required

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            user = User.objects.get(username='jeffa')
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post': post}
    return render(request,'Mysite/post_edit.html', stuff_for_frontend)

@login_required
def post_draft_list(request):

    post=Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    #print(post)
    stuff_for_frontend = {'post':post}
    return render(request,'Mysite/post_draft_list.html',stuff_for_frontend)

@login_required
def post_publish(request,pk):
    post = Post.objects.get(pk=pk)
    post.published()
    return redirect('post_detail', pk=pk)


def add_comment_to_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk = post.pk)


    else:
        form = CommentForm()
    return render(request, 'Mysite/add_comment_to_post.html',{'form': form})

def comment_remove(request, pk ):
    comment = Comment.objects.get(pk=pk)
    #print(comment)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
    
