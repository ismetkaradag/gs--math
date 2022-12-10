import time
import requests
from bs4 import BeautifulSoup as bs
url = "http://math.gsu.edu.tr/mezun/mezun%20sayfasi.html"
r = requests.get(url)
soup = bs(r.content,'html.parser')
a = soup.find_all("div","bioCard")
class Mezun:
    def __init__(self,isim,image,bilgiler):
        self.isim = isim
        self.image = image
        self.bilgiler = bilgiler
        
y = 0
for i in a:
    y +=1
    if y ==50:
        time.sleep(30)
    image = i.find("img")
    image = image.get("src").split("/")[1]
    linkedin = i.find_all("a",text="Linkedin bağlantısı")
    if linkedin != []:
        linkedin = linkedin[0].get("href")
    else:
        linkedin = None


    s=i
    if s!=None:
        text = s.text
        stext = str(text.strip())
        isim = stext[0:stext.index("\n")]
        bilgiler = stext[stext.index("\n"):]
        bilgiler = bilgiler.replace("Linkedin bağlantısı","")
        bilgiler = bilgiler.strip().replace("   ","")
        asa = bilgiler.split("\n")
        
        mezun = Mezun(isim,image,asa)
        yazi = ''
        for i in mezun.bilgiler:
            pmetin = '<p class="card-text" style="overflow-wrap:break-word;">'+i+'</p>'
            yazi += pmetin

        if linkedin == None:

            html = '<div class="col-lg-6"><div class="card mb-3 text-bg-light" style="border-right: 1px solid black;max-height:238px;border-top: 1px solid black;border-bottom: 1px solid black;"> <div class="row g-0"> <div class="col-5"> <img src="static/image/mezun/'+mezun.image+'" class="img-fluid rounded-start" style="border-radius:50%;height:238px !important;display: block;margin: auto;margin-left: 0;height: 100%;" alt="imfoto"></div><div class="col-7"><div class="card-body" style="height:100% !important ;"><h5 class="card-title">'+mezun.isim+'</h5><hr>'+ yazi+'</div></div></div></div></div>'
        else:
            html = '<div class="col-lg-6"><div class="card mb-3 text-bg-light" style="border-right: 1px solid black;max-height:238px;border-top: 1px solid black;border-bottom: 1px solid black;"> <div class="row g-0"> <div class="col-5"> <img src="static/image/mezun/'+mezun.image+'" class="img-fluid rounded-start" style="border-radius:50%;height:238px !important;display: block;margin: auto;margin-left: 0;height: 100%;" alt="imfoto"></div><div class="col-7"><div class="card-body" style="height:100% !important ;"><h5 class="card-title">'+mezun.isim+'</h5><hr>'+ yazi+'</div><div style="position: absolute;top: 0;right: 0;"><a class="btn btn-primary btn-sm border-0" href="'+linkedin+'"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/></svg></a></div></div></div></div></div>'
        print(html)
    
            

a = '<div class="col-lg-6"><div class="card mb-3 text-bg-light" style="border-right: 1px solid black;max-height:238px;border-top: 1px solid black;border-bottom: 1px solid black;"> <div class="row g-0"> <div class="col-5"> <img src="static/image/mezun/barisbasyayla.jpeg" class="img-fluid rounded-start" style="border-radius:50%;max-height:238px;;display: block;margin: auto;margin-left: 0;height: 100%;" alt="imfoto"></div><div class="col-7"><div class="card-body"><h5 class="card-title">Barış Başyayla</h5><hr><p class="card-text text-muted"><b>Tel.:</b> +90 212 227 4480 - 471</p><p class="card-text text-muted"><b>E-mail:</b> oguzabel [at] gmail.com</p><p class="card-text text-muted mb-1"><b>Web:</b> http://math.gsu.edu.tr/kaya/</p><p class="card-text text-muted mb-1"><b>Ph.D.:</b>Université de Lille 1-Sciences et Technologies, Lille, France, 2015</p><p class="card-text text-muted"><b>İlgi alanları:</b> Harmonik analizdegeometrik metodlar</p></div></div></div></div></div>'

