from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.http import Http404


from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str , DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib import auth

from .utils import token_generator
from posts.models import Post , Category , PostImage, Order
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.files.storage import default_storage

# Create your views here.


class RegisterCustomerView(View):
  def get(self, request):
    return render(request, 'users/register-customer.html')
  def post(self, request):

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    role = request.POST.get('role', User.CUSTOMER)  
    profile_picture = request.FILES.get('profile_picture')
    document = request.FILES.get('document', '')


    context={
      'fieldValues' : request.POST
    }
    if not User.objects.filter(email=email).exists():
      if len(password)<6:
        messages.error(request, 'Password Too Short')
        return render(request, 'users/register.html', context)

      if profile_picture:
        file_name = default_storage.save('uploads/profile/' + profile_picture.name, profile_picture)

      if document:
        document_name = default_storage.save(document.name, document)
      else:
        document_name = None

      user = User.objects.create_user(email=email, first_name=firstname, last_name=lastname, role=role ,img=file_name, file = document_name )
      user.set_password(password)
      user.is_active = False
      if role == User.CUSTOMER:
          user.is_active = True
      else:
          user.is_active = False
      user.save()
      uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
      domain = get_current_site(request).domain
      link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
      activate_url='http://'+domain+link
      email_subject = 'Activate Your Account'
      email_body = 'Hi '+ user.last_name \
      +' Please use the link to verify your account\n'+activate_url
      email = EmailMessage(email_subject,email_body,"miketayson75b@gmail.com",[email])
      email.send(fail_silently=False)
      messages.success(request, 'Account successfully created')
      return render(request, 'users/login.html')
    else:
      messages.error(request, 'email in use')
      return render(request, 'users/register.html')


class RegisterSellerView(View):
  def get(self, request):
    return render(request, 'users/register-seller.html')
  def post(self, request):

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    role = request.POST.get('role', User.CUSTOMER)  
    profile_picture = request.FILES.get('profile_picture')
    document = request.FILES.get('document', '')


    context={
      'fieldValues' : request.POST
    }
    if not User.objects.filter(email=email).exists():
      if len(password)<6:
        messages.error(request, 'Password Too Short')
        return render(request, 'users/register.html', context)

      if profile_picture:
        file_name = default_storage.save('uploads/profile/' + profile_picture.name, profile_picture)

      if document:
        document_name = default_storage.save(document.name, document)
      else:
        document_name = None

      user = User.objects.create_user(email=email, first_name=firstname, last_name=lastname, role=role ,img=file_name, file = document_name )
      user.set_password(password)
      user.is_active = False
      if role == User.CUSTOMER:
          user.is_active = True
      else:
          user.is_active = False
      user.save()
      uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
      domain = get_current_site(request).domain
      link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
      activate_url='http://'+domain+link
      email_subject = 'Activate Your Account'
      email_body = 'Hi '+ user.last_name \
      +' Please use the link to verify your account\n'+activate_url
      email = EmailMessage(email_subject,email_body,"miketayson75b@gmail.com",[email])
      email.send(fail_silently=False)
      messages.success(request, 'Account successfully created')
      return render(request, 'users/login.html')
    else:
      messages.error(request, 'email in use')
      return render(request, 'users/register.html')








class RegisterInvesterView(View):
  def get(self, request):
    return render(request, 'users/register.html')
  def post(self, request):

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    role = request.POST.get('role', User.CUSTOMER)  
    profile_picture = request.FILES.get('profile_picture')
    document = request.FILES.get('document', '')


    context={
      'fieldValues' : request.POST
    }
    if not User.objects.filter(email=email).exists():
      if len(password)<6:
        messages.error(request, 'Password Too Short')
        return render(request, 'users/register.html', context)

      if profile_picture:
        file_name = default_storage.save('uploads/profile/' + profile_picture.name, profile_picture)

      if document:
        document_name = default_storage.save(document.name, document)
      else:
        document_name = None

      user = User.objects.create_user(email=email, first_name=firstname, last_name=lastname, role=role ,img=file_name, file = document_name )
      user.set_password(password)
      user.is_active = False
      if role == User.CUSTOMER:
          user.is_active = True
      else:
          user.is_active = False
      user.save()
      uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
      domain = get_current_site(request).domain
      link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
      activate_url='http://'+domain+link
      email_subject = 'Activate Your Account'
      email_body = 'Hi '+ user.last_name \
      +' Please use the link to verify your account\n'+activate_url
      email = EmailMessage(email_subject,email_body,"miketayson75b@gmail.com",[email])
      email.send(fail_silently=False)
      messages.success(request, 'Account successfully created')
      return render(request, 'users/login.html')
    else:
      messages.error(request, 'email in use')
      return render(request, 'users/register.html')









class VerficationView(View):
  def get(self, request, uidb64,token): 
    try:
      id=force_str(urlsafe_base64_decode(uidb64))
      user=User.objects.get(pk=id)
      if not token_generator.check_token(user, token):
        return redirect('login'+'?messages'+'User Already Activated You KNOW')
      if user.is_verified:
        return redirect('login'+'?messages'+'User Already Activated')
      user.is_verified = True
      user.save()
      messages.success(request, 'Account Activated Successfully you can login now')
      return redirect('login')
    except Exception as ex:
      pass
    return redirect('login')

class LoginView(View):
  def get(self,request):
    return render(request, 'users/login.html')
  def post(self, request):
    email=request.POST['email']
    password=request.POST['password']

    context={
      'fieldValues' : request.POST
    }
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, 'User with this email does not exist')
        return render(request, 'users/login.html', context)
    if not user.is_verified:
      messages.error(request, 'Account is not verified, please check Your Email')
      return render(request, 'users/login.html', context)
    if not user.is_active:
      messages.error(request, 'Account is not active yet wait for admins to active your account')
      return render(request, 'users/login.html')

    if email and password:
      user=auth.authenticate(email=email, password=password)
      if user:
        if user.is_verified:
          auth.login(request, user)
          messages.success(request, 'Welcome, '+ ' ' + user.last_name + ' You are now logged in')
          return redirect('profile')
        messages.error(request, 'Account is not verified, please check Your Email')
        return render(request, 'users/login.html')
      messages.error(request,'Invalid credentials, Try Again')
      return render(request, 'users/login.html', context)
    messages.error(request,'Please fill all fields')
    return render(request, 'users/login.html', context)


class LogoutView(View):
  def get(self, request):
    # return render(request, 'users/login.html')
    return redirect('login')
  def  post(self, request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect('profile')

# @method_decorator(login_required(login_url='login'), name='dispatch')
# class ProfileView(View):
#   def get(self, request):
#     user = request.user.id
#     posts = Post.objects.filter(seller=user)
#     post_data = []
#     image_urls= []
#     for post in posts:
#         post_images = PostImage.objects.filter(post=post.id)
#         for post_image in post_images :
#           image_urls.append(post_image.image)
          
#         post_data.append({'post': post, 'images': image_urls})

#     context = {'post_data':post_data}
#     return render(request, 'users/profile.html',context)

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    def get(self, request):
        user = request.user
        role = user.role

        if role == "seller":
            return SellerProfileView.as_view()(request)
        elif role == "customer":
            return CustomerProfileView.as_view()(request)
        else:
            return redirect('invester-market')  



@method_decorator(login_required(login_url='login'), name='dispatch')
class SellerProfileView(View):
    def get(self, request):
        user = request.user
        role = user.role
        if role == "seller":
          posts = Post.objects.filter(seller=user)
          post_data = []

          for post in posts:
              post_images = PostImage.objects.filter(post=post)
              image_url = post_images.first().image.url
              post_data.append({'post': post, 'image': image_url})

          context = {'post_data': post_data}
          return render(request, 'users/sellerProfile.html', context)

@method_decorator(login_required(login_url='login'), name='dispatch')
class CustomerProfileView(View):
    def get(self, request):
        user = request.user
        role = user.role
        if role == "customer":
          orders = Order.objects.filter(customer_id=user)
          ordered_posts_data = []

          for order in orders:
              post_images = PostImage.objects.filter(post=order.post)
              image_url = post_images.first().image.url if post_images.exists() else None
              ordered_posts_data.append({'post': order.post, 'image': image_url})
          context = {'ordered_posts': ordered_posts_data}
          return render(request, 'users/customerProfile.html', context)
