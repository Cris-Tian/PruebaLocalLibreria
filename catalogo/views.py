from django.shortcuts import render

# Create your views here.
def index(request):
	"""
	
	Función vista para la pagina inicio del sitio
	"""
	# Genera contadores de algunos de los objetos principales
	num_books=book.objects.all().count()
	num_instance=bookInstance.objects.all().count()
	# Libros disponibles(status = 'a')
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count() #El 'all()' esta implicito por defecto.
	
	#Renderiza la plantilla HTML index.html con los datos en la variable contexto
	return render(
	request,
	'index.html',
	context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
	
	)
