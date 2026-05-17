from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Service, Project, Testimonial, SiteConfig, ClientLogo, TeamMember, Post, Category, Package, FAQ
from .forms import ContactForm


def home_view(request):
    """Home page with featured content."""
    services = Service.objects.all().order_by('order')
    projects = Project.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all().order_by('order')
    latest_posts = Post.objects.filter(is_published=True)[:3]
    client_logos = ClientLogo.objects.all()
    config = SiteConfig.load()
    
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'faqs': faqs,
        'latest_posts': latest_posts,
        'client_logos': client_logos,
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
    """Portfolio page with all projects, separated by featured and recent."""
    featured_projects = Project.objects.filter(is_featured=True)
    recent_projects = Project.objects.filter(is_featured=False)
    testimonials = Testimonial.objects.all()
    context = {
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
        'testimonials': testimonials,
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
    """Blog list page with category filtering and keyword search."""
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search')
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    active_category = None

    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=active_category)

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(excerpt__icontains=search_query) | 
            Q(content__icontains=search_query)
        )

    # Separate latest post as the Featured Post if no search or category filters are active
    featured_post = None
    if not category_slug and not search_query:
        featured_post = posts.first()
        if featured_post:
            posts = posts.exclude(id=featured_post.id)

    context = {
        'featured_post': featured_post,
        'posts': posts,
        'categories': Category.objects.all(),
        'active_category': active_category,
        'search_query': search_query,
    }
    return render(request, 'blog/post_list.html', context)


def blog_detail_view(request, slug):
    """Blog detail page with related posts recommended."""
    post = get_object_or_404(Post, slug=slug, is_published=True)
    related_posts = Post.objects.filter(category=post.category, is_published=True).exclude(id=post.id)[:3]
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)


def contact_view(request):
    """Contact page with form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract extra fields from POST request
            company = request.POST.get('company', '').strip()
            service = request.POST.get('service', '').strip()
            budget = request.POST.get('budget', '').strip()

            contact_msg = form.save(commit=False)

            # Build enriched metadata details
            extra_info = []
            if company:
                extra_info.append(f"Company: {company}")
            if service:
                extra_info.append(f"Service Needed: {service}")
            if budget:
                extra_info.append(f"Budget Range: {budget}")

            if extra_info:
                contact_msg.message = f"{contact_msg.message}\n\n---\n[Form Metadata]\n" + "\n".join(extra_info)

            contact_msg.save()
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
