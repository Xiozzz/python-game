# -*- coding:Utf-8 -*-
# toutes les données du jeu

LIEUX = {
	"couL01": {
	"nom" : "un couloir", 
	"decription" : "Ce couloir longe deux murs en pierre, il est possible d'aller au nord et au sud."
	},
	"porT01": {
	"nom" : "une porte",
	"description" : "Elle est cassé et impossible à ouvrir."
	}
}

OBJET = {
	
	#potion de soin
	#torche
	#ration de nourriture
}

ARMES = {
	
	"epeE01" : {
	"nom" : "une épée en cuivre", 
	"description" : "une vieille épée en cuivre", 
	"dégats" : 2, 
	"points" : 1
	 },
	"epeE02" : {
	"nom" : "une épée rouillé", 
	"description" : "une épée rouillé en fer", 
	"dégats" : 2 },
	"epe03"
	#épée 03 aiguisée
}

ARMURES = {
	
	#cuir, "défense" : 1
	#acier, "défense" : 2
	#
}


NPC = {
	
	"hoT01" : {
	"nom" : "Un homme tigre",
	"description" : "Le corps d'un homme d'âge adulte, un visage de felin."
	"dis00" : "Bonjour!"
	} 
	"maG01" : {
	"nom" : "Un magicien",
	"description" : "Il porte un grand chapeau"
	}
}


MAP00 = {
01 : {
"a" : ["porT01"], 
"b" : ["mur"],
"c" : ["mur"], 
"d" : ["mur"],
"e" : ["mur"],
"f" : ["mur"]
},
02 : {
"a" : ["couL01"], 
"b" : [""],
"c" : [""], 
"d" : [""],
"e" : [""],
"f" : [""]}
}
03 : {
"a" : ["couL02"], 
"b" : [""],
"c" : [""], 
"d" : [""],
"e" : [""],
"f" : [""]}
}
04 : {
"a" : [""], 
"b" : [""],
"c" : [""], 
"d" : [""],
"e" : [""],
"f" : [""]}
}
05 : {
"a" : [""], 
"b" : [""],
"c" : [""], 
"d" : [""],
"e" : [""],
"f" : [""]}
}
06 : {
"a" : [""], 
"b" : [""],
"c" : [""], 
"d" : [""],
"e" : [""],
"f" : [""]}
}
07 : {
"a" : [""], 
"b" : [""],
"c" : [""], 
"d" : [""],
"e" : [""],
"f" : [""]}
}
