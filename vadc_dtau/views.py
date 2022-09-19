from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from datetime import datetime, date




# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@api_view(['GET', 'POST'])
def vadc_dtau_cal(request):
    if request.method == 'POST':
        data = request.data
        # convert the request data into correct format
        service_stream = data['service_stream']
        try:
            start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
        except:
            start_date = datetime(1900, 1, 1)
        try:
            end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
        except:
            end_date = datetime(1900, 1, 1)
        try:
            funding_source = int(data['funding_source'])
        except: 
            funding_source = 0
        target_population = data['target_population']
        course_length = data['course_length']
        contact_count = int(data['contact_count'])
        contact_count125 = int(data['contact_count125'])
        contact_count123459 = int(data['contact_count123459'])
        contact_count346 = int(data['contact_count346'])
        indigenous_status = data ['indigenous_status']
        acso_identifier = data['acso_identifier']
        referral_direction = data['referral_direction']
        try:
            event_type = int(data['event_type'])
        except:
            event_type = 0
        percentage_course_completed = data['percentage_course_completed']
        try:
            contact_type = int(data['contact_type'])
        except:
            contact_type = 0
        significant_goal_achieved = data['significant_goal_achieved']
        service_team = data['service_team']
        try:
            outlet_code = int(data['outlet_code'])
        except:
            outlet_code = 0
        client_urn = data['client_urn']
        episode_no = data['episode_no']
        date_delta = abs((end_date - start_date).days)

        # print('stream:' + service_stream, start_date, end_date, 'funding:' + str(funding_source), 'target:' + target_population, 
        #        'course:' + course_length, 'contact_count' + str(contact_count), 'contact_method:' + str(contact_method), date_delta)

        # calculate DTAU base
        if service_stream != 'AD52' and end_date != datetime(1900, 1, 1):  # Episode based DTAU
            if service_stream == 'AD10' and funding_source == 121 and date_delta <= 10:
                dtau_base = 4.871
            elif service_stream == 'AD10' and funding_source == 121 and date_delta > 10 and date_delta < 10000:
                dtau_base = 8.768
            elif service_stream == 'AD10' and funding_source == 117:
                dtau_base = 5.816
            elif service_stream == 'AD10' and funding_source == 118:
                dtau_base = 6.548
            elif service_stream == 'AD10' and funding_source == 119 and date_delta <= 10:
                dtau_base = 7.000
            elif service_stream == 'AD10' and funding_source == 119 and date_delta > 10 and date_delta < 10000:
                dtau_base = 12.600
            elif service_stream == 'AD10' and funding_source == 120 and date_delta <= 10:
                dtau_base = 9.349
            elif service_stream == 'AD10' and funding_source == 120 and date_delta > 10 and date_delta < 10000:
                dtau_base = 16.828
            elif (service_stream == 'AD11' and funding_source in [100, 116, 3] 
                    and target_population in ['Men', 'Women', 'Parent with Child', 'Family', 'Child', 'General Non-specific'] 
                    and course_length in ['Standard', 'Not stated/inadequately described'] 
                    and contact_count > 0):
                dtau_base = 0.849
            elif (service_stream == 'AD11' and funding_source in [100, 116, 3] 
                    and target_population in ['Men', 'Women', 'Parent with Child', 'Family', 'Child', 'General Non-specific'] 
                    and course_length == 'Extended' and contact_count > 0):
                dtau_base = 2.124
            elif (service_stream == 'AD20' and funding_source in [100, 116, 3]
                    and target_population in ['Men', 'Women', 'Parent with Child', 'Family', 'Child', 'General Non-specific'] 
                    and course_length in ['Standard', 'Not stated/inadequately described'] 
                    and contact_count123459 > 0):
                dtau_base = 0.91
            elif (service_stream == 'AD20' and funding_source in [100, 116, 3]
                    and target_population in ['Men', 'Women', 'Parent with Child', 'Family', 'Child', 'General Non-specific'] 
                    and course_length == 'Extended'
                    and contact_count123459 > 0):
                dtau_base = 3.414
            elif service_stream == 'AD20' and funding_source == 112:
                dtau_base = 2.094
            elif service_stream == 'AD20' and funding_source == 113:
                dtau_base = 3.926
            elif service_stream == 'AD20' and funding_source == 114:
                dtau_base = 2.748
            elif service_stream == 'AD20' and funding_source == 115:
                dtau_base = 4.120
            elif (service_stream == 'AD21' and funding_source in [116, 134, 135, 136] 
                    and contact_count125 > 0): # ignore contact_type as all existing contact_type is '1' 
                dtau_base = 0.781
            elif (service_stream == 'AD21' and funding_source == 109 and contact_count125 > 0):
                dtau_base = 0.470
            elif (service_stream == 'AD21' and funding_source in [116, 134, 135, 136] and contact_type == 2 
                    and contact_count125 > 0):
                dtau_base = 0.130   
            elif (service_stream == 'AD21' and funding_source == 109 and contact_type == 2 and contact_count125 > 0):
                dtau_base = 0.850     
            elif (service_stream == 'AD30' and funding_source == 128 and date_delta <= 160):
                dtau_base = 13.481
            elif (service_stream == 'AD30' and funding_source == 128 and date_delta > 160 and date_delta < 10000):
                dtau_base = 53.659
            elif (service_stream == 'AD30' and funding_source == 129):
                dtau_base = 5.947
            elif (service_stream == 'AD30' and funding_source == 123):
                dtau_base = 7.180
            elif (service_stream == 'AD30' and funding_source == 106 and date_delta <= 160):
                dtau_base = 16.810
            elif (service_stream == 'AD30' and funding_source == 106 and date_delta > 160 and date_delta < 10000):
                dtau_base = 66.913
            elif (service_stream == 'AD30' and funding_source == 111):
                dtau_base = 63.573
            elif (service_stream == 'AD30' and funding_source == 125 and date_delta <= 160):
                dtau_base = 27.874
            elif (service_stream == 'AD30' and funding_source == 125 and date_delta > 160 and date_delta < 10000):
                dtau_base = 110.949
            elif (service_stream == 'AD30' and funding_source == 126 and date_delta <= 90):
                dtau_base = 24.660
            elif (service_stream == 'AD30' and funding_source == 126 and date_delta > 90 and date_delta < 10000):
                dtau_base = 83.846
            elif (service_stream == 'AD30' and funding_source == 127 and date_delta <= 90):
                dtau_base = 28.293
            elif (service_stream == 'AD30' and funding_source == 127 and date_delta > 90 and date_delta < 10000):
                dtau_base = 96.198
            elif (service_stream == 'AD31' and funding_source in [100, 116]):
                dtau_base = 11.000
            elif (service_stream == 'AD33' and funding_source in [106, 111, 128, 126, 127, 129, 123, 125]):
                dtau_base = 0.974
            elif (service_stream == 'AD33' and funding_source in [117, 118, 119, 120, 121]):
                dtau_base = 0.325
            elif (service_stream == 'AD50' and funding_source in [100, 116, 3]):
                dtau_base = 2.222
            elif (service_stream == 'AD71' and funding_source in [100, 116, 3]):
                dtau_base = 0.781
            elif (service_stream in ['AD20', 'AD21', 'AD71'] and funding_source == 102 and contact_count125 > 0):
                dtau_base = 0.470     #ignoed contact_type == 1 as only one contact type exists
            elif (service_stream == 'AD80' and funding_source in [100, 3] and contact_count > 0 and contact_count125 > 0):
                dtau_base = 0.091
            elif (service_stream == 'AD80' and funding_source in [100, 3] and contact_count > 0 and contact_count346 > 0):
                dtau_base = 0.072
            else:
                dtau_base = 0

        elif (end_date != datetime(1900, 1, 1) and service_stream == 'AD52' and funding_source in [116, 120, 126, 130, 131, 132, 133] and contact_count125 > 0): # Contact based DTAU (service_stream == 'AD52')
            dtau_base = contact_count125 * 0.091
        else:
            dtau_base = 0

        # Readjusting DTAU base
        if funding_source in [102, 109, 112, 113, 114, 115]:
            dtau_base = dtau_base / 1.15
        elif funding_source == 127:
            dtau_base = dtau_base / 1.30

        # calculate DTAU weight
        if (indigenous_status in ['Aboriginal', 'Torres Strait Islander', 'BOTH Aboriginal & TSI']):
            dtau_weight = 1.30
        elif ((acso_identifier not in ['9999999', '0000000'] and referral_direction == 'Referral IN') or funding_source in [102, 109, 112, 113, 114, 115]):
            dtau_weight = 1.15
        else:
            dtau_weight = 1.0

        # calculate DTAU
        if (event_type == 3 and percentage_course_completed in ['None of course completed', 'Not stated / inadequately described']):
            dtau = 0
        else:
            dtau = dtau_base * dtau_weight

        # catogerise activity code
        if funding_source in [100, 102]:
            if service_stream == 'AD11':
                activity_code = '34303'
                activity_name = 'Non-residential Withdrawal'
            elif service_stream == 'AD20':
                activity_code = '34301'
                if outlet_code == 10:
                    activity_name = 'Counselling - Reconnexion'
                else:
                    activity_name = 'Counselling'
            elif service_stream in ['AD30', 'AD32']:
                activity_code = '34053'
                activity_name = 'Adult Residential Rehabilitation'
            elif service_stream == 'AD50':
                activity_code = '34300'
                activity_name = 'Care and Recovery Coordination'
            elif service_stream == 'AD51':
                activity_code = '34071'
                activity_name = 'Youth Outreach'
            elif service_stream == 'AD71':
                activity_code = '34307'
                if outlet_code == 10:
                    activity_name = 'Assessment - Reconnexion'
                else:
                    activity_name = 'Assessment'
            elif service_stream == 'AD80':
                activity_code = '34306'
                if outlet_code == 10:
                    activity_name = 'Intake - Reconnexion'
                else:
                    activity_name = 'Intake'
            elif service_stream == 'AD21':
                activity_code = '34307'
                if outlet_code == 10:
                    activity_name = 'Assessment - Reconnexion'
                else:
                    activity_name = 'Assessment'
            else:
                activity_code = 'UKN'
        elif funding_source in [128, 131]:
            activity_code = '34053'
            activity_name = 'Adult Residential Rehabilitation'
        elif funding_source in [132, 134]:
            activity_code = '34306'
            if outlet_code == 10:
                activity_name = 'Intake - Reconnexion'
            else:
                activity_name = 'Intake'
        elif funding_source in [133, 135]:
            activity_code = '34307'
            if outlet_code == 10:
                activity_name = 'Assessment - Reconnexion'
            else:
                activity_name = 'Assessment'
        elif funding_source == 136:
            activity_code = '34301'
            if outlet_code == 10:
                activity_name = 'Counselling - Reconnexion'
            else:
                activity_name = 'Counselling'
        elif funding_source == 503 and service_stream == 'AD20' and target_population == 'Family':
            activity_code = ''
            activity_name = 'Family Focus'
        else:
            activity_code = 'UKN'

        # Categorize forensic type
        if (acso_identifier not in ['0000000', '9999999'] and referral_direction == 'Referral IN') or funding_source in [102, 109, 112, 113, 114, 115]:
            forensic = 'Forensic'
        else:
            forensic = 'Voluntary'

        # Categorize Risk Of Overdose (ROO) flag
        if service_team in ['AOD SE Harm Minimisation', 'AOD Eastern Harm Minimisation']:
            roo_flag = 'Y'
        else:
            roo_flag = 'N'

        # Mark sub-activities
        if roo_flag == 'Y':
            sub_activity = "ROO - " + activity_name
        elif service_stream == 'AD52':
            sub_activity = activity_name + ' - Bridging Support'
        elif service_stream == 'AD21':
            sub_activity = activity_name + ' - Brief Intervention'
        else:
            sub_activity = activity_name

        return Response({"message": "Success!", 
                         "data": {
                            "dtau_base": dtau_base, 
                            "dtau_weight": dtau_weight,
                            "dtau": dtau, 
                            "activity_code": activity_code,
                            "activity_name": activity_name,
                            "forensic_type": forensic, 
                            "roo_flag": roo_flag,
                            "sub_activity": sub_activity
                         }})
    return Response({'error': "The VADC DTAU Base api only supports POST operation!"})