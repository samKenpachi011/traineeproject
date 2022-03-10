
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
from edc_visit_tracking.constants import (SCHEDULED, UNSCHEDULED, LOST_VISIT,
                                        MISSED_VISIT, COMPLETED_PROTOCOL_VISIT)
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from traineeproject_dashboard.patterns import subject_identifier
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU


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


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = 'botswana'
    definitions = {
        '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                             slots=[100, 100, 100, 100, 100, 100, 100]),
        '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                             slots=[100, 100, 100, 100, 100])}
class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    default_appt_type = 'clinic'
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='traineeproject_subject.subjectvisit',
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
    
class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
    reason_field = {'training_subject.subjectvisit': 'reason'}
    create_on_reasons = [SCHEDULED, UNSCHEDULED, COMPLETED_PROTOCOL_VISIT]
    delete_on_reasons = [LOST_VISIT, MISSED_VISIT, FAILED_ELIGIBILITY]       