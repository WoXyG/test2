from flask import Flask, render_template, request
from random import choice
import requests

app = Flask(__name__)

@app.route("/attackontitanarat")
def attackontitanarat():
   return render_template("attackontitanarat.html")
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/verilerial', methods=['POST', 'GET'])
def verilerial():
   if request.method == 'POST':
      isim = request.form.get('isim') 
      aotresp = requests.get("https://ruka-chan.woxy.repl.co/aot")
      aot_verisi = aotresp.json()
      aot_sayi = 0
      isim = isim.capitalize()
      while True :
        first_name = aot_verisi["data"][aot_sayi]["firstname"]
        if first_name == isim:
          print(aot_sayi)
          break
        else:
          aot_sayi += 1
          print(aot_sayi)

      aot = dict()
      aot["name"] = aot_verisi["data"][aot_sayi]["firstname"]
      aot["lastname"] = aot_verisi["data"][aot_sayi]["lastname"]
      aot["Hair_color"] = aot_verisi["data"][aot_sayi]["Hair color"]
      aot["Eye_color"] = aot_verisi["data"][aot_sayi]["Eye color"]
      aot["old"] = aot_verisi["data"][aot_sayi]["old"]
      aot["sex"] = aot_verisi["data"][aot_sayi]["sex"]
      aot["whence"] = aot_verisi["data"][aot_sayi]["whence"]
      aot["class"] = aot_verisi["data"][aot_sayi]["class"]
      aot["power"] = aot_verisi["data"][aot_sayi]["power"]
      aot["img"] = aot_verisi["data"][aot_sayi]["img"]

      return render_template("attackontitansonuc.html",aot = aot)

   else:
      return render_template("attackontitansonuc.html",hata="Formdan veri gelmedi!")



if __name__ == "__main__":  
  app.run(host='0.0.0.0', port=8080)