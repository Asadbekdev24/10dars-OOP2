import os
os.system("cls")

class Texnika:
    def __init__(self, brand:str, model:str,tipi:str) -> None:
        self.model=model
        self.brand=brand
        self.tipi=tipi
    def more_info(self):
        return (f"""
Brend = {self.brand}
Model = {self.model}
Tipi = {self.tipi}""" )



class Noutbuk(Texnika):

    def __init__(self, brand: str, model: str, tipi: str, video_card:str, ram:str, dislplay:str) -> None:
        super().__init__(brand, model, tipi)
        self.video_card=video_card
        self.ram=ram
        self.display=dislplay

    def more_info(self) -> str:
        return super().more_info() + f"""
Video karta = {self.video_card}
Ram = {self.ram}
Displayi = {self.display}
        """

class Televisor(Texnika):
    def __init__(self, brand: str, model: str, tipi: str, size:int, display:str) -> None:
        super().__init__(brand, model, tipi)
        self.size=size
        self.display=display

    def more_info(self):
        return super().more_info()+ f"""
O'lchami = {self.size}
Display = {self.display}
"""

class Smartphone(Texnika):
    def __init__(self, brand: str, model: str, tipi: str, size:int, sim_count:int) -> None:
        super().__init__(brand, model, tipi)
        self.size=size
        self.sim_count=sim_count
    def more_info(self):
        return super().more_info()+f"""
O'lchami = {self.size}
Sim karta slot = {self.size}
"""

hp=Noutbuk("HP", "game3", "oddiy","Gtx","8 GB", "15.6 dyum")
artel=Televisor("Artel", "v2", "premium", 1500, "15.6 dyum" )
tel=Smartphone("Samsung", "A34","oddiy", 15, 2)

print(hp.more_info())
print(artel.more_info())
print(tel.more_info())
