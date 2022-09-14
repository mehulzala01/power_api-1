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
        try:
            contact_method = int(data['contact_method'])
        except:
            contact_method = 0
        indigenous_status = data ['indigenous_status']
        acso_identifier = data['acso_identifier']
        referral_direction = data['referral_direction']
        try:
            event_type = int(data['event_type'])
        except:
            event_type = 0
        percentage_course_completed = data['percentage_course_completed']
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
                    and contact_method in [1, 2, 3, 4, 5, 9]):
                dtau_base = 0.91
            elif (service_stream == 'AD20' and funding_source in [100, 116, 3]
                    and target_population in ['Men', 'Women', 'Parent with Child', 'Family', 'Child', 'General Non-specific'] 
                    and course_length == 'Extended'
                    and contact_method in [1, 2, 3, 4, 5, 9]):
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
                    and contact_method in [1, 2, 5]): # ignore contact_type as all existing contact_type is '1' 
                dtau_base = 0.781
            elif (service_stream == 'AD21' and funding_source == 109 and contact_method in [1, 2, 5]):
                dtau_base = 0.470
            # elif (service_stream == 'AD21' and funding_source in [116, 134, 135, 136] anc contact_type == 2 
            #         and contact_method in [1, 2, 5]):
            #         dtau_base = 0.130   # ignored as no contact_type == 2 in existing dataset
            # elif (service_stream == 'AD21' and funding_source == 109, and contact_type == 2 and contact_method in [1, 2, 5]):
            #     dtau_base = 0.850       # ignored as no contact_type == 2 in existing dataset
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
            elif (service_stream in ['AD20', 'AD21', 'AD71'] and funding_source == 102 and contact_method in [1, 2, 5]):
                dtau_base = 0.470     #ignoed contact_type == 1 as only one contact type exists
            elif (service_stream == 'AD80' and funding_source in [100, 3] and contact_count > 0 and contact_method in [1, 2, 5]):
                dtau_base = 0.091
            elif (service_stream == 'AD80' and funding_source in [100, 3] and contact_count > 0 and contact_method in [3, 4, 6]):
                dtau_base = 0.072
            else:
                dtau_base = 0

        elif (end_date != datetime(1900, 1, 1) and service_stream == 'AD52' and funding_source in [116, 120, 126, 130, 131, 132, 133] and contact_method in [1, 2, 5]): # Contact based DTAU (service_stream == 'AD52')
            dtau_base = contact_count * 0.091
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
        elif ((acso_identifier not in ['9999999', None] and referral_direction == 'Referral IN') or funding_source in [102, 109, 112, 113, 114, 115]):
            dtau_weight = 1.15
        else:
            dtau_weight = 1.0

        # calculate DTAU
        if (event_type == 3 and percentage_course_completed in ['None of course completed', 'Not stated / inadequately described']):
            dtau = 0
        else:
            dtau = dtau_base * dtau_weight


        return Response({'message': "Success!", 
                         'data': {
                            'dtau_base': dtau_base, 
                            'dtau_weight': dtau_weight,
                            'dtau': dtau
                         }})
    return Response({'error': "The VADC DTAU Base api only supports POST operation!"})