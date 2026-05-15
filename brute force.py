import itertools 

import string 

import time 

  

# --- PARAMÈTRES --- 

MAX_LENGTH = 6          # limite pédagogique (évite explosion) 

TIME_LIMIT = 100000
# secondes max avant arrêt 

  

# --- INPUT UTILISATEUR --- 

password = input("Entrez un mot de passe à tester (max 6 caractères conseillés) : ") 

  

if len(password) > MAX_LENGTH: 

    print(f"[!] Mot de passe trop long pour la démo (max {MAX_LENGTH}).") 

    exit() 

  

# alphabet utilisé (modifiable pour démo) 

chars = string.ascii_lowercase + string.digits 

  

print(f"\n[+] Début du brute force sur '{password}'...") 

print(f"[+] Alphabet utilisé : {chars}") 

print(f"[+] Longueur : {len(password)} caractères\n") 

  

start_time = time.time() 

attempt_count = 0 

  

found = False 

  

# --- BRUTE FORCE --- 

for attempt in itertools.product(chars, repeat=len(password)): 

    attempt_count += 1 

    attempt = ''.join(attempt) 

  

    # Vérification 

    if attempt == password: 

        found = True 

        break 

  

    # Vérification du temps 

    if time.time() - start_time > TIME_LIMIT: 

        print("\n[!] Temps limite atteint, arrêt de la recherche.") 

        break 

  

end_time = time.time() 

elapsed = end_time - start_time 

  

# --- RÉSULTATS --- 

print("\n===== RÉSULTATS =====") 

  

if found: 

    print(f"Mot de passe trouvé : {attempt}") 

else: 

    print("Mot de passe non trouvé") 

  

print(f"Temps écoulé : {elapsed:.2f} secondes") 

print(f"Nombre de tentatives : {attempt_count}") 

  

if elapsed > 0: 

    print(f"Vitesse : {attempt_count / elapsed:.0f} tentatives/seconde") 
