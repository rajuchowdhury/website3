from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
# Use include() to add paths from the catalog application
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
path('admin/', admin.site.urls),
path('catalog/', include('catalog.urls')),
path('/', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
]