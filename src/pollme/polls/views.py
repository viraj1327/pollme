from django.shortcuts import render
rom django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
rom snippets.serializers import SnippetSerializer
# Create your views here.


@csrf_exempt
def polls_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        polls = polls.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def polls_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        polls = polls.objects.get(pk=pk)
    except polls.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionListSerializer(polls)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionListSerializer(polls, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        polls.delete()
        return HttpResponse(status=204)
