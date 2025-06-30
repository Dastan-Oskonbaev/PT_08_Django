from django.http import HttpResponse


def hello_view(request):
    return HttpResponse("Hello, world!")


def goodbye_view(request):
    html = ("<html>"
            "<body>"
            "<h1>"
            "Goodbye, world!"
            "</h1>"
            "</body>"
            "</html>")
    return HttpResponse(html, status=200)