import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsqaud_project.settings')
django.setup()

from devsqaud.models import Service, Project, Post

# Source directory containing the premium generated assets
brain_dir = r"C:\Users\USER\.gemini\antigravity\brain\dc23d95a-cbae-4855-a39e-7af031b5cb33"

# Destination directories inside media
media_services_dir = os.path.join("media", "services")
media_projects_dir = os.path.join("media", "projects")
media_blog_dir = os.path.join("media", "blog")

os.makedirs(media_services_dir, exist_ok=True)
os.makedirs(media_projects_dir, exist_ok=True)
os.makedirs(media_blog_dir, exist_ok=True)

print("Copying premium visuals from artifacts...")

def copy_file(src_filename, dest_path):
    src_path = os.path.join(brain_dir, src_filename)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"  - Copied {src_filename} to {dest_path}")
        return True
    else:
        print(f"  - WARNING: Source file {src_path} not found.")
        return False

# 1. Services Mockups
copy_file("service_web_dev_v2_1778922960664.png", os.path.join(media_services_dir, "web_dev.png"))
copy_file("service_app_dev_v1_1778927792027.png", os.path.join(media_services_dir, "app_dev.png"))
copy_file("service_uiux_v2_1778922978059.png", os.path.join(media_services_dir, "uiux.png"))
copy_file("service_cloud_v2_1778922991023.png", os.path.join(media_services_dir, "cloud.png"))
copy_file("service_graphics_v1_1778927809505.png", os.path.join(media_services_dir, "graphics.png"))

# 2. Projects Mockups
copy_file("media__1778932420148.png", os.path.join(media_projects_dir, "project_fintech.png"))
copy_file("media__1778939032737.png", os.path.join(media_projects_dir, "project_analytics.png"))
copy_file("blog_thumb_tech_v1_1778932108525.png", os.path.join(media_projects_dir, "project_ecommerce.png"))

# 3. Blog Mockups
copy_file("blog_thumb_tech_v1_1778932108525.png", os.path.join(media_blog_dir, "blog_tech_trends.png"))
copy_file("about_workspace_mockup_1778997751515.png", os.path.join(media_blog_dir, "blog_architecture.png"))
copy_file("web_dev_hero_v2_1778922943016.png", os.path.join(media_blog_dir, "blog_design_psychology.png"))

print("\nUpdating Database Fields...")

# 1. Update Services
web_dev = Service.objects.filter(title__icontains="Web Development").first()
if web_dev:
    web_dev.image = "services/web_dev.png"
    web_dev.save()
    print("  - Updated Custom Web Development image")

app_dev = Service.objects.filter(title__icontains="App Development").first()
if app_dev:
    app_dev.image = "services/app_dev.png"
    app_dev.save()
    print("  - Updated Premium App Development image")

graphics = Service.objects.filter(title__icontains="Graphics").first()
if graphics:
    graphics.image = "services/graphics.png"
    graphics.save()
    print("  - Updated Graphics Design image")

# 2. Update Projects with Premium Mockups
projects = list(Project.objects.all())
mockup_project_images = [
    "projects/project_ecommerce.png",
    "projects/project_analytics.png",
    "projects/project_fintech.png"
]

for i, p in enumerate(projects):
    p.image = mockup_project_images[i % len(mockup_project_images)]
    p.save()
    print(f"  - Assigned image '{p.image}' to Project: '{p.title}'")

# 3. Update Blog Posts with Local Premium Images
posts = list(Post.objects.all())
mockup_blog_images = [
    "blog/blog_tech_trends.png",
    "blog/blog_architecture.png",
    "blog/blog_design_psychology.png"
]

for i, post in enumerate(posts):
    post.thumbnail = mockup_blog_images[i % len(mockup_blog_images)]
    post.external_thumbnail = ""  # Clear external URL to prioritize local high-res image
    post.save()
    print(f"  - Assigned image '{post.thumbnail}' to Blog Post: '{post.title}'")

print("\nDatabase update completed successfully!")
