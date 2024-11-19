from gigachat import GigaChat


# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
giga = GigaChat(credentials='MjIyMWE1YjItZmExNi00ODNkLTlkYmEtNzYzNDU3NThjNjQ3OjYwYzYwOWExLTJmNTktNDhmOS1hNDYzLWI1OTY4MWUxZDQ5Mg==', verify_ssl_certs = False)
with open('prompt_file.txt', 'r') as file:
    request=file.read().replace('\n', '').replace('\r', '')
response = giga.chat(request)
file = open('example.txt', 'a')
# запись ответа в отдельный файл
file.write(f'{response.choices[0].message.content}, \n')
print(response.choices[0].message.content)