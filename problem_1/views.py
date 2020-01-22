from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from tablib import Dataset


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'problem_1.html'

    def get(self, request):
        print("Get Calling")
        return Response()

    def post(self, request):
        print("Post Calling")
        dataset = Dataset()
        file = request.FILES['myfile']
        #imported_data = dataset.load(file.read())
        dataset_for_import = dataset.load(file.read())
        print(dataset_for_import)

        # data = dict(imported_data)
        # print(imported_data)
        return Response({"Success": "Success"}, status=status.HTTP_200_OK)
