# -*- coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Recibo
from .forms import reciboForm
from datetime import date

#Página inicial donde se listan las facturas
def index(request):
	template = loader.get_template('recibo/index.html')
	recibos = Recibo.objects.all()
	context = {
		'recibos': recibos,
	}
	return HttpResponse(template.render(context, request))

#Formulario para actualizar recibo
def actRecibo(request, recId):
	rec = Recibo.objects.get(id=recId)
	template = loader.get_template('recibo/actRecibo.html')
	fechaPago = rec.fechaPago
	fechaF = date(fechaPago.year, fechaPago.month, fechaPago.day)
	context = {
		'idRecibo': recId,
		'titulo': 'Actualización de Recibo',
		'action': 'Actualizar',
		'Numrec': rec.numRecibo,
		'Fecharec': fechaF.strftime("%Y-%m-%d"),
		'Cantrec': rec.cantidad,
		'Clienterec': rec.cliente,
		'Conceptorec': rec.concepto,
	}
	return HttpResponse(template.render(context, request))

#Acción Actualizar Recibo
def actualizar(request, recId):
	template = loader.get_template('recibo/index.html')
	numeroN = request.POST.get('numRecibo')
	clienteN = request.POST.get('cliente')
	fechaN = request.POST.get('fechaPago')
	cantidadN = request.POST.get('cantidad')
	conceptoN = request.POST.get('concepto')

	rec = Recibo.objects.get(id=recId)
	rec.numRecibo = numeroN
	rec.cliente = clienteN
	rec.fechaPago = fechaN
	rec.cantidad = cantidadN
	rec.concepto = conceptoN

	rec.save()
	context = {}

	return redirect('/recibo/')


def crearRecibo (request):
	if request.method == "POST":
		form = reciboForm(request.POST)
		if form.is_valid():
			recib = form.save(commit=False)
			recib.numRecibo=request.POST["numRecibo"]
			recib.fechaPago=request.POST["fechaPago"]
			recib.cliente=request.POST["cliente"]
			recib.concepto=request.POST["concepto"]
			recib.cantidad=request.POST["cantidad"]
			recib.save()
			return redirect('/recibo/')
	else:
		form = reciboForm()
	return render(request, 'recibo/crear.html', {'form': form})


def eliminarRecibo(request, recId):
	recib= Recibo.objects.get(pk=recId)
	recib.delete()
	return redirect('/recibo/')
