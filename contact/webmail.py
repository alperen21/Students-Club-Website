import smtplib
from email.mime.multipart import MIMEMultipart
import sys
from email.mime.text import MIMEText

def send_mail(email,body,name):
    
    #MIMEMultipart objesi oluşturdum.
    #Subject almıyorum çünkü her mailin başlığının "Yeni Website Mesajı" olmasını istiyorum
    message = MIMEMultipart()
    message["From"] = "mail"
    message["To"] = "mail"
    message["Subject"] = "Yeni Website Mesajı"
    body = "{} emailine sahip {} isimli kişiden yeni bir websitesi mesajı var\n\n".format(email,name) + body
    message_body = MIMEText(body,"plain")
    message.attach(message_body)

    #SMTP portuna bağlanıyorum
    #buradan sonrasını try içinde yazıyorum çünkü bir şeylerin yanlış gitme ihtimali var
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587) #587 numaralı gmail smtp'sine bağlanıyorum çünkü Google sadece bu portta smtp'ye izin veriyor.
        mail.ehlo() #gmaildeki smtp portuna bağlanmak için gerekiyor.
        mail.starttls() #enkripsiyon için
        mail.login("username", "password") #giriş yapmak için I'll switch to environment variables instead of hardcoding password / username and I'll use real email of the club.
        mail.sendmail(message["From"],message["To"],message.as_string())
        mail.close() #SMTP portu ile bağlantıyı kesmek için

        return True #websitesinde mail başarıyla gönderildi mesajı çıkması için bool döndürüyorum
    
    except:
        return False #websitesinde bir sorun çıktı mesajı çıkması için bool döndürüyorum






    