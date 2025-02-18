import requests
from bs4 import BeautifulSoup

class Arabam_API():
    """arabam.com 3. taraf python api wrapper"""
    def __init__(self):
        pass

    def sayfacek(self , link:str): 
        """girmis oldugunuz linkteki sayfalari listenin icerisine sozluk olarak kaydediyor.
        listenin belirli bir elemanini dondukten sonra istediginiz elemani sozluk olarak secebilirsiniz
        
        ornek kullanim:
        
        dict(arabam.sayfacek[1]).get("fiyat")


        keys:
        fiyat , url , resim , model
        """
        carlist = []
        req = requests.get(url=link)
        soup = BeautifulSoup(req.content, 'html5lib')
        cars = soup.find_all(name='div', attrs = {"class":"visible-on-parent-hover toolbox-wrapper"})
        for car in cars:
            main = car.find(name="span",attrs={"class":"toolbox-item","id":lambda value: value and value.startswith("compare")})
            newlist = str(main).splitlines()
            filtered = (str(newlist).split("Popup({",1)[1].split("}, ev",1)[0])
            carspec = filtered.split("\\")
            specs = {
                    "fiyat":carspec[3],
                    "url":carspec[5],
                    "resim":carspec[7].removeprefix("'"),
                    "model":carspec[11],
            }

            carlist.append(specs)
        return carlist
    
    def arabacek(self,link:str):
        """
        verilen arabanin tum detaylarini siteden ceker
        """
        alin = []
        req = requests.get(url=link)
        soup = BeautifulSoup(req.content, 'html5lib')
        car = soup.find(name='div', attrs = {"class":"product-properties"}).find_all(name='div', attrs = {"class":"property-value"})
        for i in car:
            carspec = i.find(text=True, recursive=False)
            alin.append(carspec)
        alin.pop(0)
        return alin
        
arabamcom = Arabam_API()