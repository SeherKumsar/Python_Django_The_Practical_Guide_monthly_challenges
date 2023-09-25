from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# url için Redirect
from django.urls import reverse

# Create your views here.
# def january (request):
#     return HttpResponse("This works! January")

# # February
# def february (request):
#     return HttpResponse("This february response")

monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "Walk for at leats 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Nisan",
    "may": "Mayıs",
    "june": "Haziran",
    "july": "Temmuz",
    "august": "Ağustos",
    "september": "Eylül",
    "october": "Ekim",
    "november": "Kasım",
    "december": "Aralık",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_month)
    #return HttpResponseRedirect("/challenge/" + redirect_month)
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    # return HttpResponse(month) # sadece integer sayıları döndürür


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
