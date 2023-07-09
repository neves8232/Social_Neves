
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Post, LikePost, Comment, FollowersCount
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url='signin')
def index(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    posts = Post.objects.all()
    comments = Comment.objects.all()

    return render(request, 'index.html', {'user_profile': user_profile, 'posts': posts, 'comments': comments})

@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user_profile = get_object_or_404(Profile, user=request.user)
        img_url = user_profile.profileimg.url
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=request.user.username, image=image, caption=caption, img_url=img_url)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

# Rest of your views here...
