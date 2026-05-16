from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service, Project, Testimonial, SiteConfig, ClientLogo, TeamMember, Post, Category, Package, FAQ
from .forms import ContactForm


def home_view(request):
    """Home page with featured content."""
    services = Service.objects.all().order_by('order')
    projects = Project.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all().order_by('order')
    config = SiteConfig.load()
    
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'faqs': faqs,
        'config': config,
    }
    return render(request, 'home.html', context)


def pricing(request):
    """Public pricing page."""
    packages = Package.objects.all()
    faqs = FAQ.objects.all().order_by('order')
    context = {
        'packages': packages,
        'faqs': faqs,
    }
    return render(request, 'pricing.html', context)

def team_view(request):
    """Public team members page."""
    team = TeamMember.objects.all()
    context = {
        'team': team,
    }
    return render(request, 'team.html', context)


def services_view(request):
    """All services page."""
    services = Service.objects.all().order_by('order')
    context = {
        'services': services,
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
    context = {
        'team_members': TeamMember.objects.all(),
    }
    return render(request, 'about.html', context)


def blog_list_view(request):
    """Blog list page with category filtering."""
    category_slug = request.GET.get('category')
    posts = Post.objects.filter(is_published=True)
    active_category = None

    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=active_category)

    context = {
        'posts': posts,
        'categories': Category.objects.all(),
        'active_category': active_category,
    }
    return render(request, 'blog/post_list.html', context)


def blog_detail_view(request, slug):
    """Blog detail page."""
    post = get_object_or_404(Post, slug=slug, is_published=True)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


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


def subscribe(request):
    """Handle newsletter subscription via POST."""
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
            messages.success(request, "Thanks for subscribing! We'll keep you updated.")
        else:
            messages.error(request, "Please provide a valid email address.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def privacy_view(request):
    """Static privacy policy page."""
    return render(request, 'legal/privacy.html')

def terms_view(request):
    """Static terms of service page."""
    return render(request, 'legal/terms.html')
