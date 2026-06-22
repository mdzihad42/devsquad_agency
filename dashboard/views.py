from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from .models import VisitorCount, Transaction, SEOData
from devsqaud.models import ContactMessage, Project
from django.contrib import messages

from django.db.models.functions import TruncMonth

# Security: Ensure only staff access
@staff_member_required
def dashboard_home(request):
    total_visits = VisitorCount.objects.aggregate(total=Sum('count'))['total'] or 0
    total_leads = ContactMessage.objects.count()
    
    total_income = Transaction.objects.filter(transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    total_profit = total_income - total_expense
    
    # Chart Data: Last 6 months revenue
    monthly_data = Transaction.objects.filter(transaction_type='INCOME') \
        .annotate(month=TruncMonth('date')) \
        .values('month') \
        .annotate(total=Sum('amount')) \
        .order_by('month')[:6]
    
    chart_labels = [item['month'].strftime('%b') for item in monthly_data]
    chart_values = [float(item['total']) for item in monthly_data]
    
    recent_transactions = Transaction.objects.all()[:5]
    recent_leads = ContactMessage.objects.all()[:5]
    
    context = {
        'total_visits': total_visits,
        'total_leads': total_leads,
        'monthly_revenue': total_income,
        'total_profit': total_profit,
        'recent_transactions': recent_transactions,
        'recent_leads': recent_leads,
        'chart_labels': chart_labels,
        'chart_values': chart_values,
    }
    return render(request, 'dashboard/dashboard_home.html', context)

@staff_member_required
def message_list(request):
    leads = ContactMessage.objects.all()
    return render(request, 'dashboard/message_list.html', {'leads': leads})

@staff_member_required
def message_detail(request, pk):
    message_obj = get_object_or_404(ContactMessage, pk=pk)
    if not message_obj.is_read:
        message_obj.is_read = True
        message_obj.save()
    return render(request, 'dashboard/message_detail.html', {'msg': message_obj})

@staff_member_required
def finance_list(request):
    transactions = Transaction.objects.all()
    total_income = transactions.filter(transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'dashboard/finance_list.html', {
        'transactions': transactions,
        'income': total_income,
        'expense': total_expense,
        'profit': total_income - total_expense
    })

@staff_member_required
def finance_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        t_type = request.POST.get('type')
        date = request.POST.get('date')
        
        Transaction.objects.create(
            title=title,
            amount=amount,
            category=category,
            transaction_type=t_type,
            date=date
        )
        messages.success(request, "Transaction added successfully!")
        return redirect('dashboard_finances')
    return render(request, 'dashboard/finance_form.html')

@staff_member_required
def seo_list(request):
    seo_items = SEOData.objects.all()
    return render(request, 'dashboard/seo_list.html', {'seo_items': seo_items})

@staff_member_required
def seo_add(request):
    if request.method == 'POST':
        page_url = request.POST.get('page_url')
        title_tag = request.POST.get('title_tag')
        meta_description = request.POST.get('meta_description')
        keywords = request.POST.get('keywords')
        
        SEOData.objects.create(
            page_url=page_url,
            title_tag=title_tag,
            meta_description=meta_description,
            keywords=keywords
        )
        messages.success(request, f"SEO config for {page_url} created!")
        return redirect('dashboard_seo')
    return render(request, 'dashboard/seo_form.html', {'is_add': True})


@staff_member_required
def seo_edit(request, pk):
    seo = get_object_or_404(SEOData, pk=pk)
    if request.method == 'POST':
        seo.title_tag = request.POST.get('title_tag')
        seo.meta_description = request.POST.get('meta_description')
        seo.keywords = request.POST.get('keywords')
        seo.save()
        messages.success(request, f"SEO for {seo.page_url} updated!")
        return redirect('dashboard_seo')
    return render(request, 'dashboard/seo_form.html', {'seo': seo})

@staff_member_required
def portfolio_list(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/portfolio_list.html', {'projects': projects})
