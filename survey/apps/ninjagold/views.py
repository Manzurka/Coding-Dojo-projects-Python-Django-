# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
from time import localtime, strftime
# Create your views here.
def root(request):
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'gold' not in request.session:
        request.session['gold'] =0
    return render(request, 'ninjagold/index.html')

def process(request):
    if  request.POST['building'] == "farm":
        winnings=random.randrange(10,20)
        request.session['gold']+=winnings
        request.session['activity'].append("Earned "+str(winnings)+" golds from the farm!  "+ strftime("%b-%d-%Y %H:%M %p", localtime()))
        request.session.modified = True

    elif request.POST['building'] == "cave":
        winnings=random.randrange(5,10)
        request.session['gold']+=winnings
        request.session['activity'].append("Earned "+str(winnings)+" golds from the cave!  "+ strftime("%b-%d-%Y %H:%M %p", localtime()))
        request.session.modified = True
    elif request.POST['building'] == "house":
        winnings=random.randrange(2,5)
        request.session['gold']+=winnings
        request.session['activity'].append("Earned "+str(winnings)+" golds from the house!  "+ strftime("%b-%d-%Y %H:%M %p", localtime()))
        request.session.modified = True

    elif request.POST['building'] == "casino":
        money=random.randrange(-50,50)

        if (money>0):
            request.session['gold']+=money
            request.session['activity'].append("Earned "+str(money)+" golds from the casino!  "+ strftime("%b-%d-%Y %H:%M %p", localtime()))
            request.session.modified = True
        else:
            request.session['gold']-=abs(money)
            request.session['activity'].append("Lost "+str(abs(money))+" golds from the casino!  "+ strftime("%b-%d-%Y %H:%M %p", localtime()))
            request.session.modified = True
    
    return redirect('/ninjagold')
