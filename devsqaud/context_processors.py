from .models import SiteConfig


def site_config_context(request):
    """Make SiteConfig available globally in all templates."""
    return {
        'site': SiteConfig.load(),
    }


def currency_context(request):
    """Expose the active currency code and symbol globally."""
    currency = request.session.get('currency', 'USD')
    symbols = {
        'USD': '$',
        'BDT': '৳',
        'EUR': '€',
        'GBP': '£',
        'SAR': '﷼',
        'AED': 'د.إ'
    }
    return {
        'active_currency': currency,
        'currency_symbol': symbols.get(currency, '$'),
    }
