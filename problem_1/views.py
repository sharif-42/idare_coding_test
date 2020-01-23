from django.shortcuts import render
from tablib import Dataset

from problem_1.parse_data import parse_requested_data_and_get_result


def calculate_xl_data(request):
    if request.method == "POST":
        print("Post Calling")
        dataset = Dataset()
        file = request.FILES['myfile']
        imported_data = list(dataset.load(file.read()))
        data, data2, data3 = parse_requested_data_and_get_result(imported_data)
        return render(request, 'return.html', {"data": data, "data2": data2, "data3": data3})
    else:
        return render(request, 'upload.html', )
