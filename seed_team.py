import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsqaud_project.settings')
django.setup()

from devsqaud.models import TeamMember

print("Seeding premium team member profiles...")

# Clear existing team members to avoid duplicates
TeamMember.objects.all().delete()

# Seed Founder and Collaborator
team_data = [
    {
        "name": "Zihad",
        "role": "Founder & Lead Engineer",
        "bio": "Full-stack architect with over 6 years of experience building scalable web apps. Specializes in Django, React, Cloud Automation, and high-performance databases.",
        "linkedin": "https://linkedin.com/",
        "twitter": "https://twitter.com/",
        "order": 1
    },
    {
        "name": "Alex Mercer",
        "role": "Senior UI/UX & Brand Designer",
        "bio": "Collaborating expert. Crafting user-focused interface designs and high-conversion landing pages for over 5 years. Focuses on premium glassmorphic styling and responsive frames.",
        "linkedin": "https://linkedin.com/",
        "twitter": "https://twitter.com/",
        "order": 2
    },
    {
        "name": "Sarah Chen",
        "role": "SEO Specialist & Technical Copywriter",
        "bio": "Collaborating expert. Optimizing platforms to rank page-one on Google. Analyzes indexing schemas and engineers long-form content conversion matrices.",
        "linkedin": "https://linkedin.com/",
        "twitter": "https://twitter.com/",
        "order": 3
    }
]

for member in team_data:
    tm = TeamMember.objects.create(
        name=member["name"],
        role=member["role"],
        bio=member["bio"],
        linkedin=member["linkedin"],
        twitter=member["twitter"],
        order=member["order"]
    )
    print(f"Seeded Team Member: {tm.name} — {tm.role}")

print("Seeding team successfully complete!")
