from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Poem, Comment, WishlistItem
from .forms import RegisterForm, PoemForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Use named URL 'home' for better flexibility
            return redirect(request.GET.get('next', 'home'))  # Redirect to 'next' or home
    else:
        form = AuthenticationForm()
    return render(request, 'poems/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('poem_list')  # Redirect to poem list after registration
    else:
        form = RegisterForm()
    return render(request, 'poems/register.html', {'form': form})

@login_required
def create_poem(request):
    if request.method == 'POST':
        form = PoemForm(request.POST, request.FILES)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user
            poem.save()
            return redirect('poem_list')  # Redirect to poem list after poem creation
    else:
        form = PoemForm()
    return render(request, 'poems/create_poem.html', {'form': form})

def poem_list(request):
    poems = Poem.objects.all()
    return render(request, 'poems/poem_list.html', {'poems': poems})

def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    comments = poem.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.poem = poem
            comment.author = request.user
            comment.save()
            return redirect('poem_detail', pk=poem.pk)  # Redirect to the same poem's detail page after comment submission
    else:
        form = CommentForm()
    return render(request, 'poems/poem_detail.html', {'poem': poem, 'comments': comments, 'form': form})

@login_required
def add_to_wishlist(request, poem_id):
    poem = get_object_or_404(Poem, pk=poem_id)  # Ensure we're using poem_id
    # Prevent duplicates: Check if the item already exists in the wishlist
    if not WishlistItem.objects.filter(poem=poem, user=request.user).exists():
        wishlist_item = WishlistItem(poem=poem, user=request.user)
        wishlist_item.save()
    return redirect('wishlist')  # Redirect to wishlist page

@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'poems/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_wishlist(request, pk):
    item = get_object_or_404(WishlistItem, user=request.user, poem_id=pk)
    item.delete()
    return redirect('wishlist')  # Redirect to wishlist page after removing item

def home(request):
    featured_poems = Poem.objects.filter(featured=True)[:3]  # Featured poems
    recent_poems = Poem.objects.order_by('-created_at')[:3]  # Recent poems
    return render(request, 'poems/home.html', {'featured_poems': featured_poems, 'recent_poems': recent_poems})
