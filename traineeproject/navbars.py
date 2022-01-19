from unicodedata import name
from django.conf import settings
from edc_navbar import NavbarItem, site_navbars ,Navbar

traineeproject = Navbar(name = 'traineeproject') 

traineeproject.append_item(
    NavbarItem(
        name='eligible_subject',
        label='Subject Screening',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('screening_listboard_url')))

traineeproject.append_item(
    NavbarItem(
        name='traineeproject_subject',
        label='Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')))

site_navbars.register(traineeproject)        