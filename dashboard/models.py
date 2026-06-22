from django.db import models

class VisitorCount(models.Model):
    page_path = models.CharField(max_length=255, unique=True)
    count = models.PositiveIntegerField(default=0)
    last_visit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.page_path} - {self.count} views"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.transaction_type}: {self.title} - {self.amount}"

class SEOData(models.Model):
    page_url = models.CharField(max_length=255, unique=True, help_text="Relative URL, e.g., '/' or '/services/'")
    title_tag = models.CharField(max_length=200)
    meta_description = models.TextField()
    keywords = models.CharField(max_length=255, blank=True)
    og_title = models.CharField(max_length=200, blank=True)
    og_description = models.TextField(blank=True)
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True)

    def __str__(self):
        return self.page_url
