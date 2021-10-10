import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail:
  def __init__(self, email, password):
    self.email = ""
    self.password = ""
    self.receiver = ""
    self.port = 465
    self.message = MIMEMultipart()
    self.subject = ""
    self.context = ssl.create_default_context()
    
    if email:
      self.email = email
    if password:
      self.password = password
  
  def send(self):
    self.__set()
    with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
      server.login(self.email, self.password)
      server.sendmail(self.email, self.receiver, self.message.as_string())
      
  def attach(self, image):
    with open(image, "rb") as attachment:
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())
      encoders.encode_base64(part)
      part.add_header(
        "Content-Disposition",
        f"attachment; filename= {image}",
      )
      self.message.attach(part)
  
  def addText(self, text):
    self.message.attach(MIMEText(text, 'plain'))
  
  def addHTML(self, html):
    self.message.attach(MIMEText(html, 'html'))
        
  def __set(self):
    self.message["From"] = self.email
    self.message["To"] = self.receiver
    self.message["Subject"] = self.subject