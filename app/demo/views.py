# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from demo.models import *
from demo.forms import *

def index_view(request):
	cadena = "Hola mario"
	return HttpResponse(cadena)


def post(request, id):
	# aca se consulta la bd para obtener la info
	return HttpResponse("Este es el post %s" %id)

def hora_actual(request):
	ahora = datetime.now()
	
	#t = get_template('template1.html')
	#c = Context({'hora': ahora})
	#html = t.render(c)
	#return HttpResponse(html)

	#otra alternativa
	usuario = "Mario"
	rango = range(1,10)
	return render_to_response('template1.html', {'hora': ahora, 'usuario': usuario, 'rango': rango})

def agregar(request):
	template = "agregar.html"

	if request.method == "POST":
		form = LibroForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = LibroForm()
	
	data = {'form': form}
	return render_to_response(template, context_instance=RequestContext(request, data))

def home(request):
	template = "galeria.html"
	galeria = Libro.objects.all()
	return render_to_response(template, context_instance=RequestContext(request, {'libros': galeria}))