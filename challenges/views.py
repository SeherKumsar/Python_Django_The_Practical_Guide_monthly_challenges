from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    return HttpResponseRedirect("/challenges/" + redirect_month)

    # return HttpResponse(month) # sadece integer sayıları döndürür


# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == "january":
#         challenge_text = "Eat no meat for entire month"
#     elif month == "february":
#         challenge_text = "Walk for at leats 20 minutes every day"
#     elif month == "march":
#         challenge_text = "Learn Django for at least 20 minutes every day"
#     elif month == "april":
#         challenge_text = "april"
#     elif month == "may":
#         challenge_text = "may"
#     elif month == "june":
#         challenge_text = "june"

#     else:
#         return HttpResponseNotFound("This month is not supported!")

#     return HttpResponse(challenge_text)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
