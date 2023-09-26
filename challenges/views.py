from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
# from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# url için Redirect
from django.urls import reverse
# from django.template.loader import render_to_string


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
    "december": None,
}

# Create views


def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    #     # a href bağlantısı yazılırken tırnak hatası olmaması için \" \" kullanılır
    # # "<li><a href="...">January</a></li><li><a href="...">February</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        # return HttpResponseNotFound("<h1>Invalid month</h1>")
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    # /challenges/january
    redirect_path = reverse("month-challenge", args=[redirect_month]) ## /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            #{"text": challenge_text, "month_name": month.capitalize()},
            {"text": challenge_text, "month_name": month}
        )
        # response_data = render_to_string("challenges/challenge.html")
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")
