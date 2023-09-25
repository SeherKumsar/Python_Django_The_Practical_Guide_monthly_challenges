from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# url için Redirect
from django.urls import reverse


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

# Create views

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        # a href bağlantısı yazılırken tırnak hatası olmaması için \" \" kullanılır
    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
