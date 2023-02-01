from django import forms
from django.forms import ModelForm
from .models import*

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        
        fields = ['bill_to','customer_gst_no','description','description2','description3','quantity','quantity2','quantity3','unit_price','unit_price2','unit_price3','amount','amount2','amount3','due_date1','due_date2','due_date3','due_amount1','due_amount2','due_amount3','gst_amount']

     
    <!-- in html page -->
    
    {% widget_tweaks %}
<form action="/your-name/" method="post">
    {% csrf_token %}
    
    <div class="form-group">
    <h6 class="text-light"> <i class="bi bi-reception-0" style="color: aliceblue;"></i> &nbsp; Name</h6>
    {% render_field form.name class='form-control' %}
</div><br>


    <input type="submit" value="Submit">
</form>

   
    <!-- in settings.py (within installed apps) -->
    
    'widget_tweaks'
