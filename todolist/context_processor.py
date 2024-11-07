# yourapp/context_processors.py
from .models import SiteSettings

def base_template(request):
    try:
        site_settings = SiteSettings.objects.first()
        template = site_settings.template if site_settings else 'base1.html'
    except SiteSettings.DoesNotExist:
        template = 'base1.html'  # Default template if settings not found

    return {
        'base_template': template
    }
