import smtplib, ssl


def sendEmail(message):
    host = 'smtp.gmail.com'
    port = 465

    password = 'mefscnqbsrfcriwi'
    username = 'lucascsantana6@gmail.com'
    receiver = 'lucascsantana6@gmail.com'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


