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


import random

def contact_view(request):
    """Contact page with form and secure anti-bot Math Captcha."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        # Verify Captcha
        user_answer = request.POST.get('captcha_input', '').strip()
        actual_answer = request.session.get('captcha_answer')
        
        if not user_answer or actual_answer is None or str(user_answer) != str(actual_answer):
            messages.error(request, 'Security verification failed! Please solve the math puzzle again.')
            # Generate new captcha and preserve form inputs
            num1 = random.randint(1, 9)
            num2 = random.randint(2, 9)
            request.session['captcha_answer'] = num1 + num2
            context = {
                'form': form,
                'num1': num1,
                'num2': num2,
                # Keep fields entered
                'selected_company': request.POST.get('company', '').strip(),
                'selected_service': request.POST.get('service', '').strip(),
                'selected_budget': request.POST.get('budget', '').strip(),
            }
            return render(request, 'contact.html', context)

        if form.is_valid():
            # Clear session captcha on success to prevent reuse
            request.session['captcha_answer'] = None
            
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
        
    # Generate Math Captcha numbers
    num1 = random.randint(1, 9)
    num2 = random.randint(2, 9)
    request.session['captcha_answer'] = num1 + num2

    context = {
        'form': form,
        'num1': num1,
        'num2': num2,
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


from django.http import HttpResponse
from django.urls import reverse

def sitemap_view(request):
    """Dynamic XML sitemap generator."""
    host = f"{request.scheme}://{request.get_host()}"
    
    # Static pages list
    static_urls = [
        reverse('home'),
        reverse('services'),
        reverse('portfolio'),
        reverse('about'),
        reverse('team'),
        reverse('contact'),
        reverse('pricing'),
        reverse('blog_list'),
        reverse('privacy'),
        reverse('terms'),
    ]
    
    xml_items = []
    
    # 1. Add static pages
    for url in static_urls:
        xml_items.append(f"  <url>\n    <loc>{host}{url}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>")
        
    # 2. Add Projects
    for project in Project.objects.all():
        loc = f"{host}{reverse('project_detail', args=[project.slug])}"
        xml_items.append(f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>")
        
    # 3. Add Blog Posts
    for post in Post.objects.filter(is_published=True):
        loc = f"{host}{reverse('blog_detail', args=[post.slug])}"
        # Format updated time
        updated = post.updated_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
        xml_items.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{updated}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>")

    xml_content = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(xml_items) + '\n</urlset>'

    return HttpResponse(xml_content, content_type="application/xml")


def robots_view(request):
    """Serve robots.txt dynamically."""
    host = f"{request.scheme}://{request.get_host()}"
    content = f"User-agent: *\nAllow: /\nDisallow: /management/\nDisallow: /logout/\n\nSitemap: {host}/sitemap.xml\n"
    return HttpResponse(content, content_type="text/plain")
