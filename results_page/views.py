from django.shortcuts import render, redirect
from .models import CountryVote

def vote_for_country(request,country_name):
    if request.method == 'POST':
        try:
            country_vote = CountryVote.objects.get(country_name=country_name)
            country_vote.votes += 1
            country_vote.save()
            return redirect('results_page:results.')
        except CountryVote.DoesNotExist:
            pass
        
    return redirect('home.html')
    

def results(request):
    all_votes = CountryVote.objects.all()
    
    return render(request, 'results.html', {all_votes: all_votes})
