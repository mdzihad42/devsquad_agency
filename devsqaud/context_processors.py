from .models import SiteConfig


def site_config_context(request):
    """Make SiteConfig available globally in all templates."""
    return {
        'site': SiteConfig.load(),
    }
