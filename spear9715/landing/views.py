from django.shortcuts import render
import json

def index(request):
    
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
    
    return render(request, 'index.html', {'skills': skills})