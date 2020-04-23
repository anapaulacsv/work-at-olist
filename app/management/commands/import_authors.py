from django.core.management.base import BaseCommand, CommandError
from app.models import Author
from csv import reader


class Command(BaseCommand):
   
    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        #Get file name
        csv_file = options['csv_file']
        #Verify valid file name
        if csv_file is not None and csv_file[0] is not None:
            with open(csv_file[0], encoding="utf8") as csv_file:
                #Read file
                csv_read = reader(csv_file)
                #For each row create an author
                for row in csv_read:
                    author = Author(name=row[0])
                    author.save()         
                    print(f'Imported author {row[0]}')
        self.stdout.write('Import completed')