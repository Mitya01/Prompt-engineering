from gigachat import GigaChat


# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
def generate_questions(credentials_generate: str, vacancy_text: str) -> str:
    giga = GigaChat(credentials = credentials_generate, verify_ssl_certs = False)
    request_giga = """Представь, что ты рекрутер, который ищет кандидата на позицию """
    request_giga += vacancy_text.partition('\n')[0]
    request_giga += """, при этом кандидат должен подходить по требованиям, представленным в описании вакансии. Сформулируй 5 технических скрининговых вопросов, основываясь на описании вакансии и примерах 5 скрининговых вопросов для разработчика на языке программирования Python. Вопросы должны быть краткими, понятными и соответствовать уровню знаний, необходимому для выполнения работы. Убедись, что скрининговые вопросы затрагивают несколько обязанностей и требований, предъявляемых кандидату. Описание вакансии:"""
    for index in range(1, len(vacancy_text.partition('\n'))):
        request_giga += vacancy_text.partition('\n')[index]
    request_giga += """Выведи ответ в таком же формате, как и в примере
Пример 5 скрининговых вопросов для разработчика на языке программирования Python.

1. Что такое Python и перечислите некоторые из его ключевых функций.

2. Что такое cписки и кортежи в Python?

3. В чём разница между изменяемым типом данных и неизменяемым типом данных?

4. Можете ли вы объяснить распространённые обхода графов в Python?

5. Что такое ошибка KeyError в Python и как с этим справиться?"""
    response = giga.chat(request_giga)
    return response.choices[0].message.content

# print(generate_questions('MjIyMWE1YjItZmExNi00ODNkLTlkYmEtNzYzNDU3NThjNjQ3OjYwYzYwOWExLTJmNTktNDhmOS1hNDYzLWI1OTY4MWUxZDQ5Mg==', """Middle Backend Python разработчик
# Обязанности:

# разработка и проектирование ПО;
# разработка ПО от R&D до корпоративного решения (Enterprise) - «трансфер технологий»;
# Code Review.
# Требования:

# умение писать чистый и поддерживаемый код;
# покрытие кода тестами;
# понимание принципов построения микросервисной архитектуры и опыт разработки микросервисов;
# понимание принципов REST.
# Требования по стеку:

# FastAPI + SQLAlchemy;
# docker, docker-compose;
# PostgreSQL, Redis;
# работа с асинхронностью."""))

