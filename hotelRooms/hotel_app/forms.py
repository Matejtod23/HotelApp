from django import forms

from .models import Reservation, Employee, Room


class ReservationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.CheckboxInput):
                field.field.widget.attrs['class'] = 'form-control'

        self.fields['receptionist'].queryset = Employee.objects.filter(employee_type="R")

    class Meta:
        model = Reservation
        exclude = ['user', ]
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'})
        }



class RoomForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.CheckboxInput):
                field.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Room
        fields = '__all__'