# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os


def sendEmail(nome, email):

    # import credentials
    load_dotenv(verbose=True)
    password = os.getenv("PASSWORD")  # password do sender

    # create message object instance
    msg = MIMEMultipart()

    body = f""" 

    Olá, {nome}. Tudo bem?

    Foi identificado que seu saldo em conta corrente não é suficiente para suas obrigações de hoje!

    Favor reconsiderar gastos! 

    Segue abaixo registro da última transação feita:

    Atenciosamente,

    Equipe ABC Brasil

    """

    # setup the parameters of the message
    msg['From'] = "lucasmuchaluat@gmail.com"  # email do sender
    msg['Subject'] = "[URGENTE] Saldo Insuficiente"
    msg['To'] = email  # receiver

    # add in the message body
    msg.attach(MIMEText(body, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print(f"successfully sent email to {email}")
