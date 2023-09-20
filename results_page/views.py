from django.shortcuts import render, redirect
from .models import CountryVote

def vote_for_country(request,country_name):
    """
    Handle voting for a specific country.

    This view function handles voting for a specific country. It expects a POST request with the
    country name as a parameter. If the country exists in the database, its vote count is
    incremented by 1, and the user is redirected to the 'results' page. If the country does not
    exist, no action is taken.

    Args:
        request (HttpRequest): The HTTP request object.
        country_name (str): The name of the country to vote for.

    Returns:
        HttpResponseRedirect: Redirects the user to the 'results' page after voting.

    """
    
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
    """
    Display the results of the country votes.

    This view function retrieves all the country votes from the database and renders the 'results'
    template with the vote data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'results.html' template with the vote data.
    """
    
    all_votes = CountryVote.objects.all()
    
    return render(request, 'results.html', {all_votes: all_votes})
