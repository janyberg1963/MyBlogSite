from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'Mysite/post_list.html', stuff_for_frontend)



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request,  'Mysite/post-detail.html', stuff_for_frontend)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username='jeffa')
            post = form.save(commit=False)
            post.author = user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'Mysite/post_edit.html',stuff_for_frontend)
