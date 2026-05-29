import mailtrap as mt
class Send_Email():
    def __init__(self, content:str, action):
        self.content = content
        self.action = action
    def send(self):
        if self.action == 'request':
            self.subject = "Meet Greek Artists: New Artist Request"
        elif self.action == 'report':
            self.subject = "Meet Greek Artists: Report Problem"
        mail = mt.Mail(
        sender=mt.Address(email="konmanfts@demomailtrap.co", name="Mailtrap Test"),
        to=[mt.Address(email="konmanfts@gmail.com")],
        subject=self.subject,
        text=f"{self.content}",
        category="New Artist Request/ Problem report",
        )

        client = mt.MailtrapClient(token="d0e086171bef2fe7ac6e7f602d80c7d1")
        response = client.send(mail)