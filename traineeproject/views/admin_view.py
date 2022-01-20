from django.views.generic import TemplateView
from edc_base.view_mixins import AdministrationViewMixin,EdcBaseViewMixin
from edc_navbar import NavbarViewMixin
class AdministrationView(EdcBaseViewMixin, NavbarViewMixin,
                         AdministrationViewMixin, TemplateView):

    navbar_name = 'traineeproject'
    navbar_selected_item = 'administration'