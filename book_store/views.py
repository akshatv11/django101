from django.shortcuts import HttpResponse


# def index(request):
    # name = request.GET['fname']
    # print(name)
    # print(request.GET)
    # return HttpResponse('<h1>hello world</h1>')

def index(request):
    answer = request.GET('number')
    answer = int(answer)**2
    print(answer)
    return HttpResponse(f'{answer}')
