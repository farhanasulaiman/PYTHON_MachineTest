from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from StudentApp.models import Student
from StudentApp.serializers import StudentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def f_studentlist(request):
    if request.method == 'GET':
        studentset = Student.objects.all()
        serializer = StudentSerializer(studentset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def f_studentrecord(request, id):
    try:
        stud = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(stud)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)
