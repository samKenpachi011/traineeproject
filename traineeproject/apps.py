import configparser
import os
from datetime import datetime
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from dateutil.tz import gettz

from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_label.apps import AppConfig as BaseEdcLabelAppConfig
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_data_manager.apps import AppConfig as BaseEdcDataManagerAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection
from edc_appointment.constants import COMPLETE_APPT
from traineeproject_dashboard.patterns import subject_identifier



class AppConfig(DjangoAppConfig):
    name = 'traineeproject'



class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP150'
    protocol_name = 'BHP150 | ADZ 1222 - ESR-21-21311'
    protocol_number = '150'
    protocol_title = ''
    study_open_datetime = datetime(
        2021, 4, 1, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))

class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='esr21_subject.subjectvisit',
            appt_type='clinic'),
    ]
class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'traineeproject_subject':(
                'subject_visit','traineeproject_subject.subjectvisit')}    

class EdcLabAppConfig(BaseEdcLabAppConfig):
    requisition_model = 'esr21_subject.subjectrequisition'
    result_model = 'edc_lab.result'

class EdcLabelAppConfig(BaseEdcLabelAppConfig):
    template_folder = os.path.join(
        settings.STATIC_ROOT, 'traineeproject', 'label_templates')    
class EdcDataManagerAppConfig(BaseEdcDataManagerAppConfig):
    identifier_pattern = subject_identifier

class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
    timepoints = TimepointCollection(
        timepoints=[
            Timepoint(
                model='edc_appointment.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
            Timepoint(
                model='edc_appointment.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
        ])                