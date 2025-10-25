from django.db import models
from django.utils.text import slugify
from django.utils.safestring import mark_safe
import markdown
import bleach


class BlogPost(models.Model):
    """Model for blog posts with markdown support."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def tag_list(self):
        """Return tags as a list."""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []

    @property
    def rendered_content(self):
        """Return sanitized HTML rendered from Markdown content.

        Uses python-markdown to convert Markdown to HTML and bleach to sanitize
        the resulting HTML to prevent XSS. The returned value is marked safe
        because it has been sanitized.
        """
        # Convert markdown to HTML
        html = markdown.markdown(
            self.content or "",
            extensions=[
                "extra",  # tables, fenced_code, etc.
            ],
            output_format="html5",
        )

        # Define sanitization policy
        allowed_tags = [
            "p", "pre", "code", "blockquote", "hr",
            "ul", "ol", "li",
            "strong", "em", "b", "i", "u", "s",
            "a", "h1", "h2", "h3", "h4", "h5", "h6",
        ]
        allowed_attributes = {
            "a": ["href", "title", "rel"],
        }
        allowed_protocols = ["http", "https", "mailto"]

        cleaned = bleach.clean(
            html,
            tags=allowed_tags,
            attributes=allowed_attributes,
            protocols=allowed_protocols,
            strip=True,
        )
        return mark_safe(cleaned)