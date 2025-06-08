from django.http import HttpResponse

from django.views.generic import View
from django.template.loader import get_template
from django.shortcuts import render

import datetime

from .renderers import render_to_pdf

def index(request):
    return render(request, 'index.html', {})

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')

        context = {
            "invoice_number": request.GET.get('numero'),
            "customer_name": request.GET.get('nombre'),
            "amount": "S/." + request.GET.get('monto'),
            "date": datetime.date.today(),
        }

        pdf = render_to_pdf('pdf/invoice.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

def indexPDF(request):
    return render(request, 'pdf/create_pdf.html', {})