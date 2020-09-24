from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from crossword.api.serializers import UserSerializer, GroupSerializer
from django.views.decorators.csrf import csrf_exempt
from crossword.ai.handle_crossword import HandleCrossword
import json


@csrf_exempt
def generate_crossword(request):
    response = {"error": "Method Not Allowed!"}
    if request.method != 'GET':
        return JsonResponse(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    data = request.GET.get('data')
    if not data:
        response = {"error": "Invalid value!"}
        return JsonResponse(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    try:
        crossword_schema = json.loads(data)
    except:
        response = {"error": "Invalid json!"}
        return JsonResponse(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    handle_crossword = HandleCrossword(crossword_schema)
    complete_crossword = handle_crossword.generate()

    return JsonResponse({'response': complete_crossword})


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
