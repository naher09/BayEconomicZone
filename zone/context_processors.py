from .models import SiteBanner


def site_banner(request):
    """Provide the active site banner matching the current page slug."""
    slug = request.path.strip('/').split('/')[0]
    # Prefer a banner explicitly assigned to this page; fall back to a
    # blanket banner (page_name left blank) if none matches.
    banner = (
        SiteBanner.objects.filter(is_active=True, page_name__iexact=slug).first()
        or SiteBanner.objects.filter(is_active=True, page_name__isnull=True).first()
    )
    return {
        'site_banner': banner,
    }