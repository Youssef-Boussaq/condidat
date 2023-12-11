 
def ajoute( nom ,prenom ,tel , type):
    with open("contact.txt","a") as f :
        f.write(f"{nom};{prenom};{tel};{type}\n") 
def supprimer():
    with open('contact.txt', 'r') as f:
        lines = f.readlines()
    with open('contact.txt', 'w') as f:
        for line in lines:
            if 'personnel' not in line:
                f.write(line)
