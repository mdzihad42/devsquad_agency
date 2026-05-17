from django import template

register = template.Library()

@register.filter
def convert_currency(amount, request):
    """Converts price dynamically based on session currency, stripping non-numeric chars."""
    if not amount:
        return ""
    
    amount_str = str(amount).replace('$', '').replace(',', '').strip()
    
    # Try to parse the numeric amount
    try:
        val = float(amount_str)
    except ValueError:
        # If it's "Custom" or non-numeric, return as-is
        return amount
        
    currency = request.session.get('currency', 'USD')
    
    # Dynamic exchange rates mapping
    rates = {
        'USD': 1.0,
        'BDT': 117.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'SAR': 3.75,
        'AED': 3.67
    }
    
    symbols = {
        'USD': '$',
        'BDT': '৳',
        'EUR': '€',
        'GBP': '£',
        'SAR': '﷼',
        'AED': 'د.إ'
    }
    
    multiplier = rates.get(currency, 1.0)
    symbol = symbols.get(currency, '$')
    
    converted = val * multiplier
    
    # Format cleanly with thousands separator and prepend active symbol
    return f"{symbol}{converted:,.0f}"
