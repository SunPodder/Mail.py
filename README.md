# Mail-py
Python library for sending emails.

## Usage

Import module and create instance:
```
from Mail import *

mail = Mail("sender@example.com", "password")
```
<br><br>
Set receiver's email address and subject:
```
mail.receiver = "receiver@example.com" #Receiver's email address
mail.subject = "Demo Mail" #email subject
```
<br><br>
Send a simple email:
```
mail.addText("Hello world!\nThis is a test mail.\nHappy Coding!")
#adds text to email body
mail.send()
```
<br><br>
Send mail in HTML format:
```
mail.addHTML("<h1>This is a heading</h1>") #Adds HTML code to email body. Can be used for formatting emails.
mail.send()
```
<br><br>
Add files via email attachment:
```
mail.attach("image.jpg")
mail.send()
```
