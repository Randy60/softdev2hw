from flask import Flask, render_template, request
import random
import time

app = Flask(__name__)

def time(f):
    def meta( *args ):
        now = time.time()
        temp = f( *args )
        now = time.time()-now
        print (f.func_name + "("+str(*args)+")\n"
                +" returned " + str(temp)+"\n"+
                " and took" + str(now) + " seconds")
        return temp
    return meta




@app.route("/")
@app.route("/home")
@time
def home():
   return render_template("home.html")

@app.route("/WhoIsChamp", methods=["GET","POST"])
@time
def JC():
    if request.method=="GET":
        return render_template("JohnCena1.html")
    else:
        button = request.form['button']
        isCena = request.form['password']
        if button == "cancel":
            return render_template("JohnCena1.html")
        if isCena == "John Cena":
            return render_template("JohnCena2.html", pic_id="templates/JC1.jpg")
        else:
            return render_template("JohnCena1.html", error = "that's just not true")

@app.route("/morePicturesOfJohnCena")
@time
def JCmany():
    r = random.randint(1,6)

    return render_template("JohnCena2.html",pic_id="templates/JC"+str(r)+".jpg")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8001)
