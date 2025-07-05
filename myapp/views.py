'''from django.shortcuts import render
from django.http import HttpResponse
    # Create your views here.
def game(request):
    result=None
    player1=''
    player2=''
    if request.method=='POST':
        player1 = request.POST.get('player1','').lower()
        player2 = request.POST.get('player2', '').lower()
        
        valid_choices = ['rock', 'paper', 'scissors']
        
        if player1 in valid_choices and player2 in valid_choices:
            if player1 == player2:
                result = "tie"
            elif (player1 == 'rock' and player2 == 'scissor')or \
                (player1 == 'scissor' and player2 == 'paper')or \
                (player1 == 'paper' and player2 == 'rock'):
                result = "palyer1 wins"
            else:
                result = "player2 wins"
        else:
            result='Invaild input! please enter rock paper scissor'
    return render(request, 'index.html', {
        'result':result,
        'player1':player1,
        'player2':player2,
    })'''

from django.shortcuts import render,redirect
from django.http import HttpResponse


def home(request):
    result=None
    if request.method == 'POST':
        a = int(request.POST.get('num1'))
        b = int(request.POST.get('num2'))
        o = request.POST.get('op')
        if o == 'add':
            result = a + b
        return redirect('hello',result)
    return render(request, 'index.html')
   
    
def hello(request):
    return render(request, 'result.html',{'result':result})
        
            

