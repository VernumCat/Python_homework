def send_email(message, recipient, *, sender='university.help@gmail.com'):
    recipient_ru = recipient[-3] + recipient[-2] + recipient[-1]
    sender_ru = sender[-3] + sender[-2] + sender[-1]
    recipient_com_net = recipient[-4] + recipient_ru
    sender_com_net = sender[-4] + sender_ru
    domen = ['.com', '.net']
    recipient_domen = False
    sender_domen = False
    if recipient_ru == '.ru' or recipient_com_net in domen:
        recipient_domen = True
    if sender_ru == '.ru' or sender_com_net in domen:
        sender_domen = True
    if recipient.find('@') == -1 or sender.find('@') == -1 or recipient_domen != True or sender_domen != True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}!')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
