from django.shortcuts import render, redirect, HttpResponse, render_to_response
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from marketapp.models import Tovar, Sklad, Postavschik, Postavka
from marketapp.serializers import TovarSerializer, SkladSerializer, PostavschikSerializer, PostavkaSerializer
from marketapp.forms import TovarForm, SkladForm, PostavschikForm, PostavkaForm
from django.db import connection
import csv

def index(request):
	return render(request, "marketapp/index.html")

def tovar_view(request):
	tovar = Tovar.objects.all().order_by("-id")
	return render(request, "marketapp/tovar.html",{'tovars': tovar})

def sklad_view(request):
	sklad = Sklad.objects.all().order_by("-id")
	return render(request, "marketapp/sklad.html",{'sklads': sklad})

def postavschik_view(request):
	postavschik = Postavschik.objects.all().order_by("-id")
	return render(request, "marketapp/postavschik.html",{'postavschiks': postavschik})

def postavka_view(request):
	postavka = Postavka.objects.all().order_by("-id")
	return render(request, "marketapp/postavka.html",{'postavkas': postavka})



def tovaradd(request):
	form = TovarForm()

	if request.method == "POST":
		form = TovarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(tovar_view)
	return render(request, "marketapp/tovaradd.html",{'form': form})


def tovaredit(request, tovar_id):
	form = TovarForm(instance = Tovar.objects.get(id = tovar_id))

	if request.method == "POST":
		form = TovarForm(request.POST, request.FILES, instance = Tovar.objects.get(id = tovar_id))
		if form.is_valid():
			tovar = form.save()
			return redirect(tovar_view)
	return render(request, "marketapp/tovaredit.html", {"form": form})

def tovardelete(request, tovar_id):
		tovar = Tovar.objects.get(id=tovar_id)
		tovar.delete()
		return redirect(tovar_view)



def skladadd(request):
	form = SkladForm()

	if request.method == "POST":
		form = SkladForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(sklad_view)
	return render(request, "marketapp/skladadd.html",{'form': form})

def skladedit(request, sklad_id):
	form = SkladForm(instance = Sklad.objects.get(id = sklad_id))

	if request.method == "POST":
		form = SkladForm(request.POST, request.FILES, instance = Sklad.objects.get(id = sklad_id))
		if form.is_valid():
			sklad = form.save()
			return redirect(sklad_view)
	return render(request, "marketapp/skladedit.html", {"form": form})

def skladdelete(request, sklad_id):
		sklad = Sklad.objects.get(id=sklad_id)
		sklad.delete()
		return redirect(sklad_view)



def postavkaadd(request):
	form = PostavkaForm()
	form1 = SkladForm()

	if request.method == "POST":
		form = PostavkaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(postavka_view)
	return render(request, "marketapp/postavkaadd.html",{'form': form})


def postavkaedit(request, postavka_id):
	form = PostavkaForm(instance = Postavka.objects.get(id = postavka_id))

	if request.method == "POST":
		form = PostavkaForm(request.POST, request.FILES, instance = Postavka.objects.get(id = postavka_id))
		if form.is_valid():
			postavka = form.save()
			return redirect(postavka_view)
	return render(request, "marketapp/postavkaedit.html", {"form": form})

def postavkadelete(request, postavka_id):
		postavka = Postavka.objects.get(id=postavka_id)
		postavka.delete()
		return redirect(postavka_view)



def postavschikadd(request):
	form = PostavschikForm()

	if request.method == "POST":
		form = PostavschikForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(postavschik_view)
	return render(request, "marketapp/postavschikadd.html",{'form': form})


def postavschikedit(request, postavschik_id):
	form = PostavschikForm(instance = Postavschik.objects.get(id = postavschik_id))

	if request.method == "POST":
		form = PostavschikForm(request.POST, request.FILES, instance = Postavschik.objects.get(id = postavschik_id))
		if form.is_valid():
			postavschik = form.save()
			return redirect(postavschik_view)
	return render(request, "marketapp/postavschikedit.html", {"form": form})

def postavschikdelete(request, postavschik_id):
		postavschik = Postavschik.objects.get(id=postavschik_id)
		postavschik.delete()
		return redirect(postavschik_view)

# API

class TovarList(ListCreateAPIView):
    serializer_class = TovarSerializer
    queryset = Tovar.objects.all()

class TovarDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TovarSerializer
    queryset = Tovar.objects.all()

class SkladList(ListCreateAPIView):
    serializer_class = SkladSerializer
    queryset = Sklad.objects.all()

class SkladDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SkladSerializer
    queryset = Sklad.objects.all()

class PostavschikList(ListCreateAPIView):
    serializer_class = PostavschikSerializer
    queryset = Postavschik.objects.all()

class PostavschikDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PostavschikSerializer
    queryset = Postavschik.objects.all()

class PostavkaList(ListCreateAPIView):
    serializer_class = PostavkaSerializer
    queryset = Postavka.objects.all()

class PostavkaDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PostavkaSerializer
    queryset = Postavka.objects.all()


#CSV
def tovar_csv(request):
    file = 'tovar.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file
    tovar = Tovar.objects.all()
    writer = csv.writer(response, delimiter=';')
    for i in tovar:
        writer.writerow([i.code, i.name, i.price])
    return response

def sklad_csv(request):
    file = 'sklad.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file
    sklad = Sklad.objects.all()
    writer = csv.writer(response, delimiter=';')
    for i in sklad:
        writer.writerow([i.code, i.count])
    return response

def postavka_csv(request):
    file = 'postavka.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file
    postavka = Postavka.objects.all()
    writer = csv.writer(response, delimiter=';')
    for i in postavka:
        writer.writerow([i.date, i.count_post, i.code, i.postavschik])
    return response

def postavschik_csv(request):
    file = 'postavschik.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file
    postavschik = Postavschik.objects.all()
    writer = csv.writer(response, delimiter=';')
    for i in postavschik:
        writer.writerow([i.ogrn, i.name, i.phone])
    return response