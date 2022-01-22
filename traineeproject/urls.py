from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls.conf import path, include
from django.views.generic.base import RedirectView
from traineeproject_subject.admin_site import traineeproject_subject_admin
from edc_data_manager.admin_site import edc_data_manager_admin
from edc_registration.admin_site import edc_registration_admin
from edc_lab.admin_site import edc_lab_admin


from .views import HomeView, AdministrationView
APP_NAME = 'traineeproject'
urlpatterns = [

    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),

    path('admin/', admin.site.urls),
    path('admin/', traineeproject_subject_admin.urls),
    path('admin/', edc_data_manager_admin.urls),
    path('admin/', edc_registration_admin.urls),
    path('admin/', edc_lab_admin.urls),

    path('administration/', AdministrationView.as_view(),
         name='administration_url'),

    path('admin/traineeproject_subject/', RedirectView.as_view(url='admin/traineeproject_subject/'),
         name='traineeproject_subject_models_url'),
    path('edc_base/', include('edc_base.urls')),
    path('edc_data_manager/', include('edc_data_manager.urls')),
    path('edc_label/', include('edc_label.urls')),
    path('edc_device/', include('edc_device.urls')),

    path('edc_registration/', include('edc_registration.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_subject_dashboard/', include('edc_subject_dashboard.urls')),

    path('traineeproject_subject/', include('traineeproject_subject.urls')),
    path('subject/', include('traineeproject_dashboard.urls')),

    path('switch_sites/', LogoutView.as_view(next_page=settings.INDEX_PAGE),
         name='switch_sites_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
