from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("operations.urls")),
    path("reports/", include("reporting.urls")),
]
