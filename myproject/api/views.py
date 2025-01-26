from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from api.models import Department, Employee
from api.serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request):
      try:
        queryset = self.get_queryset()  # Automatically uses the queryset defined at the class level
        serializer = DepartmentSerializer(queryset, many=True)
        return Response({"message": "Departments retrived successfully.", "data": serializer.data},
        status=status.HTTP_200_OK )
      except Employee.DoesNotExist:
            return Response(
                {"message": "Departments not found."},
                status=status.HTTP_404_NOT_FOUND
            )

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            department = serializer.save()
            return Response(
                {"message": "Department created successfully.", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Failed to create Department.", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request):
      try:
        queryset = self.get_queryset()  
        print(queryset)
        # Automatically uses the queryset defined at the class level
        serializer = EmployeeSerializer(queryset, many=True)
        return Response({"message": "employees retrived successfully.", "data": serializer.data},
        status=status.HTTP_200_OK )
      except Employee.DoesNotExist:
            return Response(
                {"message": "Empoyees not found."},
                status=status.HTTP_404_NOT_FOUND
            )


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            return Response(
                {"message": "Employee created successfully.", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Failed to create employee.", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        employee = self.get_object()
        print(args)
        employee.delete()
        return Response(
            {"message": f"Employee '{employee.name}' deleted successfully."},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        employee = self.get_object()
        serializer = self.get_serializer(employee, data=request.data, partial=True) 
        print("edit")
         # partial=True for partial update
        if serializer.is_valid():
            updated_employee = serializer.save()
            return Response(
                {"message": "Employee updated successfully.", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Failed to update employee.", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def retrieve(self, request, *args, **kwargs):
        try:
            # Get the employee object by its primary key (id)
            employee_id = kwargs.get('pk') 
            print(employee_id)
            employee = self.get_object()
            serializer = self.get_serializer(employee)
            return Response(
                {
                    "message": "Employee retrieved successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK
            )
        except Employee.DoesNotExist:
            return Response(
                {"message": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )
