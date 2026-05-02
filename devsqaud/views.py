from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service, Project, Testimonial, SiteConfig
from .forms import ContactForm


def home_view(request):
    """Home page with featured content."""
    context = {
        'services': Service.objects.filter(is_featured=True)[:4],
        'projects': Project.objects.filter(is_featured=True)[:3],
        'testimonials': Testimonial.objects.filter(is_featured=True)[:3],
    }
    return render(request, 'home.html', context)


def services_view(request):
    """All services page."""
    context = {
        'services': Service.objects.all(),
    }
    return render(request, 'services.html', context)


def portfolio_view(request):
    """Portfolio page with all projects."""
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio.html', context)


def project_detail_view(request, slug):
    """Single project detail page."""
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)


def about_view(request):
    """About page."""
    return render(request, 'about.html')


def contact_view(request):
    """Contact page with form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully. We\'ll get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
