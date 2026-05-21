import itertools
import string
import time
import hashlib

# --- PARAMÈTRES ---
MAX_LENGTH = 8
TIME_LIMIT = 3600

# alphabet utilisé
chars = string.ascii_lowercase + string.digits + string.ascii_uppercase

# --- INPUT UTILISATEUR ---
password = input("Entrez un mot de passe à tester (max 6 conseillés) : ")

if len(password) > MAX_LENGTH:
    print(f"[!] Mot de passe trop long pour la démo (max {MAX_LENGTH}).")
    exit()

# On transforme le mot de passe en hash (simulation cible)
# (MD5 juste pour la démo)
target_hash = hashlib.md5(password.encode()).hexdigest()

print(f"\n[+] Début brute force HASH sur '{password}'...")
print(f"[+] Alphabet utilisé : {chars}")
print(f"[+] Longueur : {len(password)} caractères")
print(f"[+] Hash cible : {target_hash}\n")

start_time = time.time()
attempt_count = 0

found = False

# --- BRUTE FORCE ---
for attempt in itertools.product(chars, repeat=len(password)):
    attempt_count += 1
    attempt = ''.join(attempt)

    #on hash chaque tentative
    attempt_hash = hashlib.md5(attempt.encode()).hexdigest()

    # comparaison des HASH
    if attempt_hash == target_hash:
        found = True
        break

    # timeout
    if time.time() - start_time > TIME_LIMIT:
        print("\n[!] Temps limite atteint, arrêt.")
        break

# --- RÉSULTATS ---
end_time = time.time()
elapsed = end_time - start_time

print("\n===== RÉSULTATS =====")

if found:
    print(f"[✔] Mot de passe trouvé : {attempt}")
else:
    print("[✘] Mot de passe non trouvé")

print(f"Temps écoulé : {elapsed:.2f} secondes")
print(f"Nombre de tentatives : {attempt_count}")

if elapsed > 0:
    print(f"Vitesse : {attempt_count / elapsed:.0f} tentatives/seconde")