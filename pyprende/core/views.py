from django.shortcuts import render
# from django.http import HttpResponse # Envia para o servidor um response


def home(request):
    # return HttpResponse(u'Olá Mundo') # envia para o servidor 'Ola Mundo'
    return render(request, 'home.html')
    '''
        -> return render
        Responsavel por chamar um template, como o exemplo no segundo parametro
        o terceiro parametro é um dicionario assim pode haver o uso de variaveis
        no template.
    '''


def contact(request):
    return render(request, 'contact.html')