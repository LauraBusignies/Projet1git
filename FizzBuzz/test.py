l1 = ["   .-'-.      ",
 " _/.-.-.\_    ",
 "( ( o o ) )   ",
 " |/  '  \|    ",
 "  \ .-. /     ",
 "  /`'''`\     ",
 " /       \    "]

compteur = 0
for loop in range (7):
    ligne = ""
    for loop in range(10):
        ligne = (f'{ligne}{l1[compteur]}')
    compteur += 1
    print (ligne)