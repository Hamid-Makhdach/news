from django.shortcuts import render
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import PredictedParagraph






def home(request):
    return render(request, 'index.html')





def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='singin')
def predict_paragraph(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        title=request.POST.get('titre')
        category = request.POST.get('categ')

        # Charger le modèle pré-entrainé
        with open('ml_model/fakenews.pkl', 'rb') as f:
            model = pickle.load(f)

        # Charger le vecteur TF-IDF pré-entrainé
        with open('ml_model/tfidfvect2.pkl', 'rb') as f:
            tfidf_vectorizer = pickle.load(f)

        # Prédire les paragraphes
        paragraphs = text.split("\n")

        # Vectoriser les paragraphes avec TF-IDF
        paragraph_vectors = tfidf_vectorizer.transform(paragraphs)

        # Prédire les classes et les probabilités
        predictions = model.predict(paragraph_vectors)
        #probabilities = model.predict_proba(paragraph_vectors)

        # Préparer les données pour l'affichage
        colored_paragraphs = []
        true_probability=0
        num_fake = 0
        num_total = len(paragraphs)
        

        for p, pred,  in zip(paragraphs, predictions):
            if pred == 'fausse':
                colored_paragraphs.append('<span style="color: red;">' + p + '</span>')
                num_fake += 1
                title
                
            else:
                colored_paragraphs.append('<span style="color: blue;">' + p + '</span>')
                title

        colored_text = '<br>'.join(colored_paragraphs)
        
        fake_probability = (num_fake / num_total )*100
        true_probability=100-fake_probability

        request.session['predicted_paragraphs'] = colored_paragraphs
        
        
        predicted_paragraph = PredictedParagraph(

            text=colored_text,
            fake_p=fake_probability,
            true_p=true_probability,
            titre=title,
            category=category  
            
        )
        predicted_paragraph.save()

        return render(request, 'Prediction.html', {'colored_text': colored_text, 'fake_probability': fake_probability, 'true_probability': true_probability,  'titre': title, 'category':category })

    return render(request, 'Prediction.html')





def hist_view(request):
    predicted_paragraphs = PredictedParagraph.objects.all()
    
    return render(request, 'hist.html', {'predicted_paragraphs': predicted_paragraphs})

def poli_view(request):
    predicted_paragraphs = PredictedParagraph.objects.all()
    
    return render(request, 'poli.html', {'predicted_paragraphs': predicted_paragraphs})


def eco_view(request):
    predicted_paragraphs = PredictedParagraph.objects.all()
    
    return render(request, 'eco.html', {'predicted_paragraphs': predicted_paragraphs})


def sport_view(request):
    predicted_paragraphs = PredictedParagraph.objects.all()
    
    return render(request, 'sport.html', {'predicted_paragraphs': predicted_paragraphs})


  
     



def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Votre mot de passe et votre mot de passe de confirmation ne sont pas les mêmes !!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('singin')
        

    return render (request,'register.html')




def singin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('predict')
        else:
            return HttpResponse ("Le nom d'utilisateur ou le mot de passe est incorrect!!!")
    return render(request, 'singin.html')



def Logout(request):
    logout(request)
    return redirect('home')





def about(request):
    return render(request, 'about.html')