from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def ana_sehife(request):
    html_kod = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mənim Şəklim</title>
        <style>
            body { display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background-color: #1a1a1a; }
            img { max-width: 90%; max-height: 90vh; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        </style>
    </head>
    <body>
        <img src="/static/foto.jpg" alt="Layihə Şəkli">
    </body>
    </html>
    '''
    return HttpResponse(html_kod)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ana_sehife, name='home'),  # Əsas səhifə üçün keçid
    path('polls/', include('polls.urls')),
    path('roblox/', include('roblox.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)