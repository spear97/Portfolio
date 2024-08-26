from django.shortcuts import render
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
