from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost
import markdown
import bleach


def render_markdown_to_safe_html(markdown_text: str) -> str:
    """Render Markdown to sanitized HTML to prevent XSS.

    Allows a conservative subset of HTML tags suitable for blog content.
    """
    if not markdown_text:
        return ""

    # Render Markdown to HTML
    rendered_html = markdown.markdown(
        markdown_text,
        extensions=[
            "fenced_code",
            "tables",
            "sane_lists",
            "toc",  # generates anchors for headings (safe after cleaning)
        ],
        output_format="html5",
    )

    # Sanitize HTML
    allowed_tags = [
        "p",
        "br",
        "hr",
        "pre",
        "code",
        "blockquote",
        "ul",
        "ol",
        "li",
        "em",
        "strong",
        "a",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "table",
        "thead",
        "tbody",
        "tr",
        "th",
        "td",
    ]
    allowed_attributes = {
        "a": ["href", "title", "rel"],
        "code": ["class"],
        "th": ["colspan", "rowspan"],
        "td": ["colspan", "rowspan"],
    }
    cleaned_html = bleach.clean(
        rendered_html,
        tags=allowed_tags,
        attributes=allowed_attributes,
        strip=True,
    )

    # Auto-link plain URLs safely
    linked_html = bleach.linkify(cleaned_html, skip_pre=True)

    return linked_html


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
    
    rendered_content = render_markdown_to_safe_html(post.content)

    context = {
        'post': post,
        'related_posts': related_posts,
        'rendered_content': rendered_content,
    }
    return render(request, 'blog/blog_detail.html', context)