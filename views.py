from django.shortcuts import render

def submit(request):
    return render(request, 'result.html')

def show_exam_result(request):
    context = {
        'score': 80,
        'total': 100
    }
    return render(request, 'result.html', context)
