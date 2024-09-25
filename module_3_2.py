def send_email(message, recipient, *, sender='university.help@gmail.com'):
    adres1 = recipient[-4] + recipient[-3] + recipient[-2] + recipient[-1]
    adres2 = sender[-4] + sender[-3] + sender[-2] + sender[-1]
    adres3 = ['.com', '.ru', '.net']
    if recipient.find('@') == -1 or sender.find('@') == -1 or adres1 not in adres3 or adres2 not in adres3:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}!')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
