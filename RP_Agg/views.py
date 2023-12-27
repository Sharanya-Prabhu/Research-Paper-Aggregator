from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from .models import UserPaperPreference, Paper
from .forms import UserPaperPreferenceForm

import requests
from bs4 import BeautifulSoup
import re


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_search')  # redirect to the dashboard page after successful login
        else:
            # handle authentication error
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


def index_view(request):
    return render(request, "index_view.html", {})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_search')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def scrape_arxiv(query):
    url = f"https://arxiv.org/search/?query={query}&searchtype=all&source=header"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("li", class_="arxiv-result")

    papers = []
    for result in results:
        title = result.find("p", class_="title is-5 mathjax").text.strip()
        link_ele = result.find("a", title="pdf")
        if link_ele:
            link = link_ele.get("href")
        else:
            link = "https://arxiv.org/pdf/2304.12233.pdf"
        summary = result.find("span", class_="abstract-full has-text-grey-dark mathjax").text.strip()
        papers.append({"title": title, "link": link, "summary": summary})

    return papers


@login_required
def query_handler(request):
    if request.method == 'GET':
        search_query = request.GET.get('query')
        papers = scrape_arxiv(search_query)
        return render(request, 'user_search.html', {'papers': papers, 'query': search_query})


@login_required
@require_POST
def save_preferences(request):
    user_paper_preference, created = UserPaperPreference.objects.get_or_create(user=request.user)

    paper_titles = request.POST.getlist('papers')

    for title in paper_titles:
        paper, created = Paper.objects.get_or_create(title=title)
        paper.users.add(request.user)

    user_paper_preference.preferences.add(*Paper.objects.filter(users=request.user))

    return redirect('user_search')




@login_required
def show_preferences(request):
    user_preference, created = UserPaperPreference.objects.get_or_create(user=request.user)
    papers = user_preference.preferences.all()

    for paper in papers:
        # Scrape summary for the paper
        summary = scrape_arxiv(paper.title)[0]['summary']
        paper.summary = summary

    return render(request, 'user_search.html', {'papers': papers})

