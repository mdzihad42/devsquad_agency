from .models import VisitorCount
from django.db.models import F

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Track only GET requests to non-admin and non-static pages
        if request.method == 'GET' and not request.path.startswith(('/admin/', '/static/', '/media/', '/dashboard/')):
            visit, created = VisitorCount.objects.get_or_create(page_path=request.path)
            VisitorCount.objects.filter(page_path=request.path).update(count=F('count') + 1)

        return response
