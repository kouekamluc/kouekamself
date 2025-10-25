from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost


def blog_list(request):
    """List view for blog posts with pagination."""
    posts = BlogPost.objects.filter(published=True)
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'posts': page_obj,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Detail view for individual blog posts."""
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    
    # Get related posts (same tags)
    related_posts = BlogPost.objects.filter(
        published=True,
        tags__in=post.tag_list
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/blog_detail.html', context)