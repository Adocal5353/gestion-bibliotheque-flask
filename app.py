import os
from flask import abort

from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dotenv import load_dotenv  # permet d'importer les variables d'environnement
load_dotenv()
app = Flask(__name__)


password=quote_plus(os.getenv('password'))
host = os.getenv('host')
database = os.getenv('database')
#motdepasse = quote_plus('caleb1234')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:{}@{}:5432/{}".format(password,host,database)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Categorie(db.Model):
    __tablename__="categories"
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(100), nullable=False)
    my_livres=db.relationship('Livre',backref='categories',lazy=True)

    def __init__(self,libelle_categorie):
        self.libelle_categorie=libelle_categorie
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return{
            'id':self.id,
            'libelle':self.libelle_categorie
        }


class Livre(db.Model):
    __tablename__="livres"
    id=db.Column(db.Integer,primary_key=True)
    isbn=db.Column(db.String,nullable=False,unique=True)
    titre=db.Column(db.String(200),nullable=False)
    date_publication=db.Column(db.DateTime,nullable=True)
    auteur=db.Column(db.String(100),nullable=False)
    editeur=db.Column(db.String(100),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=False)
    
    def __init__(self,isbn,titre,date_publication,auteur,editeur,categorie_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return{
            'id':self.id,
            'isbn':self.isbn,
            'titre':self.titre,
            'date_publication':self.date_publication,
            'auteur':self.auteur,
            'editeur':self.editeur,
            'categorie_id':self.categorie_id
        }

db.create_all()

########################################################
#
#La route de demarage. Par defaut cette route ne retourne aucun resultat
#
####################################################################

@app.route('/',methods=['POST','GET'])
def index():
    abort(400)

###########################################################
#
#cette route donne la liste de tous les livres
#
###########################################################

@app.route('/livres',methods=['GET'])
def get_all_books():
    try:
        livres=Livre.query.all()
        formated_livre=[livre.format() for livre in livres]
        return jsonify({
            'success':True,
            'livres':formated_livre,
            'Total':Livre.query.count()
        })
    except:
        abort(400)

################################################################
#
#cette route retourne un livre dont l'id est passé en paramètre
#
#####################################################################

@app.route('/livres/<int:id>',methods=['GET'])
def get_one_book(id):
    try:
        livre=Livre.query.get(id)
        if livre is None:
            abort(404)
        else:
            return jsonify({
                'success':True,
                'searched_book_id':id,
                'Searched_book':livre.format()
            })
    except:
        abort(400)

##################################################################
#cette route retourne les livres contenues dans une categorie donné
##################################################################  
@app.route('/categories/<int:id>/livres',methods=['GET'])
def get_one_categorie_books(id):
    try:
        livres=Livre.query.filter(Livre.categorie_id==id)
        formated_livres=[livre.format() for livre in livres]
        if livres is None:
            abort(404)
        else:
            return jsonify({
                'Success':True,
                'categorie_id':id,
                'Livres':formated_livres,
                'Total':Livre.query.filter(Livre.categorie_id==id).count()
            })
    except:
        abort(400)


##########################################################
#cette route retourne les informations d'une categorie dont l'id est passé en paramètre
#############################################################

@app.route('/categories/<int:id>',methods=['GET'])
def get_one_category(id):
    try:
        categorie=Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            return jsonify({
                'Success':True,
                'searched_categorie_id':id,
                'seached_categorie':categorie.format()
            })
    except:
        abort(400)

        

##############################################################
#cette route retourne les informations de toutes les categories
###############################################################

@app.route('/categories',methods=['GET'])
def get_all_categorie():
    try:
        categories=Categorie.query.all()
        if categories is None:
            abort(404)
        else:
            formated_cat = [categorie.format() for categorie in categories]
            return jsonify({
                'Success':True,
                'Categories':formated_cat,
                'Total':Categorie.query.count()
            })
    except:
        abort(400)

################################################################
#cette route supprime une livre dont l'id est passé est paramètre
###################################################################

@app.route('/livres/<int:id>',methods=['DELETE'])
def delete_book(id):
    try:
        livre = Livre.query.get(id)
        if livre is None:
            abort(400)
        else:
            livre.delete()
            return jsonify({
                'Success':True,
                'Deleted_book':livre.format(),
                'Total_books':Livre.query.count()
            })
    except:
        abort(400)
    finally:
        db.session.close()


###################################################################
#cette route supprime une categorie dont l'id est passé en paramètre
###################################################################

@app.route('/categories/<int:id>',methods=['DELETE'])
def delete_category(id):
    try:
        categorie = Categorie.query.get(id)
        if categorie is None:
            abort(400)
        else:
            categorie.delete()
            return jsonify({
                'Success':True,
                'Deleted_Categorie':categorie.format(),
                'Total_categorie':Categorie.query.count()
            })
    except:
        abort(400)
    finally:
        db.session.close()


#########################################################################
#cette route modifie les infos d'un livre dont l'id est passé en paramètre
##############################################################################
@app.route('/livres/<int:id>',methods=['PATCH'])
def modify_book(id):
    body=request.get_json()
    try:
        livre=Livre.query.get(id)
        livre.isbn=body.get('isbn',None)
        livre.titre=body.get('titre',None)
        livre.date_publication=body.get('date_publication',None)
        livre.auteur=body.get('auteur',None)
        livre.editeur=body.get('editeur',None)
        livre.categorie_id=body.get('categorie_id',None)
        if livre is None:
            abort(400)
        else:
            livre.update()
            return jsonify({
                'Success':True,
                'Updated_book_id':id,
                'Updated_book':Livre.query.get(id).format()
            })
    except:
        abort(400)
    finally:
        db.session.close()

##############################################################
#cette route modifie les infos d'une categorie dont l'id est passé en paramètre
###################################################################

@app.route('/categories/<int:id>',methods=['PATCH'])
def modify_category(id):
    body=request.get_json()
    try:
        categorie=Categorie.query.get(id)
        categorie.libelle_categorie=body.get('libelle_categorie',None)
        if categorie is None or categorie.libelle_categorie is None:
            abort(404)
        else:
            categorie.update()
            return jsonify({
                'Success':True,
                'Updated_category_id':id,
                'Updated_category':categorie.format()
            })
    except:
        abort(400)
    finally:
        db.session.close()


############################ 
#Les errors handlers
#############################

#404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success":False,
        "Message":"Not found",
        "error":404
    }),404

#400

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success":False,
        "Message":"Bad request",
        "error":400
    }),400

#500
@app.errorhandler(500)
def internal_server_error():
    return jsonify({
        "success":False,
        "Message": "Internal server error",
        "Error":500
    })