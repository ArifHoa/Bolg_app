from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # request.FILES জরুরি
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if post.image:  # যদি ইমেজ থাকে
            post.image.delete(save=False)  # মিডিয়া ফাইল থেকেও ডিলিট করে
        post.delete()  # তারপর ডেটাবেস থেকে রেকর্ড ডিলিট
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})



#conctar
def reg_ster(request):

    return render(request, 'register.html')



def login_site(request):

    return render(request, 'login.html')



