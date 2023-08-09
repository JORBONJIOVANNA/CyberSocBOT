class Captcha:
    def __init__(self,captcha,user, word) -> None:
        self.captcha = captcha
        self.user = user
        self.word = word

    def verify_captcha(self,u_input):
        return self.word == u_input