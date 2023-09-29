from django.shortcuts import render, redirect, get_object_or_404
from .models import DispositivoIoT
from django.http import JsonResponse

def atualizar_dados_dispositivo(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serialNumber')
        novo_json = request.POST.get('novoJSON')
        
        # Verifique se os campos são válidos e não estão vazios
        if serial_number and novo_json:
            dispositivo = get_object_or_404(DispositivoIoT, serialNumber=serial_number)
            dispositivo.dados = novo_json
            dispositivo.save()
            return JsonResponse({'message': 'Dados atualizados com sucesso'})
        else:
            return JsonResponse({'error': 'Campos inválidos ou vazios'})

    return JsonResponse({'error': 'Método não permitido'})


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
