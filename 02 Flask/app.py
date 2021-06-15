from flask import Flask, request, render_template, url_for, redirect, flash, session
from scripts.db import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

# ------------------------------ >   Menu publico  < ------------------------------

"""
	Ruta Inicial del proyecto, solo muetra nuestros nombres
"""
@app.route('/',methods = ['POST','GET'])
def inicio():
	session.clear()
	return render_template('index.html')	

"""
	Ruta que carga el login del proyecto
"""
@app.route('/login',methods = ['POST','GET'])
def login():
	session.clear()
	if request.method == 'POST':	
		usr=request.form['usuario']
		psw=request.form['clave']
		conexion = conecta_db("Proyecto.db")
		respuesta = valida_login(conexion,usr,psw,1)		
		if respuesta == "Administrador":
			session["usr"] = usr			
			session["idTipoUsr"] = 1
			session["nom"] = regresa_nombre(conexion,usr)
			return respuesta			
		if respuesta == "Cliente":
			session["usr"] = usr
			session["idTipoUsr"] = 2
			session["nom"] = regresa_nombre(conexion,usr)
			return respuesta
		if respuesta == "Invalido":
			return respuesta
		close_db(conexion)
	return render_template('login.html')

"""
	Ruta que sirve para dar de alta usuarios del tipo cliente
"""
@app.route('/regPublic',methods = ['POST','GET'])
def registro_Publico():
	session.clear()
	return render_template('registro.html')

# --------------------------------------------------------------------------------



# ------------------------------ >  Menu Administrador  < ------------------------------

"""
	Rescanear toda la red y configura protocolos
"""
@app.route('/adm0',methods = ['POST','GET'])
def adm0():
	
	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm0.html',nombrecito=session["nom"])

"""
	Gestiona Administradores - Menu
"""
@app.route('/adm1',methods = ['POST','GET'])
def adm1():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm1.html',nombrecito=session["nom"])

"""
	Gestiona Administradores - Form Agregar
"""
@app.route('/adm11',methods = ['POST','GET'])
def adm11():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			if request.method == 'POST':
				usr=request.form['usr']
				psw=request.form['psw']
				nom=request.form['nom']
				ap1=request.form['ap1']
				ap2=request.form['ap2']
				gen=request.form['gen']
				ema=request.form['ema']
				conexion = conecta_db("Proyecto.db")
				respuesta = alta_usur(conexion,ema,usr,psw,nom,ap1,ap2,gen,1)
				close_db(conexion)
				return respuesta

	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm11.html',nombrecito=session["nom"])

"""
	Gestiona Administradores - Tabla Busca
"""
@app.route('/adm12',methods = ['POST','GET'])
def adm12():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			conexion = conecta_db("Proyecto.db")
			respuesta = consulta_usur(conexion,1)
			return render_template('Adm12.html',filas=respuesta,nombrecito=session["nom"])


	except Exception as e:
		return redirect(url_for("login"))	

"""
	Gestiona Administradores - Form modifica
"""
@app.route('/adm121',methods = ['POST','GET'])
def adm121():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			if request.method == 'POST':
				usr=request.form['usr']
				conexion = conecta_db("Proyecto.db")
				respuesta = consulta_usur_esp(conexion,usr)
				return render_template('Adm121.html',filas=respuesta,nombrecito=session["nom"])


	except Exception as e:
		return redirect(url_for("login"))	

"""
	Gestiona Administradores - Metodo modifica
"""
@app.route('/adm122',methods = ['POST','GET'])
def adm122():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			if request.method == 'POST':
				usr=request.form['usr']
				psw=request.form['psw']
				nom=request.form['nom']
				ap1=request.form['ap1']
				ap2=request.form['ap2']
				gen=request.form['gen']
				ema=request.form['ema']
				conexion = conecta_db("Proyecto.db")
				respuesta = cambio_usur(conexion,usr,psw,nom,ap1,ap2,gen)				
				close_db(conexion)
				return respuesta

	except Exception as e:
		return redirect(url_for("login"))	


"""
	Gestiona Administradores - Tabla pre eliminar
"""
@app.route('/adm13',methods = ['POST','GET'])
def adm13():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			conexion = conecta_db("Proyecto.db")
			respuesta = consulta_usur(conexion,1)
			return render_template('Adm13.html',filas=respuesta,nombrecito=session["nom"])

	except Exception as e:
		return redirect(url_for("login"))	

"""
	Gestiona Administradores - Metodo eliminar
"""
@app.route('/adm131',methods = ['POST','GET'])
def adm131():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			if request.method == 'POST':
				usr=request.form['usr']
				conexion = conecta_db("Proyecto.db")
				respuesta = elimina_usur(conexion,usr)
				close_db(conexion)
				return respuesta

	except Exception as e:
		return redirect(url_for("login"))



@app.route('/adm2',methods = ['POST','GET'])
def adm2():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm2.html',nombrecito=session["nom"])

@app.route('/adm21',methods = ['POST','GET'])
def adm21():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			if request.method == 'POST':
				usr=request.form['usr']
				psw=request.form['psw']
				nom=request.form['nom']
				ap1=request.form['ap1']
				ap2=request.form['ap2']
				gen=request.form['gen']
				ema=request.form['ema']
				conexion = conecta_db("Proyecto.db")
				respuesta = alta_usur(conexion,ema,usr,psw,nom,ap1,ap2,gen,2)
				close_db(conexion)
				return respuesta


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm21.html',nombrecito=session["nom"])

@app.route('/adm22',methods = ['POST','GET'])
def adm22():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			conexion = conecta_db("Proyecto.db")
			respuesta = consulta_usur(conexion,2)
			return render_template('Adm22.html',filas=respuesta,nombrecito=session["nom"])


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm22.html',nombrecito=session["nom"])

@app.route('/adm221',methods = ['POST','GET'])
def adm221():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			if request.method == 'POST':
				usr=request.form['usr']
				conexion = conecta_db("Proyecto.db")
				respuesta = consulta_usur_esp(conexion,usr)
				return render_template('Adm221.html',filas=respuesta,nombrecito=session["nom"])

	except Exception as e:
		return redirect(url_for("login"))	

"""
	Gestiona Clientes - Metodo modifica
"""
@app.route('/adm222',methods = ['POST','GET'])
def adm222():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			if request.method == 'POST':
				usr=request.form['usr']
				psw=request.form['psw']
				nom=request.form['nom']
				ap1=request.form['ap1']
				ap2=request.form['ap2']
				gen=request.form['gen']
				ema=request.form['ema']
				conexion = conecta_db("Proyecto.db")
				respuesta = cambio_usur(conexion,usr,psw,nom,ap1,ap2,gen)				
				close_db(conexion)
				return respuesta

	except Exception as e:
		return redirect(url_for("login"))	


@app.route('/adm23',methods = ['POST','GET'])
def adm23():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			conexion = conecta_db("Proyecto.db")
			respuesta = consulta_usur(conexion,2)
			return render_template('Adm23.html',filas=respuesta,nombrecito=session["nom"])

	except Exception as e:
		return redirect(url_for("login"))	


@app.route('/adm3',methods = ['POST','GET'])
def adm3():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm3.html',nombrecito=session["nom"])


@app.route('/adm4',methods = ['POST','GET'])
def adm4():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm4.html',nombrecito=session["nom"])

@app.route('/adm41',methods = ['POST','GET'])
def adm41():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm41.html',nombrecito=session["nom"])


@app.route('/adm5',methods = ['POST','GET'])
def adm5():

	try:
		usr = session["idTipoUsr"]
		if(usr!=1):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Adm5.html',nombrecito=session["nom"])

# --------------------------------------------------------------------------------



# ------------------------------ >  Menu Cliente  < ------------------------------



@app.route('/usr0',methods = ['POST','GET'])
def usr0():

	try:
		usr = session["idTipoUsr"]
		if(usr!=2):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Usr0.html')

@app.route('/usr1',methods = ['POST','GET'])
def usr1():

	try:
		usr = session["idTipoUsr"]
		if(usr!=2):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Usr1.html')

@app.route('/usr2',methods = ['POST','GET'])
def usr2():

	try:
		usr = session["idTipoUsr"]
		if(usr!=2):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Usr2.html')

@app.route('/usr21',methods = ['POST','GET'])
def usr21():

	try:
		usr = session["idTipoUsr"]
		if(usr!=2):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Usr21.html')

@app.route('/usr3',methods = ['POST','GET'])
def usr3():

	try:
		usr = session["idTipoUsr"]
		if(usr!=2):
			return redirect(url_for("login"))
		else:
			pass


	except Exception as e:
		return redirect(url_for("login"))

	return render_template('Usr3.html')


# --------------------------------------------------------------------------------


@app.errorhandler(404)
def error404(error):
    return render_template("404.html")

if __name__ == '__main__':
	conexion = conecta_db("Proyecto.db")
	crea_tbs(conexion)
	close_db(conexion)
	app.run(host='0.0.0.0',debug=True)