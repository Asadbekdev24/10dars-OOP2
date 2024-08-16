import os
os.system("cls")

class BankAccount:
    _balance=1200
    _ownerName="Asadbek"
    _ownerID=7
    _ownerPhoneNumber=995551133
    _paymentHistory={
       "CurrentTime": {
        "to":"id=7",
        "when":"12:15",
        "summa":1500
    }

    }

    def getAccountInfo(self):
        print(f"""
Balans = {self._balance},
User ismi = {self._ownerName},
User id = {self._ownerID},
User telefon nomeri = {self._ownerPhoneNumber},
Payment tarixi = {self._paymentHistory}
""")

    def getPaymentHistory(self):
        print(self._paymentHistory)

    def getOwnerId(self):
        print(self._ownerID)

    def getOwnerName(self):
        return (self._ownerName)
    def getBalance(self):
        return (self._balance)

    def setName(self, ism:str):
        self._ownerName=ism

    def setPhoneNumber(self, number:str):
        num1=["99891", "99899","99897", "99894","99893"]
        for el in num1:
            if el in number:
                self._ownerPhoneNumber=number
                break

    def addBalance(self, pul:int):
        if pul>0:
           self._balance+=pul

    def withdrawBalance(self, ayirma:float):
        if self._balance-ayirma<0:
            print("false")
        else:
            self._balance-=ayirma
            print("true")

    def transfer(self, obyekt):
        obyekt.addBalance(self._balance)
        return f"{obyekt.getOwnerName()} balansi "+ str(obyekt.getBalance()) +" ga oshdi"


hisob=BankAccount()
hisob2=BankAccount()

hisob2.setName("Bahodir")
hisob2.setPhoneNumber("998931252132")


hisob.getAccountInfo()

print("Nomer o'zgartirish amali bajarildi")
print("Balansda o'zgarish sodir bo'ldi")
print("Bir odamdan ikkinchi odam hisobiga pul o'tkazish amali bajrildi")

hisob.addBalance(1500)
hisob.setPhoneNumber("998912221225")

natija=hisob.transfer(hisob2)
print(natija)

hisob.getAccountInfo()

hisob2.getAccountInfo()
