from django.shortcuts import render, redirect
from clubDeportivo.models import dictInstructores, dictEquipos, dictMantenciones
from datetime import datetime

# Create your views here.
def inicio(request):
    return render(request,'clubDeportivo/inicio.html')

def dashboard(request):
    # Cantidad de equipos en mantenimiento
    equipos_mantenimiento = sum(1 for equipo in dictEquipos.values() if equipo['estado'] == 'En mantenimiento')

    # Cantidad de instructores
    cantidad_instructores = len(dictInstructores)

    # Cantidad de mantenimientos realizados y por venir
    hoy = datetime.today().date()
    
    # Convirtiendo las fechas de string a datetime antes de comparar
    mantenimientos_realizados = sum(1 for mantencion in dictMantenciones.values() if datetime.strptime(mantencion['fecha'], '%Y-%m-%d').date() < hoy)
    mantenimientos_por_venir = sum(1 for mantencion in dictMantenciones.values() if datetime.strptime(mantencion['fecha'], '%Y-%m-%d').date() >= hoy)

    # Cantidad de equipos en estado de falla
    equipos_falla = sum(1 for equipo in dictEquipos.values() if equipo['estado'] == 'Falla')

    data = {
        'equipos_mantenimiento': equipos_mantenimiento,
        'cantidad_instructores': cantidad_instructores,
        'mantenimientos_realizados': mantenimientos_realizados,
        'mantenimientos_por_venir': mantenimientos_por_venir,
        'equipos_falla': equipos_falla,
    }

    return render(request, 'clubDeportivo/dashboard.html', data)



##################################################################################################################################################################################################################################
def inventarioequipos(request):
    data = {
    'dictEquipos':dictEquipos,        
    }
    return render(request,'clubDeportivo/inventarioequipos.html',data)

def equipo(request, id=None):
    equipo = None
    if id is not None:
        equipo = dictEquipos.get(id, None)
        if not equipo:
            return redirect('inventarioequipos')

    if request.method == 'POST':
        nombre = request.POST['nombre']
        estado = request.POST['estado']
        modelo = request.POST['modelo']
        ubicacion = request.POST['ubicacion']


        if equipo:
            dictEquipos[id] = {
                'nombre': nombre,
                'estado': estado,
                'modelo': modelo,
                'ubicacion': ubicacion,
            }
        else:
            nuevo_id = max(dictEquipos.keys()) + 1
            dictEquipos[nuevo_id] = {
                'nombre': nombre,
                'estado': estado,
                'modelo': modelo,  
                'ubicacion': ubicacion,
            }

        return redirect('inventarioequipos')

    return render(request, 'clubDeportivo/equipo.html', {'equipo': equipo})

def eliminar_equipo(request, id):
    if id in dictEquipos:
        del dictEquipos[id]

    return redirect('inventarioequipos')



##################################################################################################################################################################################################################################

def instructores(request):
    data = {
        'dictInstructores':dictInstructores,
    }
    return render(request,'clubDeportivo/instructores.html', data)

def instructor(request,id=None):
    instructor = None
    if id is not None:
        instructor = dictInstructores.get(id, None)
        if not instructor:
            return redirect('instructores')
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        area = request.POST['area']
        ubicacion = request.POST['ubicacion']
        fecha_ingreso = request.POST['fecha_ingreso']
        
        nuevo_id = max(dictInstructores.keys()) + 1
        
        dictInstructores[nuevo_id] = {
            'rut': rut,
            'nombre': nombre,
            'categoria': categoria,
            'area': area,
            'ubicacion': ubicacion,
            'fecha_ingreso': fecha_ingreso,
        }

        return redirect('instructores')

    return render(request, 'clubDeportivo/instructor.html',{'instructor':instructor})


def eliminar_instructor(request, id):
    if id in dictInstructores:
        del dictInstructores[id]
        
    return redirect('instructores')
################################################################################################################################################################################################



def mantenciones(request):
    data = {
        'dictMantenciones':dictMantenciones,
    }
    return render(request,'clubDeportivo/mantenciones.html',data)

def mantencion(request, id=None):
    if id:
        mantencion = dictMantenciones.get(id)
        if not mantencion:
            return redirect('mantenciones')
    else:
        mantencion = None
    
    if request.method == 'POST':

        fecha = request.POST['fecha']
        hora = request.POST['hora']
        ubicacion = request.POST['ubicacion']

        if mantencion:  
            dictMantenciones[id] = {
                'fecha': fecha,
                'hora': hora,
                'ubicacion': ubicacion,
            }
        else:  
            nuevo_id = max(dictMantenciones.keys(), default=0) + 1
            dictMantenciones[nuevo_id] = {
                'fecha': fecha,
                'hora': hora,
                'ubicacion': ubicacion,
            }

        return redirect('mantenciones')  


    return render(request, 'clubDeportivo/mantencion.html', {'mantencion': mantencion})



def eliminar_mantencion(request, id):
    if id in dictMantenciones:
        del dictMantenciones[id]
        
    return redirect('mantenciones')

def calendario(request):
    eventos = []
    for mantencion in dictMantenciones.values():
        # Convertir la fecha de string a datetime
        try:
            fecha_mantencion = datetime.strptime(mantencion['fecha'], '%Y-%m-%d').date()
            hora_mantencion = mantencion['hora']  # Asume que está en formato HH:MM
            ubicacion = mantencion['ubicacion']

            # Crear evento con hora y ubicación
            eventos.append({
                'title': f"{hora_mantencion} - {ubicacion}",
                'start': f"{fecha_mantencion}T{hora_mantencion}"  # Formato ISO para fecha y hora
            })
        except KeyError as e:
            print(f"Error en mantención: falta el campo {str(e)}")

    return render(request, 'clubDeportivo/calendario.html', {'eventos': eventos})