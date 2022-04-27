import time
from flask import Flask, request, render_template, g
app = Flask(__name__)
not_allowed = [";",",","'","\"","&","|","`",":"]
 
 
@app.before_request
def before_request():
   g.request_start_time = time.time()
   g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)
 
 
@app.route("/", methods=('GET', 'POST'))
def main():
   id_avion = 0
   if request.method == 'POST':
      id_avion = request.form['id_avion']
      for char in not_allowed:
         if char in id_avion:
            return render_template('hacking.html')
      try:
         eval(id_avion)
      except:
         id_avion = str(id_avion) + " : N'est pas un numéro d'avion valide"
   time.sleep(0)
   test = g.request_time()
   sec = int(float(test[:-1]))
   if sec < 10 :
      return render_template('result.html', id_avion=id_avion)
   else:
      return render_template('flag.html')
