from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView



urlpatterns = [

    # File for webcrawlers
    path('robots.txt/', TemplateView.as_view(
        template_name='robots.txt',
        content_type='text/plain',
    )),

    # Admin panel paths
    path('admin/', admin.site.urls, name='admin'),

    path('jet/', include('jet.urls', 'jet')),
    
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
]

# Website header and title
admin.site.site_header = "Restraunt name"
admin.site.site_title = "Restraunt name"