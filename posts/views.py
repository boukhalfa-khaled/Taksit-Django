from django.shortcuts import redirect, render , get_object_or_404
from django.db.models import Count
# from django.views import View
# from .forms  import  PostForm
from .models import Category , Post ,PostImage, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.files.storage import default_storage
from users.models import User

# Create your views here.


@login_required(login_url='login')
def create_post(request):

    if request.user.role != 'seller':
        messages.error(request, 'Only sellers can create posts.')
        return redirect('profile')


    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request,  'posts/createPost.html', context)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category_name = request.POST['category']
        price = request.POST.get('price')
        wilaya = request.POST.get('wilaya')
        is_cash = request.POST.get('is_cash') == 'on'  # Convert to boolean
        if not is_cash:
            months = request.POST.get('months')


        if not title:
            messages.error(request, 'title is required')
            return render(request,  'posts/createPost.html', context)

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'posts/createPost.html', context)

        if not price:
            messages.error(request, 'Price is required')
            return render(request, 'posts/createPost.html', context)

        if not is_cash and not months:
            messages.error(request, 'Months is required for cash transactions')
            return render(request, 'posts/createPost.html', context)

        images = request.FILES.getlist('images')




        category = Category.objects.get(name=category_name)
        post = Post.objects.create( seller=request.user,
            title=title,
            description=description,
            category=category,
            price=price,
            is_cash=is_cash,
            months=months if not is_cash else None,
            wilaya=wilaya
        )
        for image in images:
            file_name = default_storage.save('uploads/postImges/' + image.name, image)
            PostImage.objects.create(post=post, image=file_name)
        messages.success(request, 'Product saved successfully')
        return redirect('profile')

def home(request):
    posts = Post.objects.all()
    post_data = []
    for post in posts:
        post_images = PostImage.objects.filter(post=post)
        image_url = post_images.first().image.url
        post_data.append({'post': post, 'image': image_url})

    context = {'posts':post_data}
    return render(request,'posts/home.html', context)

def posts(request):
    posts = Post.objects.all()
    post_data = []
    for post in posts:
        post_images = PostImage.objects.filter(post=post)
        image_url = post_images.first().image.url
        post_data.append({'post': post, 'image': image_url})

    context = {'posts':post_data}
    return render(request,'posts/posts.html', context)

def investerMarket(request):
    # posts = Post.objects.all()
    # post_data = []
    # for post in posts:
    #     post_images = PostImage.objects.filter(post=post)
    #     image_url = post_images.first().image.url
    #     post_data.append({'post': post, 'image': image_url})

    # context = {'posts':post_data}
    # return render(request,'posts/posts.html', context)
    # orders = Order.objects.all()
    orders_with_post_count = Order.objects.values('post').annotate(order_count=Count('id'))

    post_data = []

    for order in orders_with_post_count:
        post = Post.objects.get(pk=order['post'])
        post_images = PostImage.objects.filter(post=post)
        image_url = post_images.first().image.url if post_images.exists() else None
        order_count = order['order_count']
        post_data.append({'post': post, 'image': image_url, 'order_count': order_count})

    context = {'posts': post_data}
    return render(request, 'posts/investerMarket.html', context)



def post_detail(request, post_id):
    # post = get_object_or_404(Post, id=post_id)
    post = Post.objects.get(id=post_id)
    post_images = PostImage.objects.filter(post=post)
    image_urls = []
    for post_image in post_images:
        image_urls.append(post_image.image.url)

    if request.user.is_authenticated:
        has_ordered = Order.objects.filter(post=post, customer_id=request.user).exists()
    else:
        has_ordered = False

    context = {'post':post, 'images': image_urls, 'has_ordered': has_ordered }
    return render(request,'posts/single_post.html', context)



@login_required
def create_order(request, post_id):
    post = Post.objects.get(id=post_id)
    customer = request.user

    if customer.role != User.CUSTOMER:
        messages.error(request, 'Only customers can order')
        return render(request,'posts/single_post.html')

    # Create the order
    order = Order(post=post, customer_id=customer)
    order.save()

    return redirect('post_detail', post_id=post_id)