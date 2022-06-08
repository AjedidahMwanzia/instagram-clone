from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Image,Profile, Follow, Comments, Likes
from django.http  import HttpResponse,Http404
from django.contrib import messages


# Create your views here.
@login_required
def home(request):
    images=Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
   
    return render(request,'index.html',{'images':images})
    
def post_create(request,image_id):
    image=get_object_or_404(Image,id=image_id)
    comments=Comments.objects.filter(image=image).all()
    current_user=request.user
    if request.method =='POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            
            comment.image = image
            comment.save()
        return redirect('home')
    else:
        
        form = CommentForm()
    return render(request, 'post_create.html', {'image': image, 'form':form, 'comments':comments})
    
def post_detail(request,image_id):
    image=get_object_or_404(Image,id=image_id)
    comments=Comments.objects.filter(image=image).all()
    current_user=request.user
    if request.method =='POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            
            comment.image = image
            comment.save()
        return redirect('home')
    else:
        
        form = CommentForm()
    return render(request, 'post_detail.html', {'image': image, 'form':form, 'comments':comments})

@login_required
def search_results(request):
  if 'name' in request.GET and request.GET["name"]:
    name = request.GET.get('name')
    users = Profile.search_profiles(name)
    images = Image.search_images(name)
    print(users)
    return render(request, 'search.html', {"users": users, "images": images})
  else:
    return render(request, 'search.html')

@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    current_user=get_object_or_404(User,id=user_id)
    # current_user = request.user
    images = Image.objects.filter(name=current_user)
    profile = get_object_or_404(Profile,id = current_user.id)
    return render(request, 'profile/profile.html', {"images": images, "profile": profile})

@login_required(login_url='/accounts/login/')
def post_detail(request):
    if request.method=='POST':
        current_user=request.user
        form=AddImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
            messages.success(request,('Image was posted successfully!'))
            return redirect('home')
    else:
            form=AddImageForm()
    return render(request,'post_detail.html',{'form':form})
def update_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully updated your account!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile/update_profile.html', context)

def like_image(request, image_id):
    image = get_object_or_404(Image,id = image_id)
    like = Likes.objects.filter(image = image ,user = request.user).first()
    if like is None:
        like = Likes()
        like.image = image
        like.user = request.user
        like.save()
    else:
        like.delete()
    return redirect('home')

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_images = user_prof.profile.images.all()
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    params = {
        'user_prof': user_prof,
        'user_images': user_images,
        'followers': followers,
        'follow_status': follow_status
    }
    print(followers)
    return render(request, 'users/user_profile.html', params)

def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('profile', user_profile3.user.username)

def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('profile', user_profile2.user.username)


