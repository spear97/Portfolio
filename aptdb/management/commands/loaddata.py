import json
from django.core.management.base import BaseCommand
from aptdb.models import Apt, Amounts, Info, Coords, Images
from landing.models import Skills
import os

class Command(BaseCommand):
    help = 'Backup SQLite3 data to JSON'

    def handle(self, *args, **options):

        # Get the directory path to save the backup file
        backup_dir = os.path.join(os.getcwd(), 'backups')

        # Construct the file path for the backup JSON file
        backup_file_path = os.path.join(backup_dir, 'backup.json')

        if not os.path.exists(backup_file_path):
            self.stdout.write(self.style.ERROR("ERROR! Backup does not exist! Please create backup and try again!"))
            return

        with open(backup_file_path, 'r') as file:
            data = json.load(file)

            apt, amounts, info, coord, image = data['Apt'], data['Amounts'], data['Info'], data['Coords'], data['Images']

            apt_length, amounts_length, info_length, coord_length, image_length = len(apt), len(amounts), len(info), len(coord), len(image)

            if apt_length == amounts_length == info_length == coord_length == image_length:
                
                for i in range(apt_length):

                    # Create a new Apt instance
                    new_apt = Apt.objects.create(name=apt[i]['name'], address=apt[i]['address'])

                    # Create a new Amounts instance associated with the newly created Apt
                    Amounts.objects.create(minimum=amounts[i]['minimum'], maximum=amounts[i]['maximum'], apt=new_apt)

                    # Create a new Info instance associated with the newly created Apt
                    Info.objects.create(phone_number=info[i]['phone_number'], url=info[i]['url'], apt=new_apt)

                    # Create a new Coords instance associated with the newly created Apt
                    Coords.objects.create(long=coord[i]['long'], lat=coord[i]['lat'], apt=new_apt)

                    # Create a new Images instance associated with the newly created Apt
                    Images.objects.create(src=image[i]['src'], apt=new_apt)

            skill = data["skills"]

            for i in range(len(skill)):
                Skills.objects.create(name=skill[i]['name'], percentage=skill[i]['percentage'])


        # Output that Backup of Data 
        self.stdout.write(self.style.SUCCESS("Data was successfully loaded into the DataBase!"))
