# projet GESTION BIBLIOTHEQUE
## Contenu
1. Motivation
2. API Documentation
3. Authentification
4. Existing roles

## Motivation
Le projet GESTION BIBLIOTHÈQUE est réalisé dans le cadre de la validation de cours de création d'API en python flask à l'IAI-TOGO
Il a pour but de revisiter tous les concepts vues en classe, qui sont:

- Creation et connexion à une base de donnée postgres en utilisant l'ORM SQLAlchemy
- CRUDs pour interagir avec la base de donnée (app.py)
- Mise en place d'un environnement virtuelle

Suivez les intructions pour installer la dernière version de python sur la [documentation officielle](https://www.python.org/downloads/) de python



#### Installation des dépendances

Après avoir installé ou mis à jour python, vous devez installer les dépendances de notre API avec la commande:

```bash
pip install -r requirements.txt
```

Celà installera tous les packages nécéssaires que nous avons précisé dans le fichier `requirements.txt`.

##### Dépendances clés
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) est un micro framework open-source de développement web en Python.
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) est un ORM de python. Nous allons l'utiliser pour mapper nos tables en postgres à nos classes en python.

#### Variables d'environement

Nous vous recommandons de creer vos propres variables d'environnement pour la connextion à la base de donnée postgres. Pour celà créez un fichier `.env` dans lequel vous copierez le code suivant en prenant soins de remplacer 'your_password' par votre mot de passe postgres d'utilisateur,'host' par l'addresse IP de votre serveur et your_database par le nom de la base de donnée que vous auriez préalablement creé

```file
password=your_password
host=host
database=your_database
```

## Ouvrir le serveur en local
Pour démarrer l'API sur votre serveur local, vous devez déjà avoir spécifié 'localhost' comme host dans les variables d'environement. Ensuite vous tapez les commandes suivantes dans un terminal:

- Sous linux ou mac

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

- Sous Windows

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

Pour tester tous les endpoints de notre API, vous pouvez le faire depuis le bash en installant [curl](https://curl.se/download.html).
Mais nous vous conseillons de le faire avec l'application [Postman](https://www.postman.com) que vous pouvez télécharger et y importer les requetes qui se trouvent dans le fichier ...

 


## DOCUMENTATION DE L'API

Getting starter
## REFERENCE DE L'API
Cet API a été déployé sur la plateforme Heroku et est disponible sous le lien https://capstoneapi.herokuapp.com

## GESTION DES ERREURS
Les erreurs sont rertournés sous le format JSON dont voici un exemple:
{
    "success":False
    "error": 400
    "message":"Bad request
}

Voici les erreurs possibles que notre API pourrait retourner:
. 400: Bad request
. 500: Internal server error
. 404: Not found


## Endpoints

### GET /livres
    GENERAL:  Cette route retourne la liste des livres dans notre base de donnée, le statut de la requête  et le nombre total des livres.
            Sample: curl https://capstoneapi.herokuapp.com/movies

            {
                "Total": 10,
                "livres": [
                    {
                        "auteur": "Caleb",
                        "categorie_id": 1,
                        "date_publication": "Wed, 01 Jan 2020 00:00:00 GMT",
                        "editeur": "Les Frasques",
                        "id": 1,
                        "isbn": "123-12-23",
                        "titre": "La mort du soldat"
                    },
                    {
                        "auteur": "frère grimm",
                        "categorie_id": 3,
                        "date_publication": "Fri, 02 Mar 1990 00:00:00 GMT",
                        "editeur": "Contes populaire",
                        "id": 2,
                        "isbn": "120-023-24",
                        "titre": "La belle au bois dormant"
                    },
                    {
                        "auteur": "Amadou koné",
                        "categorie_id": 4,
                        "date_publication": "Thu, 12 Apr 1990 00:00:00 GMT",
                        "editeur": "Edicef",
                        "id": 3,
                        "isbn": "1202-3456-345",
                        "titre": "Les frasques d Ebinto"
                    },
                    {
                        "auteur": "Amadou koné",
                        "categorie_id": 4,
                        "date_publication": "Fri, 12 Jun 1992 00:00:00 GMT",
                        "editeur": "Edicef",
                        "id": 4,
                        "isbn": "125-345-34",
                        "titre": "Le respect des morts"
                    },
                    {
                        "auteur": "Amadou koné",
                        "categorie_id": 4,
                        "date_publication": "Thu, 20 Jun 1991 00:00:00 GMT",
                        "editeur": "Edicef",
                        "id": 5,
                        "isbn": "125-30-234",
                        "titre": "La guerre civile"
                    },
                    {
                        "auteur": "Patricia cornwel",
                        "categorie_id": 6,
                        "date_publication": "Sat, 09 Jun 1956 00:00:00 GMT",
                        "editeur": "Les morts parlent",
                        "id": 6,
                        "isbn": "425-308-234",
                        "titre": "Jack l eventreur"
                    },
                    {
                        "auteur": "Will smith",
                        "categorie_id": 2,
                        "date_publication": "Sat, 23 Jun 1990 00:00:00 GMT",
                        "editeur": "Montpelier",
                        "id": 7,
                        "isbn": "1204-345-207",
                        "titre": "A la recherche du bonheur"
                    },
                    {
                        "auteur": "Amadou ampate-bah",
                        "categorie_id": 2,
                        "date_publication": "Tue, 12 Sep 1995 00:00:00 GMT",
                        "editeur": "présence africaine",
                        "id": 8,
                        "isbn": "120-768-235",
                        "titre": "Le soleil des indépedances"
                    },
                    {
                        "auteur": "Jean le roux",
                        "categorie_id": 5,
                        "date_publication": "Thu, 12 Sep 2002 00:00:00 GMT",
                        "editeur": "Les bouquins du futur",
                        "id": 9,
                        "isbn": "904-348-450",
                        "titre": "La comète de Mars"
                    },
                    {
                        "auteur": "Ferdinand OYONO",
                        "categorie_id": 7,
                        "date_publication": "Thu, 12 Oct 1995 00:00:00 GMT",
                        "editeur": "Précence africaine",
                        "id": 10,
                        "isbn": "109-349-120",
                        "titre": "Une vie de boy"
                    }
                ],
                "success": true
            }

###  GET/livres(livre_id)
    GENERAL: Cette route vous permet d'avoir un livre à partir de son id si elle existe. Il retourne les informations concernant un livre, le statut de la requête et l'id du livre demandé.
            Sample: curl https://capstoneapi.herokuapp.com/movies/1

            {
                "Searched_book": {
                    "auteur": "Amadou koné",
                    "categorie_id": 4,
                    "date_publication": "Thu, 12 Apr 1990 00:00:00 GMT",
                    "editeur": "Edicef",
                    "id": 3,
                    "isbn": "1202-3456-345",
                    "titre": "Les frasques d Ebinto"
                },
                "searched_book_id": 3,
                "success": true
            }

###  GET /categories
    GENERAL: Cette route retourne la liste complète des catégories, le nombre total de categorie et le statut de la requête.

            Sample: curl https://capstoneapi.herokuapp.com/actors

            {
                "Categories": [
                        {
                            "id": 1,
                            "libelle": "Policier"
                        },
                        {
                            "id": 2,
                            "libelle": "aventure"
                        },
                        {
                            "id": 3,
                            "libelle": "amour"
                        },
                        {
                            "id": 4,
                            "libelle": "drame"
                        },
                        {
                            "id": 5,
                            "libelle": "Sciences-fiction"
                        },
                        {
                            "id": 6,
                            "libelle": "thriller"
                        },
                        {
                            "id": 7,
                            "libelle": "biographie"
                        }
                    ],
                "Success": true,
                "Total": 7
            }

###  GET/categories(categorie_id)
    GENERAL: Cette route retourne les informations d'une categorie à partir de son id si elle existe, le statut de la requête et l'id de la categorie recherché
            Sample: curl https://capstoneapi.herokuapp.com/actors/1

            {
                "Success": true,
                "seached_categorie": {
                    "id": 2,
                    "libelle": "aventure"
                },
                "searched_categorie_id": 2
            }


###  DELETE/livres(livre_id)
    GENERAL: Cette route permet de supprimer, si elle existe, un livre dont l'id est spécifié. Il retourne l

            Sample: curl - X DELETE https://capstoneapi.herokuapp.com/actors/5
            {
                "actors": [
                    {
                        "age": 32,
                        "gender": "M",
                        "id": 1,
                        "name": "Badiou OURO"
                    }
                ],
                "deleted": 5,
                "success": true,
                "total_actors": 1
            }


###  DELETE/movies(movie_id)
            GENERAL: Delete the movie  of the given ID if it exists. Return the id of the deleted movie, 
            success value, total of movies and movies list based on current page number. Results are
             paginated in groups of 10.

            Sample: curl - X DELETE https://capstoneapi.herokuapp.com/movies/5

            {
        "actors": [
            {
                "id": 1,
                "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                "title": "Thomas NGIJOL"
            }
        ],
        "deleted": 3,
        "success": true,
        "total_movies": 1
    }


###  POST/movies
    GENERAL: This endpoint is used to create a new movie. We return the ID of the new movie created, 
    the movie that was created, the list of movies and the number of movies.

            Sample: curl -X POST https://capstoneapi.herokuapp.com/movies 
            -H "Content-Type:application/json" -d "{"title":"Casanova","release_date":"2020-12-02"}"

                {    
            "movies": [
                {
                    "id": 1,
                    "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                    "title": "Thomas NGIJOL"
                },
                {
                    "id": 4,
                    "release_date": "Wed, 02 Dec 2020 00:00:00 GMT",
                    "title": "Casanova"
                }
            ],
            "created": 4,
            "success": true,
            "total_movies": 2
            }



###  POST/actors
    GENERAL: This endpoint is used to create a new actor. We return the ID of the new actor 
    created, the movie that was created, the list of actors and the number of actors.

            Sample: curl -X POST https://capstoneapi.herokuapp.com/actors 
            -H "Content-Type:application/json" -d "{"name":"Jamel Debouzze","age":45,"gender":"M"}"

                {
                    "actors": [
                        {
                            "age": 32,
                            "gender": "M",
                            "id": 1,
                            "name": "Badiou OURO"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 6,
                            "name": "Jamel Debouzze"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 7,
                            "name": "Jamel Debouzze"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 8,
                            "name": "Jamel Debouzze"
                        }
                    ],
                    "created": 8,
                    "success": true,
                    "total_actors": 4
                }


###  PATCH/actors(actor_id)
    GENERAL: This endpoint allows you to modify an actor. It returns the modified actor,
     the actor ID that was modified and status_code

            Sample: curl -X PATCH https://capstoneapi.herokuapp.com/actors/1 
            -H "Content-Type:application/json" -d "{"name":"Badiou OURO","gender":"M","age":32}"

                {
                    "actor": [
                        {
                            "age": 32,
                            "gender": "M",
                            "id": 1,
                            "name": "Badiou OURO"
                        }
                    ],
                    "id": 1,
                    "success": true
                    }


###  PATCH/movie(movie_id)
    GENERAL: This endpoint allows you to modify an movie. It returns the modified movie, 
    the movie ID that was modified and status_code

            Sample: curl -X PATCH https://capstoneapi.herokuapp.com/movie/1 
            -H "Content-Type:application/json" -d "{"title":"Thomas NGIJOL","release_date":"2001-03-09"}"

                {
                    "id": 1,
                    "movie": [
                        {
                            "id": 1,
                            "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                            "title": "Thomas NGIJOL"
                        }
                    ],
                    "success": true
                    }



##  Testing using capstonedb_test
To run the tests, run
```
dropdb capstonedb_test
createdb capstonedb_test
python test_app.py
```