import itertools
import string
import time

# --- PARAMÈTRES ---
MAX_LENGTH = 10
TIME_LIMIT = 3600

# fichier dictionnaire (RockYou à côté du script)
DICT_FILE = "rockyou.txt"

# --- INPUT ---
password = input("Entrez un mot de passe à tester (max 6 conseillé) : ")

if len(password) > MAX_LENGTH:
    print(f"[!] Mot de passe trop long pour la démo (max {MAX_LENGTH}).")
    exit()

chars = string.ascii_lowercase + string.digits + string.ascii_uppercase

print(f"\n[+] Début attaque sur '{password}'")
print("[+] Étape 1 : dictionnaire (RockYou)")
print("[+] Étape 2 : brute force si échec\n")

start_time = time.time()
attempt_count = 0

found = False


# =========================================================
# 1) DICTIONNAIRE ROCKYOU
# =========================================================
try:
    with open(DICT_FILE, "r", encoding="latin-1") as f:
        for line in f:
            attempt_count += 1
            attempt = line.strip()

            if attempt == password:
                print("[✔] Trouvé dans RockYou !")
                found = True
                break

            if time.time() - start_time > TIME_LIMIT:
                print("\n[!] Temps limite atteint (dictionnaire).")
                break

except FileNotFoundError:
    print("[!] Fichier rockyou.txt introuvable, passage direct brute force.")


# =========================================================
# 2) BRUTE FORCE SI PAS TROUVÉ
# =========================================================
if not found:
    print("\n[+] Passage au brute force...\n")

    for attempt in itertools.product(chars, repeat=len(password)):
        attempt_count += 1
        attempt = ''.join(attempt)

        if attempt == password:
            found = True
            break

        if time.time() - start_time > TIME_LIMIT:
            print("\n[!] Temps limite atteint (brute force).")
            break


# =========================================================
# RÉSULTATS
# =========================================================
end_time = time.time()
elapsed = end_time - start_time

print("\n===== RÉSULTATS =====")

if found:
    print(f"[✔] Mot de passe trouvé : {password}")
else:
    print("[✘] Mot de passe non trouvé")

print(f"Temps écoulé : {elapsed:.2f} secondes")
print(f"Nombre de tentatives : {attempt_count}")

if elapsed > 0:
    print(f"Vitesse : {attempt_count / elapsed:.0f} tentatives/seconde")