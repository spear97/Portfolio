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

            # Check if any filter data is entered
            entered_data = rent_min or rent_max or city or zip_code
            content = None

            # Ensure that rent_min is less than rent_max if both are provided
            if rent_min and rent_max and int(rent_min) > int(rent_max):
                rent_min, rent_max = rent_max, rent_min

            # Querysets for filtering
            apartments = Apt.objects.all()
            amounts = Amounts.objects.all()
            contacts = Info.objects.all()
            images = Images.objects.all()

            # Apply filters if any data is entered
            if entered_data:
                if city:
                    apartments = apartments.filter(address__icontains=city)
                if zip_code:
                    apartments = apartments.filter(address__icontains=zip_code)
                if rent_min:
                    amounts = amounts.filter(minimum__gte=int(rent_min))
                if rent_max:
                    amounts = amounts.filter(maximum__lte=int(rent_max))

                # Filter amounts, contacts, and images based on apartment IDs
                apartment_ids = apartments.values_list('id', flat=True)
                amounts = amounts.filter(apt_id__in=apartment_ids)
                contacts = contacts.filter(apt_id__in=apartment_ids)
                images = images.filter(apt_id__in=apartment_ids)

                # Final filtering of apartments based on filtered amounts
                amt_ids = amounts.values_list('apt_id', flat=True)
                apartments = apartments.filter(id__in=amt_ids)

            # Retrieve data
            all_addresses = list(apartments.values_list('address', flat=True))
            all_names = list(apartments.values_list('name', flat=True))
            all_mins = list(amounts.values_list('minimum', flat=True))
            all_maxs = list(amounts.values_list('maximum', flat=True))
            all_links = list(contacts.values_list('url', flat=True))
            all_imgs = list(images.values_list('src', flat=True))
            all_number = list(contacts.values_list('phone_number', flat=True))

            # Prepare content for rendering
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

        except ValueError:
            return render(request, 'aptdb_results.html', {'error': 'Invalid input. Please check your entries.'})

    return render(request, 'aptdb_results.html')
