from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView



urlpatterns = [
    path('robots.txt/', TemplateView.as_view(
        template_name='robots.txt',
        content_type='text/plain',
    )),

    path('admin/', admin.site.urls),

    path('jet/', include('jet.urls', 'jet')),
    
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
]

admin.site.site_header = "Restraunt name"
admin.site.site_title = "Restraunt name"