import hashlib

INPUT_FILE = "rockyou.txt"
OUTPUT_FILE = "rainbow_table.txt"

def hash_pwd(pwd: str) -> str:
    return hashlib.md5(pwd.encode(errors="ignore")).hexdigest()

print("[+] Génération de la table hash -> password")
print("[+] Lecture de :", INPUT_FILE)

table_size = 0

with open(INPUT_FILE, "r", encoding="latin-1") as fin, open(OUTPUT_FILE, "w", encoding="utf-8") as fout:

    for line in fin:
        pwd = line.strip()

        if not pwd:
            continue

        h = hash_pwd(pwd)

        # format simple : hash:password
        fout.write(f"{h}:{pwd}\n")

        table_size += 1

        if table_size % 100000 == 0:
            print(f"[+] {table_size} entrées traitées...")

print("\n[✔] Terminé")
print(f"[✔] {table_size} entrées écrites dans {OUTPUT_FILE}")