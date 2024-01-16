# pricing_api/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

class CalculatePricing(APIView):
    template_name = 'pricing_api/calculate_pricing.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        distance_travelled = float(request.data.get('distance_travelled', 0))
        total_time = float(request.data.get('total_time', 0))
        wait_time = float(request.data.get('wait_time', 0))

        current_date = timezone.now().date()
        day_of_week = current_date.weekday()

        dist_base_price = {} 
        ## base prices for all the days are set
        dist_base_price[1] = 80
        dist_base_price[2] = 80
        dist_base_price[3] = 80
        dist_base_price[0] = 90
        dist_base_price[4] = 90
        dist_base_price[5] = 85
        dist_base_price[6] = 85
        ## till three kms it uses the additional_price which is 28 per KM.
        ## TMF will be 1x under 1hr, 1.25x till 2 hrs, 2.2x till 3hrs and after that is 4x
        ## waiting charge is 5rs per min.
        distace_add_price = 28
        wait_charge = 5
        tmf = {}
        tmf[1] =1
        tmf[2] = 1.25
        tmf[3] = 2.2
        tmf[4] = 4
        price = 0
        tmf_factor = int((total_time-wait_time)/60 + 1)
        tmf_factor = min(tmf_factor, 4)
        if distance_travelled < 3:
            price = ((distance_travelled)*distace_add_price + (tmf[tmf_factor])*(total_time-wait_time) + (wait_time*wait_charge))
        else:
            price = (dist_base_price[day_of_week] + (distance_travelled-3)*distace_add_price + (tmf[tmf_factor])*(total_time-wait_time) + (wait_time*wait_charge))
        
        return render(request, self.template_name, {'price': price})
