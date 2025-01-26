from rest_framework import serializers
from api.models import Department,Employee

#create serializers here
class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=Department
        fields="__all__"

    def validate_name(self, value):
        if Department.objects.filter(name=value).exists():
            raise serializers.ValidationError("The Department with this name already exists")
        return value


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model=Employee
        fields="__all__"

    def validate_name(self, value):
        """ Custom validation for the name field. """
        if not value:
            raise serializers.ValidationError("The name field cannot be empty.")
        return value
        
    def validate_id(self, value):
    # Access the HTTP method
        request_method = self.context['request'].method
        if request_method in ['PUT', 'PATCH']:
            # Handle validation for updates (exclude the current object's ID)
            current_employee_id = self.instance.id  # Current instance being updated
            if Employee.objects.filter(id=value).exclude(id=current_employee_id).exists():
                raise serializers.ValidationError("An employee with this ID already exists.")
        else:
            # Handle validation for creation (ensure no duplicates)
            if Employee.objects.filter(id=value).exists():
                raise serializers.ValidationError("An employee with this ID already exists.")

        return value

