print """Lequel de ces president n'existent pas?\n
   1. kennedi
   2. Poutine
   3. hollande
   4. Henri 4\n"""
rep = False
while not rep:
	answer1=input('Votre reponse:')
	if answer1 !=4:
		print "non!"
	else:
		print "bien joue!"
		rep = True

print """Qui est le plus pauvre?\n
	1. Bill Gate
	2. Hollande
	3. Renaud\n"""
rep = False
while not rep:	
	answer2=input('Votre reponse:')
 
	if answer2 !=3:
		print "non!"
	else:
		print "Pauvre Renaud"
		rep = True
    
print """En quel language est coder ce jeu? \n
    1.c++
    2.python
    3.html_n"""
rep = False
while not rep:    
	answer3=input('Votre reponse:')
    
	if answer3 != 2:
		print "deso mais non"
	else:
		print "dis moi tu est un/une petit(e) genie"
		rep = True
		
print """Quelle est la capital de france ? \n
	1.Paris
	2.Bordeaux
	3.Lyon
	4.Marseille
	5.Dijon\n"""
rep = False
while not rep:
	answer4=input('Votre reponse:')

	if answer4 != 1:
		print "tu est sure d'etre francais"
	else:
		print "enfin un(e) personne qui sais sa geo"
		rep = True
	
print """Quelle est le nombre de continent? \n
	1
	11
	6
	666
	5.c koi un kontinant?\n"""
rep = False
while not rep:
	answer4=input('Votre reponse:')

	if answer4 != 6:
		print "...aucun commentaire"
	else:
		print "encore un(e) personne qui sais sa geo"
		rep = True

print """la moitier de deux plus deux? \n
	1.2
	2.3
	3.4\n"""
rep = False
while not rep:
	answer5=input('Votre reponse:')

	if answer5 != 2:
		print "..."
	else:
		print "bravo"
		rep = True


