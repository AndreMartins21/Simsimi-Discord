import requests

def simsimi(question):
  '''
  Função para fazer a requisição HTTP à API do Simsimi já com a mensagem digitada pelo usuário
  '''

  request = requests.get(f'https://api.simsimi.net/v1/?text={question}%C3%A1&lang=pt&cf=false')
  api = request.json()
  return api["success"] # Retorna a mensagem de resposta  
