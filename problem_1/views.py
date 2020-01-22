from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from tablib import Dataset

from problem_1.parse_data import parse_requested_data_and_get_result


# class Post(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'return.html'
#     def get(self, request):
#         print("Get Calling")
#         return Response()
#         #return Response({"Success": "Success", "data": imported_data[2:15]}, status=status.HTTP_200_OK)

def post_edit(request):
    if request.method == "POST":
        print("Post Calling")
        dataset = Dataset()
        file = request.FILES['myfile']
        imported_data = list(dataset.load(file.read()))
        data = parse_requested_data_and_get_result(imported_data)
        print(len(imported_data))
        return render(request, 'return.html',)
    else:
        return render(request, 'upload.html',)
