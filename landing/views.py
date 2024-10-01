import math
import json
import os
from .models import Skills
from django.shortcuts import render

def home(request):

    all_skills = list(Skills.objects.values_list('name', 'percentage'))

    skills = [{'name': skill[0], 'percentage': skill[1]} for skill in all_skills]

    return render(request, 'home.html', {'skills': skills})

"""Portfolio Projects"""

# View that controls the Backend for the Currency Converter Project
def currency_converter(request):

    with open('currencies.json', 'r') as file:
        currency = json.load(file)

    currency_list = list(currency.keys())

    if request.method == 'POST':

        currency1 = request.POST.get('currency1')
        currency2 = request.POST.get('currency2')

        weight = currency[currency1][currency2]

        result = f"1.0 {currency1} = {weight} {currency2}"

        content = {
            'currency_list': json.dumps(currency_list),
            'result': json.dumps(result)
        }

        return render(request, 'currency_converter_base.html', content)

    content = {
        'currency_list': json.dumps(currency_list),
    }

    return render(request, 'currency_converter_base.html', content)

def Flight_Force_Calculator(request):
    context = {}
    if request.method == 'POST':
        try:
            weight = float(request.POST.get('weight', 0))
            drag_coefficient = float(request.POST.get('dragCoefficient', 0))
            area = float(request.POST.get('area', 0))
            air_density = float(request.POST.get('airDensity', 0))

            # Constants
            GRAVITY = 9.81  # m/s²

            # Calculate takeoff speed and required force
            # Ensure no negative value under the square root
            takeoff_speed = (2 * weight * GRAVITY / (drag_coefficient * air_density * area))
            if takeoff_speed < 0:
                raise ValueError("Invalid parameters: square root of negative number.")
            
            takeoff_speed = math.sqrt(takeoff_speed)
            required_force = weight * GRAVITY

            context['takeoff_speed'] = round(takeoff_speed, 2)
            context['required_force'] = round(required_force, 2)
        except ValueError as e:
            context['error'] = f"Invalid input. {str(e)}"
        except Exception as e:
            context['error'] = f"An unexpected error occurred. {str(e)}"
    
    return render(request, 'FlightForce_base.html', context)