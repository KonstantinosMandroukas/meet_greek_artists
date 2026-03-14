import mailtrap as mt
class Send_Email():
    def __init__(self, content:str):
        self.content = content
    def send(self):
        mail = mt.Mail(
        sender=mt.Address(email="konmanfts@demomailtrap.co", name="Mailtrap Test"),
        to=[mt.Address(email="konmanfts@gmail.com")],
        subject="Meet Greek Artists: New Artist Request",
        text=f"{self.content}",
        category="New Artist Request",
        )

        client = mt.MailtrapClient(token="d0e086171bef2fe7ac6e7f602d80c7d1")
        response = client.send(mail)