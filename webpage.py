from flask import *


import appiris as p
# the url  to store the html pages
app = Flask(__name__,template_folder='C:/Users/bouzi/OneDrive/Documents/stage2/html',static_folder='C:/Users/bouzi/OneDrive/Documents/stage2/css')

@app.route("/")
def index():
     return render_template('index1.html')
 
    
@app.route('/prediction',methods = ['POST'])    
def verification() :
      #store the value in dic
      valeur=request.form.to_dict()
      print(valeur)
      #store only the values of the dic in a list
      valeur=list(valeur.values())
      print(valeur)
      #convert string to int 
      valeur=list(map(int,valeur))
      print(valeur)
      #prédiction
      result=p.prediction(valeur)

      return render_template('index2.html',result=result[0])

app.run(debug=True,port=5000)