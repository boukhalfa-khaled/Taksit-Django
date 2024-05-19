from django.db import models
from users.models import User
from django.utils.timezone import now

# Create your models here.



class Category(models.Model):
  name = models.CharField(max_length=255)

  class Meta:
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name

class Post(models.Model):
  PENDING = 'pending'
  PAID = 'paid'
  UNPAID = 'unpaid'
  STATU_CHOICES = [
    (PENDING, 'Pending'),
    (PAID, 'Paid'),
    (UNPAID, 'Unpaid'),
  ]


  title = models.CharField(255)
  description = models.TextField()
  seller = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="seller")
  category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
  price = models.CharField(255, null=True)
  months = models.CharField(255, null=True)
  wilaya = models.CharField(255, null=False, default='djelfa')
  is_cash= models.BooleanField(default=False)
  status = models.CharField(max_length=20, choices=STATU_CHOICES, default=PENDING,)
  created_at = models.DateTimeField(auto_now_add=True )
  update_at  = models.DateTimeField(auto_now=True)


  investor = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='invester')
  customer_id = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='order')




  def __str__(self):
    return self.title

class Order(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_Orderd')
  customer_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, related_name='customer')


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    image = models.FileField(upload_to='post_images/', null=True)

    def __str__(self):
        return f"Image for {self.post.title}"




