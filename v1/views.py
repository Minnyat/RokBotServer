from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .controllers.question import CheckAnswer,GoogleSrearch
# Create your views here.

@api_view(['GET'])
def lyceum(request):
    try:
        question = request.GET['question']
        checkAnswer = CheckAnswer()
        answer = checkAnswer.check(question)
        print(answer)
        if answer == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(answer, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)