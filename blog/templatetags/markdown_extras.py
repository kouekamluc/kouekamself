"""
Custom template tags for markdown rendering.
"""
from django import template
from django.utils.safestring import mark_safe
import markdown
import bleach

register = template.Library()


# Allowed HTML tags and attributes for bleach
ALLOWED_TAGS = [
    'p', 'br', 'strong', 'em', 'u', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'blockquote', 'code', 'pre', 'hr', 'div', 'span', 'ul', 'ol', 'li',
    'a', 'img', 'table', 'thead', 'tbody', 'tr', 'th', 'td'
]

ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'target', 'rel'],
    'img': ['src', 'alt', 'title', 'width', 'height'],
    'code': ['class'],
    'pre': ['class'],
    'div': ['class'],
    'span': ['class'],
}


@register.filter(name='markdown')
def markdown_filter(text):
    """
    Convert markdown text to HTML with security sanitization.
    
    Usage in templates:
        {{ post.content|markdown }}
    """
    if not text:
        return ''
    
    # Convert markdown to HTML
    html = markdown.markdown(
        text,
        extensions=[
            'markdown.extensions.fenced_code',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
            'markdown.extensions.nl2br',
            'markdown.extensions.sane_lists',
        ]
    )
    
    # Sanitize HTML to prevent XSS attacks
    clean_html = bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        strip=True
    )
    
    # Mark as safe for Django template rendering
    return mark_safe(clean_html)


@register.filter(name='truncate_markdown')
def truncate_markdown(text, length=100):
    """
    Truncate markdown text to specified length and convert to HTML.
    
    Usage in templates:
        {{ post.content|truncate_markdown:150 }}
    """
    if not text:
        return ''
    
    # Truncate text
    if len(text) > length:
        text = text[:length] + '...'
    
    # Convert to HTML
    return markdown_filter(text)
