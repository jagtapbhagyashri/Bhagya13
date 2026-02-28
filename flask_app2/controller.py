from flask_app import db ,app
from flask import request,redirect,render_template,session,url_for,flash
from werkzeug.security import generate_password_hash,check_password_hash
from user import User


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["uname"]
        email = request.form["uemail"]
        password =generate_password_hash(request.form["upass"],method='pbkdf2:sha256')



        new_user =User(username=username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        flash ("registrartion succesfull!!!","succesfully")
        #return redirect(url_for("register"))
        return redirect(url_for("login"))
    else:
        flash("Email already exist")
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method =="POST":
        email=request.form["uemail"]
        password = request.form["upass"]
        user =User.query.filter_by(email=email).first()


        if user and check_password_hash(user.password,password):
            session["user_id"]=user.id
            session["user_name"]=user.username
            flash("login succesfull","success")
            return redirect(url_for("dashboard"))
        else:
            
            flash("login failed","check your password and email")
            return redirect(url_for("login"))
    return render_template("login.html")



@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        flash("Please login first!", "warning")
        return redirect(url_for("login"))

    return render_template("dashboard.html")



@app.route("/logout")
def logout():
    session.clear()   # removes all session data
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))



if __name__=="__main__":
    app.run(debug=True)

