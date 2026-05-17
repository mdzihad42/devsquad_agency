from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Service, Project, Testimonial, SiteConfig, ContactMessage, Post, TeamMember, Category, ClientLogo, Package, FAQ, NewsletterSubscriber
from .forms import (
    ContactForm, ProjectForm, PostForm, ServiceForm, 
    TestimonialForm, TeamMemberForm, ClientLogoForm, PackageForm, FAQForm
)
from django.urls import reverse

# Model to Form Mapping
MODEL_MAP = {
    'project': (Project, ProjectForm, 'dashboard_projects', 'Project'),
    'post': (Post, PostForm, 'dashboard_blog', 'Blog Post'),
    'service': (Service, ServiceForm, 'dashboard_services', 'Service'),
    'testimonial': (Testimonial, TestimonialForm, 'dashboard_testimonials', 'Testimonial'),
    'team': (TeamMember, TeamMemberForm, 'dashboard_team', 'Team Member'),
    'logo': (ClientLogo, ClientLogoForm, 'dashboard_logos', 'Client Logo'),
    'package': (Package, PackageForm, 'dashboard_packages', 'Pricing Package'),
    'faq': (FAQ, FAQForm, 'dashboard_faq', 'FAQ'),
    'subscriber': (NewsletterSubscriber, None, 'dashboard_subscribers', 'Newsletter Subscriber'),
}

@staff_member_required
def content_create_edit(request, model_key, pk=None):
    """Unified view for creating and editing all agency content."""
    if model_key not in MODEL_MAP:
        return redirect('dashboard_home')
        
    model_class, form_class, list_url_name, display_name = MODEL_MAP[model_key]
    instance = get_object_or_404(model_class, pk=pk) if pk else None
    
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, f'{display_name} saved successfully!')
            return redirect(list_url_name)
    else:
        form = form_class(instance=instance)
        
    context = {
        'form': form,
        'title': f"{'Edit' if pk else 'Add New'} {display_name}",
        'back_url': reverse(list_url_name),
        'active_page': model_key if model_key in ['projects', 'blog', 'services', 'testimonials', 'team', 'logos'] else 'overview',
    }
    return render(request, 'dashboard/content_form.html', context)

@staff_member_required
def content_delete(request, model_key, pk):
    """Unified view for deleting agency content."""
    if model_key not in MODEL_MAP:
        return redirect('dashboard_home')
        
    model_class, _, list_url_name, display_name = MODEL_MAP[model_key]
    instance = get_object_or_404(model_class, pk=pk)
    
    if request.method == 'POST':
        instance.delete()
        messages.success(request, f'{display_name} deleted successfully.')
        return redirect(list_url_name)
    
    # If GET, show a confirmation or just redirect back (usually we want a post request for delete)
    return redirect(list_url_name)

@staff_member_required
def dashboard_home(request):
    """Main dashboard overview."""
    context = {
        'total_projects': Project.objects.count(),
        'total_posts': Post.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
        'latest_messages': ContactMessage.objects.all()[:5],
        'total_services': Service.objects.count(),
        'active_page': 'overview',
    }
    return render(request, 'dashboard/home.html', context)

@staff_member_required
def dashboard_messages(request):
    """View and manage contact messages."""
    messages_list = ContactMessage.objects.all()
    context = {
        'contact_messages': messages_list,
        'active_page': 'messages',
    }
    return render(request, 'dashboard/messages.html', context)

@staff_member_required
def message_detail(request, pk):
    """Detail view of a message, marks it as read."""
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.is_read = True
    msg.save()
    context = {
        'message': msg,
        'active_page': 'messages',
    }
    return render(request, 'dashboard/message_detail.html', context)

@staff_member_required
def dashboard_projects(request):
    """List projects in dashboard."""
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'active_page': 'projects',
    }
    return render(request, 'dashboard/projects_list.html', context)

@staff_member_required
def dashboard_blog(request):
    """List blog posts in dashboard."""
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'active_page': 'blog',
    }
    return render(request, 'dashboard/blog_list.html', context)

@staff_member_required
def dashboard_services(request):
    """List services in dashboard."""
    services = Service.objects.all()
    context = {
        'services': services,
        'active_page': 'services',
    }
    return render(request, 'dashboard/services_list.html', context)

@staff_member_required
def dashboard_testimonials(request):
    """List testimonials in dashboard."""
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials,
        'active_page': 'testimonials',
    }
    return render(request, 'dashboard/testimonials_list.html', context)

@staff_member_required
def dashboard_team(request):
    """List team members in dashboard."""
    team = TeamMember.objects.all()
    context = {
        'team': team,
        'active_page': 'team',
    }
    return render(request, 'dashboard/team_list.html', context)

@staff_member_required
def dashboard_logos(request):
    """List client logos in dashboard."""
    logos = ClientLogo.objects.all()
    context = {
        'logos': logos,
        'active_page': 'logos',
    }
    return render(request, 'dashboard/logos_list.html', context)

@staff_member_required
def dashboard_packages(request):
    """List pricing packages in dashboard."""
    packages = Package.objects.all()
    context = {
        'packages': packages,
        'active_page': 'packages',
    }
    return render(request, 'dashboard/packages_list.html', context)

@staff_member_required
def dashboard_faq(request):
    """List FAQs in dashboard."""
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
        'active_page': 'faq',
    }
    return render(request, 'dashboard/faq_list.html', context)

@staff_member_required
def dashboard_subscribers(request):
    """List newsletter subscribers in dashboard."""
    subscribers = NewsletterSubscriber.objects.all().order_by('-created_at')
    context = {
        'subscribers': subscribers,
        'active_page': 'subscribers',
    }
    return render(request, 'dashboard/subscribers_list.html', context)

@staff_member_required
def dashboard_settings(request):
    """Update SiteConfig including Social Icons."""
    config = SiteConfig.load()
    if request.method == 'POST':
        # Main Info
        config.hero_headline = request.POST.get('hero_headline')
        config.hero_subheading = request.POST.get('hero_subheading')
        config.contact_email = request.POST.get('contact_email')
        config.whatsapp_number = request.POST.get('whatsapp_number')
        
        # Social Icons
        config.social_facebook = request.POST.get('social_facebook')
        config.social_twitter = request.POST.get('social_twitter')
        config.social_linkedin = request.POST.get('social_linkedin')
        config.social_github = request.POST.get('social_github')

        # About Details
        config.about_intro = request.POST.get('about_intro')
        config.about_mission = request.POST.get('about_mission')
        config.about_vision = request.POST.get('about_vision')
        
        # Stats
        config.stat_projects = request.POST.get('stat_projects', 150)
        config.stat_experience = request.POST.get('stat_experience', 10)
        config.stat_clients = request.POST.get('stat_clients', 98)
        
        config.save()
        messages.success(request, 'Site settings updated successfully!')
        return redirect('dashboard_settings')
        
    context = {
        'config': config,
        'active_page': 'settings',
    }
    return render(request, 'dashboard/settings.html', context)
