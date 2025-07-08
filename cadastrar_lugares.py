import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings') 
django.setup()

from projeto.models import Lugar  # ajuste 'app' para o nome do seu app
from datetime import datetime

def cadastrar_lugares():
    lugares = [
        {
            "nome": "Biblioteca Central",
            "local": "Bloco A",
            "horario_abre": "08:00",
            "horario_fecha": "22:00",
            "descricao": "Principal biblioteca da UCS, com amplo acervo e espaços de estudo.",
        },
        {
            "nome": "Cantina do Bloco B",
            "local": "Bloco B",
            "horario_abre": "07:30",
            "horario_fecha": "18:00",
            "descricao": "Cantina com lanches, refeições rápidas e café.",
        },
        {
            "nome": "Auditório Principal",
            "local": "Bloco C",
            "horario_abre": "08:00",
            "horario_fecha": "20:00",
            "descricao": "Auditório para palestras, eventos e reuniões.",
        },
        {
            "nome": "Laboratório de Informática",
            "local": "Bloco D",
            "horario_abre": "07:00",
            "horario_fecha": "22:00",
            "descricao": "Laboratório equipado com computadores para aulas e pesquisas.",
        },
        {
            "nome": "Sala de Estudos 101",
            "local": "Bloco E",
            "horario_abre": "08:00",
            "horario_fecha": "21:00",
            "descricao": "Sala silenciosa para estudos individuais ou em grupo.",
        },
        {
            "nome": "Ginásio Poliesportivo",
            "local": "Bloco F",
            "horario_abre": "06:00",
            "horario_fecha": "22:00",
            "descricao": "Espaço para atividades esportivas e eventos físicos.",
        },
        {
            "nome": "Centro de Atendimento ao Aluno",
            "local": "Bloco G",
            "horario_abre": "09:00",
            "horario_fecha": "17:00",
            "descricao": "Local para suporte e informações aos estudantes.",
        },
        {
            "nome": "Parque das Araucárias",
            "local": "Área externa",
            "horario_abre": "06:00",
            "horario_fecha": "23:00",
            "descricao": "Área verde para lazer e descanso no campus.",
        },
    ]

    for lugar_data in lugares:
        abrir = datetime.strptime(lugar_data["horario_abre"], "%H:%M").time()
        fechar = datetime.strptime(lugar_data["horario_fecha"], "%H:%M").time()

        lugar, criado = Lugar.objects.get_or_create(
            nome=lugar_data["nome"],
            defaults={
                "local": lugar_data["local"],
                "horario_abre": abrir,
                "horario_fecha": fechar,
                "descricao": lugar_data["descricao"],
            }
        )
        if criado:
            print(f"Criado: {lugar.nome}")
        else:
            print(f"Já existe: {lugar.nome}")

if __name__ == "__main__":
    cadastrar_lugares()
