from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include('src.zuema_admin.urls')),
    url(r'^authentication/', include('src.authentication.urls')),
    url(r'^buyers/', include('src.buyers.urls')),
    url(r'^products/', include('src.products.urls')),
    url(r'^sellers/', include('src.sellers.urls'))
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
