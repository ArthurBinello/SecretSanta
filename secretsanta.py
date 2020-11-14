from random import shuffle
import smtplib
from email.mime.text import MIMEText

print("Pere Noel secret de Thanksgiving")
persons = []

while(1):
	name = input("Nom du participant (exit pour quitter) : ")
	if(name == "exit"):
		break
	address = input("Adresse du participant : ")
	mail = input("Email du participant : ")
	persons.append([name, address, mail])

shuffle(persons)

login = input("Login : ")
password = input("password for " + login + " : ")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(login, password)
for idx, p in enumerate(persons):
	from_ = login
	to_ = p[2]
	next_ = persons[(idx + 1) % len(persons)]
	header  = 'From: ' + from_ + '\n'
	header += 'To: ' + to_ + '\n'
	header += 'Subject: Pere Noel secret de Thanksgiving' + '\n'
	message = "Ton destinataire est : " + next_[0] + '\nSon adresse est : ' + next_[1]
	message = header + '\n' + message
	s.sendmail(from_, [to_], message)
print("Successfully sent emails")
s.quit()