from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls.conf import path, include
from django.views.generic.base import RedirectView


from .views import HomeView, AdministrationView

urlpatterns = [

    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),

    path('admin/', admin.site.urls),

    path('administration/', AdministrationView.as_view(),
         name='administration_url'),

    path('admin/traineeproject_subject/',
         RedirectView.as_view(url='admin/traineeproject_subject/'),
         name='traineeproject_subject_models_url'),

    path('traineeproject_subject/', include('traineeproject_subject.urls')),
    path('subject/', include('traineeproject_dashboard.urls')),

    path('switch_sites/', LogoutView.as_view(next_page=settings.INDEX_PAGE),
         name='switch_sites_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),

]
