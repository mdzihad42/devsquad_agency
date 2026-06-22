from .models import SEOData

def seo_context(request):
    path = request.path
    try:
        seo = SEOData.objects.get(page_url=path)
        return {
            'seo_title': seo.title_tag,
            'seo_description': seo.meta_description,
            'seo_keywords': seo.keywords,
            'og_title': seo.og_title or seo.title_tag,
            'og_description': seo.og_description or seo.meta_description,
            'og_image': seo.og_image,
        }
    except SEOData.DoesNotExist:
        # Defaults if no specific SEO data exists
        return {
            'seo_title': "Mzify — Premium Digital Agency",
            'seo_description': "Mzify builds high-performance websites and web applications with Django and WordPress.",
            'seo_keywords': "digital agency, web development, django, wordpress",
        }
