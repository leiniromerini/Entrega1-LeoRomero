from django import forms   #Aca importo los formularios de django 
from productos.models import Productos  # Aca importo el modelo Productos para usarlo  caundo creo la cass form 



#Create your Forms here 


class Product_form(forms.ModelForm):                   # Aca lo creo pero de manera mas rapida llamando a los Modelform
    class Meta:
        model = Productos
        fields = '__all__'
