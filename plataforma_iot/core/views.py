from django.shortcuts import render, redirect

# Create your views here.
from .models import DispositivoIoT

def cadastrar_dispositivo(request):
    if request.method == 'POST':
        serialNumber = request.POST['serialNumber']
        dados = request.POST['dados']
        
        # Verifique se os campos são válidos e não estão vazios
        if serialNumber and dados:
            # Crie um novo dispositivo IoT
            dispositivo = DispositivoIoT(serialNumber=serialNumber, dados=dados)
            dispositivo.save()
            return redirect('listar_dispositivos')

    return render(request, 'cadastro_dispositivo.html')

def listar_dispositivos(request):
    dispositivos = DispositivoIoT.objects.all()
    return render(request, 'listagem_dispositivos.html', {'dispositivos': dispositivos})
