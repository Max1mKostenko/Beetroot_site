from django.shortcuts import render


def main(request):
    data = {'title': 'Main Page',
            'values': ["Main Page", "About Page", "Contact Page"],
            "dictionary": {'car': 'BMW',
                           'model': 'X5',
                           'age': '2018'
                           }
            }
    return render(request, "myapp/main.html", data)


def about(request):
    return render(request, "myapp/about.html")


def contacts(request):
    return render(request, "myapp/contacts.html")


