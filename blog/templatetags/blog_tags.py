from django import template
from blog.models import Post,Comment
from blog.models import category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog-latest-post.html')
def latestposts():
    posts = Post.objects.filter(status = 1,published_date__lte = timezone.now()).order_by('published_date')[:4]
    return {'posts':posts}


@register.inclusion_tag('blog/blog-post-category.html')
def postcategory():
    posts = Post.objects.filter(status = 1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('website/home-latest-post.html')
def latestposts_home():
    posts = Post.objects.filter(status = 1,published_date__lte = timezone.now()).order_by('published_date')[:6]
    return {'posts':posts}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()