import hashlib
import time

TABLE_FILE = "rainbow_table.txt"

password = input("Mot de passe cible (clair, démo) : ")
target_hash = hashlib.md5(password.encode()).hexdigest()

print("\n[+] Attaque via rainbow table")
print(f"[+] Hash cible : {target_hash}\n")

# =========================================================
# 1) CHARGEMENT TABLE (hors chrono attaque)
# =========================================================
print("[+] Chargement de la table...")

load_start = time.time()

table = {}

with open(TABLE_FILE, "r", encoding="utf-8") as f:
    for line in f:
        try:
            h, pwd = line.strip().split(":", 1)
            table[h] = pwd
        except ValueError:
            continue

load_end = time.time()

print(f"[+] Table chargée : {len(table)} entrées")
print(f"[+] Temps chargement : {load_end - load_start:.2f} sec\n")

# =========================================================
# 2) ATTAQUE (ce que tu veux mesurer)
# =========================================================
print("[+] Recherche du hash...\n")

attack_start = time.time()

if target_hash in table:
    found = True
    result = table[target_hash]
else:
    found = False
    result = None

attack_end = time.time()

# =========================================================
# RÉSULTATS
# =========================================================
print("\n===== RÉSULTATS =====")

if found:
    print(f"[✔] Mot de passe trouvé : {result}")
else:
    print("[✘] Mot de passe non trouvé")

print(f"Temps attaque pur : {attack_end - attack_start:.8f} sec")