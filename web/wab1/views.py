from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



from .models import MultiStepFormModel
def index(request):
    # return render(request,'wab1/index2.html')
    return render(request,'wab1/multistepformexample.html')



def index2(request):
    score = 0
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    btemp = request.POST.get('temp')
    t = float(btemp)
    if t > 99.5:
        score = score + 2

    bp = request.POST.get('bprob','off')
    dp = request.POST.get('dprob','off')
    st = request.POST.get('Sorethroat','off')
    wk = request.POST.get('Weakness','off')
    rn = request.POST.get('Runnynose','off')


    if (bp == 'on' and score >= 3):
        score = score + 1
    elif (bp == 'on' and score < 3):
        score = score + 3

    if (dp == 'on' and score >= 3):
        score = score + 1
    elif (dp == 'on' and score < 3):
        score = score + 3

    if(st == 'on' and score >= 3):
        score = score + 1
    elif(st == 'on' and score < 3):
        score = score + 3

    if(wk == 'on' and score >= 3):
        score = score + 1
    elif(wk == 'on' and score < 3):
        score = score + 3

    if(rn == 'on' and score >= 3):
        score = score + 1
    elif(rn == 'on' and score < 3):
        score = score + 3
    total = score
    abpain = request.POST.get('approb', 'off')
    vm = request.POST.get('vprob', 'off')
    dia = request.POST.get('Diarrhoea', 'off')
    cp = request.POST.get('cpain', 'off')
    mp = request.POST.get('mpain', 'off')
    ps = request.POST.get('psmell', 'off')
    rsh = request.POST.get('rash', 'off')
    sph = request.POST.get('pspeech', 'off')

    if(abpain == 'on'):
        total = total + 2

    if(vm == 'on'):
        total = total + 2
    if(dia == 'on'):
        total = total + 2
    if(cp == 'on'):
        total = total + 2
    if(mp == 'on'):
        total = total + 2
    if(ps == 'on'):
        total = total + 2
    if(rsh == 'on'):
        total = total + 2
    if(sph == 'on'):
        total = total + 2

    param = {'total': total}
    if(total < 5):
        return render(request,'wab1/index1.html',param)
    elif(total == 5):
        return render(request,'wab1/index2.html',param)
    elif(total > 5 and total < 7):
        return render(request,'wab1/index3.html',param)
    elif(total > 7):
        return render(request,'wab1/index4.html',param)