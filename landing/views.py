from django.shortcuts import render
import math
import json

def home(request):

    skill_names = [
        'Python', 'Django', 'Flask', 'Amazon Web Services (AWS)', 'IBM Cloud',
        'Artificial Intelligence (AI)', 'C#', 'C++', 'Cascading Style Sheets (CSS)',
        'HTML', 'GitHub', 'Identity and Access Management (IAM)', 'PHP', 'Java',
        'JavaScript', 'Linux', 'Object-Oriented Programming (OOP)', 'REST APIs',
        'Unreal Engine', 'Unity'
    ]

    skills_percentage = [
        80, 75, 70, 45, 50, 55, 45, 80, 55, 55, 65, 35, 50, 60, 55, 45, 70, 70, 80, 75
    ]

    skills = [{'name': name, 'percentage': percentage} for name, percentage in zip(skill_names, skills_percentage)]

    return render(request, 'home.html', {'skills': skills})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

"""Additional Portfolio Projects"""

# View that controls the Backend for the Currency Converter Project
def currency_converter(request):

    currency = {
        'usd': {
            'usd': 1.0,
            'eur': 0.89,
            'gbp': 0.76,
            'jpy': 144.01
        },
        'eur': {
            'usd': 1.12,
            'eur': 1.0,
            'gbp': 0.85,
            'jpy': 161.13
        },
        'gbp': {
            'usd': 1.32,
            'eur': 1.18,
            'gbp': 1.0,
            'jpy': 190.26
        },
        'jpy': {
            'usd': 0.0069,
            'eur': 0.0062,
            'gbp': 0.0053,
            'jpy': 1.0
        }
    }

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