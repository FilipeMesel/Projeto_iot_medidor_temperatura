from django.shortcuts import render, redirect, get_object_or_404
from .models import DispositivoIoT
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Usado apenas para fins de demonstração, remova ou ajuste conforme necessário
def atualizar_dados_dispositivo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            serial_number = data.get('serialNumber')
            novo_json = data.get('novoJSON')

            # Verifique se os campos são válidos e não estão vazios
            if serial_number and novo_json:
                dispositivo, created = DispositivoIoT.objects.get_or_create(serialNumber=serial_number)
                dispositivo.dados = novo_json
                dispositivo.save()
                return JsonResponse({'message': 'Dados atualizados com sucesso'})
            else:
                return JsonResponse({'error': 'Campos inválidos ou vazios'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'})

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
