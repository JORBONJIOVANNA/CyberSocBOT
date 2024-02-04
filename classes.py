class Captcha:
    def __init__(self,captcha,user, word) -> None:
        self.captcha = captcha
        self.user = user
        self.word = word

    def verify_captcha(self,u_input)->bool:
        return self.word == u_input
    

class Rule:
    def __init__(self,txt:str) -> None:
        delim_txt= txt.split(";")
        self.title = delim_txt[0]
        self.msg = delim_txt[1]
        self.colour = delim_txt[2]

    def hex_to_rgb(self)->tuple:
        rgb = []
        for x in range(0,6,2):
            rgb.append(int(f"{self.colour[x+1]}{self.colour[x]}",16))
        return tuple(rgb)