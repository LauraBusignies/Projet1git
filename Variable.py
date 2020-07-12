
deplacement = ""
nombre = 0
liste_Map = []
positionJoueur = [25, 80]
compteurS = 0
ancienCaractere = ""
listeObjet = ["Ananas", "Banane", "Mangue"]
positionObjet = []

vitalité = {
    "Fatigue" : 100,
    "Hydratation" : 100,
    "Satiété" : 100
    }

color_character = {
    " " : {
        "name" : "rien" , 
        "image" : " ",
        "colorS" : "\033[33m",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : "C'est trop risqué d'aller sur les falaise !"        
    },
    "\\" : {
        "name" : "montagne" ,
        "image" : "M",
        "colorS" : "\033[33m",
        "colorE" : "\033[0m",
        "CanWalk" : False,
        "Erreur" : "C'est trop risqué d'escalader ses montagnes !"        
    },
    "/" : {
        "name" : "montagne" , 
        "image" : "M",
        "colorS" : "\033[33m",
        "colorE" : "\033[0m",
        "CanWalk" : False,
        "Erreur" : "C'est trop risqué d'escalader ses montagnes !"        
    },
    "≈" : {
        "name" : "riviere" , 
        "image" : "≈",
        "colorS" : "\033[33m≈",
        "colorE" : "\033[0m",
        "CanWalk" : False,
        "Erreur" : "Trop de courant pour aller dans cette rivière, chercher un autre moyen de passer"        
    },
    "░" : {        
        "name" : "sable" , 
        "image" : "░",
        "colorS" : "\033[33m░",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None       
    },
    "▒" : {
        "name" : "mer" , 
        "image" : "▒",
        "colorS" : "\033[33m▒",
        "colorE" : "\033[0m",  
        "CanWalk" : False,
        "Erreur" : "Ca va pas ! Tu veux te noyer !"
    },
    "█" : {
        "name" : "falaise" , 
        "image" : "█",
        "colorS" : "\033[33m█",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "C'est trop risqué d'aller sur les falaise !"
    },
    "║" : {
        "name" : "Coté porte" , 
        "image" : "║",
        "colorS" : "\033[33m║",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Tu te manges une porte là !"
    },
    "╔" :{
        "name" : "coin porte" , 
        "image" : "╔",
        "colorS" : "\033[33m╔",
        "colorE" : "\033[0m",
        "CanWalk" : False,
        "Erreur" : "Tu te manges une porte là !"
    },
    "═" :{
        "name" : "haut porte" , 
        "image" : "═",
        "colorS" : "\033[33m═",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Tu te manges une porte là !"
    },
    "╗" :{
        "name" : "coin porte" , 
        "image" : "╗",
        "colorS" : "\033[33m╗",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Tu te manges une porte là !"
    },
    "■" :{
        "name" : "rocher" , 
        "image" : "■",
        "colorS" : "\033[33m■",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Tu est pieds nue !"
    },   
    "♪" :{
        "name" : "clé" , 
        "image" : "♪",
        "colorS" : "\033[33m♪",
        "colorE" : "\033[0m",  
        "CanWalk" : True,
        "Erreur" : None
    },   
    "γ" :{
        "name" : "arbre" , 
        "image" : "γ",
        "colorS" : "\033[33mγ",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    },
    "♣" :{
        "name" : "arbre" , 
        "image" : "♣",
        "colorS" : "\033[33m♣",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    },  
    "↑" :{
        "name" : "arbre" , 
        "image" : "↑",
        "colorS" : "\033[33m↑",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    },  
    "_" :{
        "name" : "bordure" , 
        "image" : "—",
        "colorS" : "\033[33m—",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : None
    },  
    "|" :{
        "name" : "bordure" , 
        "image" : "|",
        "colorS" : "\033[33m|",
        "colorE" : "\033[0m", 
        "CanWalk" : False,
        "Erreur" : "Quelque chose bloque.."
    }, 
    "○" :{
        "name" : "bordure" , 
        "image" : "○",
        "colorS" : "\033[33m○",
        "colorE" : "\033[0m", 
        "CanWalk" : True,
        "Erreur" : "Tu es sur un objet !"
    } 
}

sac_a_dos = { 
    "Chaussure" :{ 
        "nom" : "Chaussure",
        "nombre" : 0,
        "Stockage" : None,
        "StockageM" : None,
        "Utilité" : "Marcher sur les cailloux",
        "Ramassage": "Vous avez trouvé des chaussures",
        "Jettable" : True,
        "message" : "Tu viens de jetter tes chaussures, tu en auras surement besoin !",
        "sac" : False
                },

    "Bouteille" :{ 
        "nom" : "Bouteille",
        "nombre" : 1,
        "StockageA" : 0,
        "StockageM" : 100,
        "Utilité" : "S'hydrater",
        "Ramassage": "Vous avez trouvé des chaussures",
        "Jettable" : False,
        "message" : "Cette bouteille est vital !",
        "sac" : False
                },
    "Couteau" :{ 
        "nom" : "Couteau",
        "nombre" : 1,
        "Stockage" : None,
        "StockageM" : None,
        "Utilité" : "A toi de trouver",
        "Ramassage": "Vous avez trouvé des chaussures",
        "Jettable" : False,
        "message" : "Ce couteau te servira bien a quelque chose !",
        "sac" : False
            },
    "Banane" :{
        "nom" : "Banane",
        "nombre" : 0,
        "Stockage" : 2,
        "StockageM" : 100,
        "Utilité" : "Satiété",
        "Ramassage": "Vous avez trouvé une Banane, miam !",
        "Jettable" : True,
        "message" : "Vous avez jetté une Banane !",
        "sac" : False
},
    "Ananas" :{ 
        "nom" : "Ananas",
        "nombre" : 1,
        "Stockage" : 10,
        "StockageM" : 100,
        "Utilité" : "Satiété",
        "Ramassage": "Vous avez trouvé un Ananas, miam !",
        "Jettable" : True,
        "message" : "Vous avez jetté une Ananas !",
        "sac" : False
},
    "Mangue" :{ 
        "nom" : "Mangue",
        "nombre" : 1,
        "Stockage" : 7,
        "StockageM" : 100,
        "Utilité" : "Satiété",
        "Ramassage": "Vous avez trouvé un Mangue, miam !",
        "Jettable" : True,
        "message" : "Vous avez jetté une Mangue !",
        "sac" : False
}
}
