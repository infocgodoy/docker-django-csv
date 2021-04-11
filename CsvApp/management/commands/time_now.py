from django.core.management.base import BaseCommand
from django.utils import timezone
from django.shortcuts import render, HttpResponse
import sqlite3
import csv 
from django.template import loader


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **options):
         # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        # The data is hard-coded here, but you could load it from a database or
        # some other source.
        csv_data = (
            ('First row', 'Foo', 'Bar', 'Baz'),
            ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
        )

        t = loader.get_template('my_template_name.txt')
        c = {'data': csv_data}
        response.write(t.render(c))
        return response