from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    """Services offered by the agency."""
    icon = models.CharField(
        max_length=100,
        help_text="Font Awesome icon class, e.g. 'fas fa-code'"
    )
    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
        help_text="Service card image (optional)"
    )
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    problem = models.TextField(blank=True, help_text="Problem statement for detail view")
    solution = models.TextField(blank=True, help_text="Solution description for detail view")
    benefits = models.TextField(blank=True, help_text="Key benefits, one per line")
    is_featured = models.BooleanField(default=False, help_text="Show on home page")
    order = models.IntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Project(models.Model):
    """Portfolio projects."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    result_highlight = models.CharField(
        max_length=300,
        help_text="e.g. '3x revenue increase'"
    )
    tech_stack = models.CharField(
        max_length=500,
        help_text="Comma-separated technologies"
    )
    is_featured = models.BooleanField(default=False, help_text="Show on home page")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_tech_list(self):
        """Return tech stack as a list."""
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Testimonial(models.Model):
    """Client testimonials."""
    client_name = models.CharField(max_length=100)
    client_role = models.CharField(max_length=200, help_text="e.g. 'CEO, TechCorp'")
    feedback = models.TextField()
    is_featured = models.BooleanField(default=False, help_text="Show on home page")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.client_name} — {self.client_role}"


class ContactMessage(models.Model):
    """Contact form submissions."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.email} ({self.created_at:%Y-%m-%d})"


class SiteConfig(models.Model):
    """Singleton site-wide configuration."""
    # Hero
    hero_headline = models.CharField(max_length=300, default="We Build Scalable Digital Products")
    hero_subheading = models.TextField(default="Transforming ideas into high-performance digital experiences that drive growth.")
    # About
    about_intro = models.TextField(default="We are a team of passionate developers and designers.")
    about_mission = models.TextField(default="To deliver world-class digital solutions.")
    about_vision = models.TextField(default="To be the most trusted digital partner globally.")
    # Stats
    stat_projects = models.CharField(max_length=50, default="50+")
    stat_experience = models.CharField(max_length=50, default="3+")
    stat_clients = models.CharField(max_length=50, default="40+")
    # Contact
    contact_email = models.EmailField(default="hello@devsquad.com")
    contact_phone = models.CharField(max_length=20, blank=True, default="+880 1234 567890")
    whatsapp_number = models.CharField(
        max_length=20,
        default="8801234567890",
        help_text="WhatsApp number without + sign"
    )
    # Footer
    footer_text = models.CharField(max_length=300, default="© 2026 DevSquad. All rights reserved.")
    # Social
    social_facebook = models.URLField(blank=True)
    social_twitter = models.URLField(blank=True)
    social_linkedin = models.URLField(blank=True)
    social_github = models.URLField(blank=True)

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return "Site Configuration"

    def save(self, *args, **kwargs):
        # Enforce singleton — always use pk=1
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        """Load or create the singleton config."""
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Category(models.Model):
    """Blog categories."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    """Blog posts."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100, default="DevSquad Team")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    icon = models.CharField(max_length=100, default="fas fa-newspaper", help_text="Font Awesome icon for the post")
    thumbnail = models.ImageField(upload_to='blog/', blank=True, null=True)
    external_thumbnail = models.URLField(blank=True, help_text="Link to external image (e.g. Unsplash)")
    excerpt = models.TextField(help_text="Short summary of the post")
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ClientLogo(models.Model):
    """Client logos for the trust bar."""
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/', help_text="Monochrome white version recommended")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    """Agency team members."""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    bio = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} — {self.role}"
