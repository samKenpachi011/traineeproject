from django.apps import apps as django_apps
from django.conf import settings
from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

class HomeView(EdcBaseViewMixin,NavbarViewMixin,TemplateView):
#  set variables
    template_name = 'traineeproject/home.html'
    navbar_name = 'traineeproject'
    navbar_selected_item = 'home'

    subject_screening_model = 'traineeproject_subject.screeningeligibility'
    subject_consent_model = 'traineeproject_subject.subjectconsent'

# create getter/setter func that return models

    @property
    def subject_screening_cls(self):
        return django_apps.get_model(self.subject_screening_model)

    @property
    def subject_consent_cls(self):
        return django_apps.get_model(self.subject_consent_model)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        subject_screening = self.subject_screening_cls.objects.all()
        subject_consent = self.subject_consent_cls.objects.all()

        screened_subjects = subject_screening.count()
        consented_subjects = subject_consent.count()

        context.update(
            screened_subjects=screened_subjects,
            consented_subjects=consented_subjects
        )
        return context