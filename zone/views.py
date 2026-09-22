from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
    banners = HomeBanner.objects.filter(is_active=True).order_by('sequence')

    home_about = HomeAboutSection.objects.filter(is_active=True).order_by('-created_at').first()
    why_choose = WhyChooseUsSection.objects.filter(is_active=True).order_by('-created_at').first()
    services = HomeService.objects.filter(is_active=True).order_by('-created_at')
    projects = HomeProject.objects.filter(is_active=True).order_by('-created_at')
    partners = HomeOutPartner.objects.filter(is_active=True)
    missions = Mission.objects.all()
    visions = Vision.objects.all()

    return render(request, 'index.html', {
        'banners': banners,
        'home_about': home_about,
        'why_choose': why_choose,
        'services': services,
        'projects': projects,
        'partners': partners,
        'missions': missions,
        'visions': visions,
        'hide_banner': True,
    })

def about_view(request):
    header = AboutPageHeader.objects.filter(page_name='about', is_active=True).first()
    about_sections = AboutSection.objects.filter(is_active=True)

    return render(request, 'about.html', {
        'header': header,
        'about_sections': about_sections,
    })


def compliance_view(request):
    compliance_sections = ComplianceSection.objects.filter(is_active=True)

    return render(request, 'compliance.html', {
        'compliance_sections': compliance_sections,
    })


def key_management_view(request):
    team_members = KeyManagement.objects.filter(is_active=True).order_by('order')
    return render(request, 'key_management.html', {
        'team_members': team_members,
    })


def legal_frameworks(request):
    legals = LegalFramework.objects.filter(is_active=True).order_by('-id')
    return render(request, 'legal_frameworks.html', {
        'legals': legals
    })


def incentives_facilities(request):
    data = FacilitiesIncentives.objects.filter(is_active=True).first()
    return render(request, 'facilities.html', {
        'facility': data
    })


def gallery(request):
    galleries = OurGallery.objects.filter(is_active=True)
    return render(request, 'gallery.html', {
        'galleries': galleries
    })

def our_service(request):
    services = OurService.objects.filter(is_active=True)
    return render(request, 'service.html', {
        'services': services
    })

def news_event(request):
    # news_events = NewsEvents.objects.filter(is_active=True)
    # return render(request, 'news_event.html', {
    #     'news_events': news_events
    # })
    pass


def mission_vision(request):
    mission_vision = MissionVision.objects.all()

    context = {
        'mission_vision': mission_vision,
    }
    return render(request, 'our_service.html', context)


def request_investor(request):
    investor_data = RequestInvestorData.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        city = request.POST.get('city', '').strip()
        country = request.POST.get('country', '').strip()
        address = request.POST.get('address', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not name or not email or not message_text:
            messages.error(request, "Name, Email, and Message are required!")
        else:
            RequestInvestorMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                city=city,
                country=country,
                address=address,
                message=message_text
            )
            send_mail(
                subject=f'New Investor Registration: {name}',
                message=(
                    f'Name: {name}\n'
                    f'Email: {email}\n'
                    f'Phone: {phone}\n'
                    f'City: {city}\n'
                    f'Country: {country}\n'
                    f'Address: {address}\n'
                    f'Message: {message_text}'
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['info@bayeconomiczone.com'],
                fail_silently=False,
            )
            messages.success(request, "Your request has been submitted successfully!")
            return redirect('request_investor')

    return render(request, 'request_investor.html', {
        'investor_data': investor_data
    })

def contact(request):
    # Get active contact info
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not name or not email or not message_text:
            messages.error(request, "Name, Email, and Message are required!")
        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            messages.success(request, "Your message has been submitted successfully!")
            return redirect('contact')  # Redirect to same page after submission

    return render(request, 'contact.html', {
        'contact_info': contact_info
    })