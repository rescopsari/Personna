import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaulttags import url

from persona_app.models import Personna


def persona_list(request):
    personas = Personna.objects.all().order_by("id").reverse()
    context = {
        'personas': personas
    }
    # for persona in personas:
    #     print(persona)

    return render(request, template_name='personna_app/persona_list.html', context=context)


def persona_details(request, id):
    persona = Personna.objects.get(id=id)

    context = {
        'persona': persona,
    }

    return render(request, template_name='personna_app/persona_details.html', context=context)


def persona_generate(request):
    information_new_user = requests.get("https://randomuser.me/api?nat=fr").json()["results"][0]
    n = Personna.objects.create(first_name=information_new_user["name"]["first"],
                            last_name=information_new_user["name"]["last"],
                            adress_street=information_new_user["location"]["street"]["name"],
                            adress_number=information_new_user["location"]["street"]["number"],
                            city=information_new_user["location"]["city"],
                            country=information_new_user["location"]["country"],
                            postcode=information_new_user["location"]["postcode"],
                            email=information_new_user["email"],
                            username=information_new_user["login"]["username"],
                            password=information_new_user["login"]["password"],
                            age=information_new_user["dob"]["age"],
                            picture=information_new_user["picture"]["medium"])
    n.save()
    return redirect('details_persona', n.id)
