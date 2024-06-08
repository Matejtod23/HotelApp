from django.contrib import admin
from django import forms
from .models import Employee, EmployeeRooom, Room,Reservation
# Register your models here.
class RoomEmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeRooom
        fields = ['room', 'employee']

    def __init__(self, *args, **kwargs):
        super(RoomEmployeeForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(employee_type="H")


class RoomEmployeeInline(admin.StackedInline):
    model = EmployeeRooom
    extra = 1
    form = RoomEmployeeForm

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomEmployeeInline, ]
    list_display = ['number', 'is_clean', ]

    def has_change_permission(self, request, obj=None):
        cleaner = Employee.objects.filter(user=request.user, employee_type="H").first()
        if obj and cleaner:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


class EmployeeAdmin(admin.ModelAdmin):
    pass

class EmployeeRoomAdmin(admin.ModelAdmin):
    pass

class ReservationAdmin(admin.ModelAdmin):
    exclude = ['user', ]
    list_display = ['code', 'room', ]

    def save_model(self, request, obj, form, change):
        if obj.room.is_clean:
            obj.user = request.user
            return super(ReservationAdmin, self).save_model(request, obj, form)
        return False

    def has_change_permission(self, request, obj=None):
        manager = Employee.objects.filter(user=request.user, employee_type="M").first()
        recep = Employee.objects.filter(user=request.user, employee_type="R").first()

        if obj and (request.user.is_superuser or manager or recep):
            return True
        return False

admin.site.register(Room, RoomAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(EmployeeRooom, EmployeeAdmin)

