from flask import Flask, render_template, request
from dati import dabut_rindinas, pierakstit_klat


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def te():
    return render_template("teksts.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["Anna", "Katls", "Kartupelis"]
    bildes = ["https://static.twentytwowords.com/wp-content/uploads/10model2-685x685.jpg", "https://arkolat.lv/storage/uploads/global/product_images/image/000/055/684/large/ef387b5ad94e9169c7f220dda11f92da.jpg", "https://img.medicine.lv/articles/open/1/5/media/users/article/galleries/150/455/15045536.jpg_15045536_600x400.jpg"]
    kopejais_saraksts = []
    faila_rindas = dabut_rindinas()
    for rinda in faila_rindas:
        elements = rinda.split(", ")
        kopejais_saraksts.append(elements)

    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums = len(saraksts), visi = kopejais_saraksts)

@app.route("/info", methods=['POST', 'GET'])
def info():
    if request.method =="POST":
        nosaukums = request.form["nosaukums"]
        adrese = request.form["adrese"]
        rinda= nosaukums + ", " + adrese
        pierakstit_klat(rinda)
    return render_template("info.html")


if __name__ == '__main__':
    app.run(port = 5000)
    

print("Sveiki!")
