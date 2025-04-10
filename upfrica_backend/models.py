from django.db import models
from django.utils.text import slugify

class HelpCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class HelpArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Auto-generate if blank
    date = models.DateTimeField(auto_now_add=True)
    lastmod = models.DateTimeField(auto_now=True)

    tags = models.CharField(max_length=250, blank=True, help_text="Comma-separated tags")
    is_published = models.BooleanField(default=True)

    summary = models.TextField(blank=True, help_text="Short summary or meta description")
    body = models.TextField(help_text="Full article content")

    images = models.JSONField(blank=True, null=True, help_text="List of image URLs (stored as JSON)")
    tips = models.TextField(blank=True, help_text="Optional tips section")
    note = models.TextField(blank=True, help_text="Optional footnotes or extra info")

    category = models.ForeignKey(
        HelpCategory, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='articles', help_text="Category this article belongs to"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:60]  # Trim for safety
            slug = base_slug
            num = 1
            while HelpArticle.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title