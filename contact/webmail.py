import smtplib
from email.mime.multipart import MIMEMultipart
import sys
from email.mime.text import MIMEText

def send_mail(email,body,name):
    
    #MIMEMultipart objesi oluşturdum.
    #Subject almıyorum çünkü her mailin başlığının "Yeni Website Mesajı" olmasını istiyorum
    message = MIMEMultipart()
    message["From"] = "alperenbot086@gmail.com"
    message["To"] = "alperenmac21@icloud.com"
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
        mail.login("alperenbot086@gmail.com", "akjadf14352") #giriş yapmak için
        mail.sendmail(message["From"],message["To"],message.as_string())
        mail.close() #SMTP portu ile bağlantıyı kesmek için

        return True #websitesinde mail başarıyla gönderildi mesajı çıkması için bool döndürüyorum
    
    except:
        return False #websitesinde bir sorun çıktı mesajı çıkması için bool döndürüyorum






    