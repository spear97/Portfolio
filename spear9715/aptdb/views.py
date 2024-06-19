from django.shortcuts import render
from .models import *
from .parser import *
import json

# Create your views here.
def index(request):

    # Retrieve all Coords instances from the database
    all_coords = list(Coords.objects.values_list('long', 'lat'))

    # Retrieve all names from the Apt model
    all_names = list(Apt.objects.values_list('name', flat=True))

    # Retrieve all addresses from Apt model
    all_addresses = list(Apt.objects.values_list('address', flat=True))

    all_cities = get_cities(all_addresses)

    content = {
        'coords': json.dumps(all_coords),
        'names': json.dumps(all_names),
        'address': json.dumps(all_addresses),
        'cities': all_cities,
    }

    return render(request, 'aptdb_index.html', content)

def search(request):

    if request.method == 'POST':

        try:
            rent_min = request.POST.get('rent_min')
            rent_max = request.POST.get('rent_max')
            city = request.POST.get('city')
            zip_code = request.POST.get('zip_code')

            entered_data = rent_min and rent_max and city and zip_code
            content = None

            if not entered_data: # Display all Apartments

                # Retrieve all addresses from Apt model
                all_addresses = list(Apt.objects.values_list('address', flat=True))

                # Retrieve all names from the Apt model
                all_names = list(Apt.objects.values_list('name', flat=True))

                # Retrieve all minimums from the Amounts model
                all_mins = list(Amounts.objects.values_list('minimum', flat=True))

                # Retrieve all maximums from the Amounts model
                all_maxs = list(Amounts.objects.values_list('maximum', flat=True))

                # Retrieve all links from the Info model
                all_links = list(Info.objects.values_list('url', flat=True))

                # Retrieve all images from the Image model
                all_imgs = list(Images.objects.values_list('src', flat=True))

                # Retrive all phone_number from the Info model
                all_number = list(Info.objects.values_list('phone_number', flat=True))

                content = {
                    'names': json.dumps(all_names),
                    'addresses': json.dumps(all_addresses),
                    'mins': json.dumps(all_mins),
                    'maxs': json.dumps(all_maxs),
                    'links': json.dumps(all_links),
                    'imgs': json.dumps(all_imgs),
                    'numbers': json.dumps(all_number),
                }

            else: # Display Apartments from Query

                # Ensure that rent_min is less than rent_max and vice-versa
                if rent_min > rent_max:
                    rent_min, rent_max = rent_max, rent_min

                # Get Contents of Models
                apartments = Apt.objects.all()
                amounts = Amounts.objects.all()
                contacts = Info.objects.all()
                images = Images.objects.all()

                if city:

                    # Filter apartments based on the selected city
                    apartments = apartments.filter(address__icontains=city)

                    # Get the IDs of the filtered apartments
                    apartment_ids = apartments.values_list('id', flat=True)

                    # Filter amounts, contacts, and images based on the IDs of the filtered apartments
                    amounts = amounts.filter(apt_id__in=apartment_ids)
                    contacts = contacts.filter(apt_id__in=apartment_ids)
                    images = images.filter(apt_id__in=apartment_ids)

                if zip_code:
                    
                    # Filter apartments based on the selected zip_code
                    apartments = apartments.filter(address__icontains=zip_code)

                    # Get the IDs of the filtered apartments
                    apartment_ids = apartments.values_list('id', flat=True)

                    # Filter amounts, contacts, and images based on the IDs of the filtered apartments
                    amounts = amounts.filter(apt_id__in=apartment_ids)
                    contacts = contacts.filter(apt_id__in=apartment_ids)
                    images = images.filter(apt_id__in=apartment_ids)

                if rent_min:
                    
                    # Filter apartments based on the entered rent_min
                    amounts = amounts.filter(minimum__gte=int(rent_min))

                    # Get the Apt_ids of the filtered apartments
                    amt_ids = amounts.values_list('apt_id', flat=True)

                    # Filter Apartments, contacts, and images based on the IDs of the filtered amounts
                    apartments = apartments.filter(id__in=amt_ids)
                    contacts = contacts.filter(apt_id__in=amt_ids)
                    images = images.filter(apt_id__in=amt_ids)

                if rent_max:
                    
                    # Filter apartments based on the entered rent_max
                    amounts = amounts.filter(minimum__lte=int(rent_max))

                    # Get the Apt_ids of the filtered apartments
                    amt_ids = amounts.values_list('apt_id', flat=True)

                    # Filter Apartments, contacts, and images based on the IDs of the filtered amounts
                    apartments = apartments.filter(id__in=amt_ids)
                    contacts = contacts.filter(apt_id__in=amt_ids)
                    images = images.filter(apt_id__in=amt_ids)

                # Retrieve all addresses from Apt model
                all_addresses = list(apartments.values_list('address', flat=True))

                # Retrieve all names from the Apt model
                all_names = list(apartments.values_list('name', flat=True))

                # Retrieve all minimums from the Amounts model
                all_mins = list(amounts.values_list('minimum', flat=True))

                # Retrieve all maximums from the Amounts model
                all_maxs = list(amounts.values_list('maximum', flat=True))

                # Retrieve all links from the Info model
                all_links = list(contacts.values_list('url', flat=True))

                # Retrieve all images from the Image model
                all_imgs = list(images.values_list('src', flat=True))

                # Retrieve all phone_number from the Info model
                all_number = list(contacts.values_list('phone_number', flat=True))

                content = {
                    'names': json.dumps(all_names),
                    'addresses': json.dumps(all_addresses),
                    'mins': json.dumps(all_mins),
                    'maxs': json.dumps(all_maxs),
                    'links': json.dumps(all_links),
                    'imgs': json.dumps(all_imgs),
                    'numbers': json.dumps(all_number),
                }

            return render(request, 'aptdb_results.html', content)

        except ValueError as e:
            return render(request, 'aptdb_results.html')


    return render(request, 'aptdb_results.html')