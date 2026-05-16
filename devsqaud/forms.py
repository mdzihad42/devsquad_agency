from django import forms
from .models import ContactMessage, Project, Post, Service, Testimonial, TeamMember, ClientLogo, Package

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about your project...', 'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 5}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'image', 'short_description', 'full_description', 'tech_stack', 'result_highlight', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'slug': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'short_description': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'result_highlight': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'tech_stack': forms.TextInput(attrs={'placeholder': 'Python, Django, Tailwind', 'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'full_description': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 5}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'icon', 'thumbnail', 'external_thumbnail', 'excerpt', 'content', 'author', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'slug': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'icon': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'author': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'external_thumbnail': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'category': forms.Select(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'excerpt': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 3}),
            'content': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 10}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'icon', 'image', 'short_description', 'full_description', 'problem', 'solution', 'benefits', 'is_featured', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'icon': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'short_description': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'full_description': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 4}),
            'problem': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 4}),
            'solution': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 4}),
            'benefits': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_role', 'feedback', 'is_featured', 'order']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'client_role': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'feedback': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
        }

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'image', 'bio', 'order', 'linkedin', 'twitter']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'role': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'bio': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 4}),
            'linkedin': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'twitter': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'order': forms.NumberInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
        }

class ClientLogoForm(forms.ModelForm):
    class Meta:
        model = ClientLogo
        fields = ['name', 'logo', 'is_active', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'order': forms.NumberInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
        }

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'display_name', 'icon', 'price', 'short_description', 'is_featured', 'order']
        widgets = {
            'name': forms.Select(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'display_name': forms.TextInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'icon': forms.TextInput(attrs={'placeholder': 'fas fa-cube', 'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'price': forms.TextInput(attrs={'placeholder': '$2,500', 'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
            'short_description': forms.Textarea(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all', 'rows': 3}),
            'order': forms.NumberInput(attrs={'class': 'w-full bg-black-pure border border-white/10 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-sunset-orange/50 transition-all'}),
        }
