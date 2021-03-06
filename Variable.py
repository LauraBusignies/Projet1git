var_enregistrer = {
    
    'positionArbreBanane' : [],
    'positionArbreMangue' : [],
    'positionArbreAnanas' : [],

    'positionSolAnanas' : [],
    'positionSolBanane' : [],
    'positionSolMangue' : [],

    'positionEnigme' : [],
    'positionJoueur' : [25, 75],

    'ancienCaractere' : "" ,  
    'nbKey' : 0,
    'objetRamasser' : "",
    'nomAventurier' : "",
    'date' : "",
    'leave' : False,
    'nombreDeplacement' : 0,
    'nombreAction' : 0,
    'resultatJeu' : "",
    "listeHistorique" : 0,

    
    'verificationMonkey' : False,
    'verificationMystere' : False,
    'verificationCesar' : False,

    'vitalite' : 
            {"Energie" :{
                "Stock" : 100,
                "-" : 3},
            "Hydratation" :{
                "Stock" : 100,
                "-" : 2},
            "Satiete" :{
                "Stock" : 100,
                "-" : 2}},

    'sac_a_dos' : { 
        "Chaussure" :{ 
            "nom" : "Chaussure",
            "nombre" : 0,
            "+" : 0 ,
            "Stockage" : None,
            "StockageM" : None,
            "Utilité" : "Marcher sur les cailloux",
            "Ramassage": "Va savoir ..",
            "message": "Vous avez jettez vos chaussures",
            "positionY" : None,
            "positionX" : None

                    },

        "Bouteille" :{ 
            "nom" : "Bouteille",
            "nombre" : 1,
            "+" : 20,
            "Stockage" : 100,
            "StockageM" : 100,
            "Utilité" : "Hydratation",
            "Ramassage": "Vous avez trouvé une bouteille d'eau",
            "message": "Oula vous avez jetter votre bouteille, vous allez mourir de soif !",
            "positionY" : None,
            "positionX" : None

                    },
        "Couteau" :{ 
            "nom" : "Couteau",
            "nombre" : 1,
            "Stockage" : None,
            "StockageM" : None,
            "Utilité" : "A toi de trouver",
            "Ramassage": "Vous avez trouvé un couteau",
            "message": "Vous avez jettez votre couteau, vous allez en avoir besoin",
            "positionY" : None,
            "positionX" : None

                },
        "Banane" :{
            "nom" : "Banane",
            "nombre" : 0,
            "+" : 20,        
            "Stockage" : None,
            "StockageM" : None,
            "Utilité" : "Satiete",
            "Ramassage": "Vous avez trouvé une Banane, miam !",
            "message": "Vous avez jettez une Banane",
            "positionY" : None,
            "positionX" : None

    },
        "Ananas" :{ 
            "nom" : "Ananas",
            "nombre" : 0,
            "+" : 25,
            "Stockage" : None,
            "StockageM" : None,
            "Utilité" : "Satiete",
            "Ramassage": "Vous avez trouvé un Ananas, miam !",
            "message": "Vous avez jettez un Ananas",
            "positionY" : None,
            "positionX" : None
    },
        "Mangue" :{ 
            "nom" : "Mangue",
            "nombre" : 0,
            "+" : 30,
            "Stockage" : None,
            "StockageM" : None,
            "Utilité" : "Satiete",
            "Ramassage": "Vous avez trouvé un Mangue, miam !",
            "message": "Vous avez jettez une Mangue",
            "positionY" : None,
            "positionX" : None
}}}


dicHistorique = {'compteurHistorique' : 0}

deplacement = ""
liste_Map = []
compteurStock = 0

listeArbre = ["\u001b[38;5;64mγ\033[0m", "\u001b[38;5;76m↑\033[0m", "\u001b[38;5;46m♣\033[0m"]
listeFruit = ["Ananas", "Banane", "Mangue"]

validationPositionFruit = False
validationPositionSol = False

contenuInventaire = []
lettre = ""
fruit = ""
checkActionSac = False
tricheur = False






color_character = {
    " " : {
        "name" : "rien" , 
        "image" : " ",
        "colorS" : "\u001b[38;5;0m ",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : "C'est trop risqué d'aller sur les falaise !"        
    },
    "M" : {
        "name" : "montagne" , 
        "image" : "M",
        "colorS" : "\u001b[38;5;58mM",
        "colorE" : "\033[0m",
        "CanWalk" : False,
        "Erreur" : "C'est trop risqué d'escalader ses montagnes !"        
    },
    "≈" : {
        "name" : "riviere" , 
        "image" : "≈",
        "colorS" : "\u001b[38;5;39m≈",
        "colorE" : "\033[0m",
        "CanWalk" : False,
        "Erreur" : "Trop de courant pour aller dans cette rivière, chercher un autre moyen de passer"        
    },
    "░" : {        
        "name" : "sable" , 
        "image" : "░",
        "colorS" : "\u001b[38;5;226m░",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None       
    },
    "▒" : {
        "name" : "mer" , 
        "image" : "▒",
        "colorS" : "\u001b[38;5;20m▒",
        "colorE" : "\033[0m",  
        "CanWalk" : False,
        "Erreur" : "Ca va pas ! Tu veux te noyer !"
    },
    "█" : {
        "name" : "falaise" , 
        "image" : "█",
        "colorS" : "\u001b[38;5;240m█",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "C'est trop risqué d'aller sur les falaise !"
    },
    "║" : {
        "name" : "Coté porte" , 
        "image" : "║",
        "colorS" : "\u001b[38;5;88m║",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Tu te manges une porte là !"
    },
    "╔" :{
        "name" : "coin porte" , 
        "image" : "╔",
        "colorS" : "\u001b[38;5;88m╔",
        "colorE" : "\033[0m",
        "CanWalk" : False,
        "Erreur" : "Tu te manges une porte là !"
    },
    "═" :{
        "name" : "haut porte" , 
        "image" : "═",
        "colorS" : "\u001b[38;5;88m═",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Tu te manges une porte là !"
    },
    "╗" :{
        "name" : "coin porte" , 
        "image" : "╗",
        "colorS" : "\u001b[38;5;88m╗",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Tu te manges une porte là !"
    },
    "■" :{
        "name" : "rocher" , 
        "image" : "■",
        "colorS" : "\u001b[38;5;8m■",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Tu ne peux pas aller sur ses cailloux !"
    },   
    "♪" :{
        "name" : "clé" , 
        "image" : "♪",
        "colorS" : "\u001b[38;5;226m♪",
        "colorE" : "\033[0m",  
        "CanWalk" : True,
        "Erreur" : None
    },   
    "♫" :{
        "name" : "clé" , 
        "image" : "♫",
        "colorS" : "\u001b[38;5;226m♫",
        "colorE" : "\033[0m",  
        "CanWalk" : True,
        "Erreur" : None
    }, 
    "γ" :{
        "name" : "arbre" , 
        "image" : "γ",
        "colorS" : "\u001b[38;5;64mγ",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    },
    "♣" :{
        "name" : "arbre" , 
        "image" : "♣",
        "colorS" : "\u001b[38;5;46m♣",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    },  
    "↑" :{
        "name" : "arbre" , 
        "image" : "↑",
        "colorS" : "\u001b[38;5;76m↑",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    },  
    "_" :{
        "name" : "bordure" , 
        "image" : "—",
        "colorS" : "\u001b[38;5;214m—",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    },  
    "—" :{
        "name" : "bordure" , 
        "image" : "—",
        "colorS" : "\u001b[38;5;214m—",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    }, 
    "|" :{
        "name" : "bordure" , 
        "image" : "|",
        "colorS" : "\u001b[38;5;214m|",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Quelque chose bloque.."
    }, 
    "○" :{
        "name" : "bordure" , 
        "image" : "○",
        "colorS" : "\u001b[38;5;120m○",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : "Tu es sur un objet !"
    } 
}

