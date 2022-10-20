# dictionary (dict) => associative array => seperti object di JS.
print("==== DICTIONARY ==== \n")
biodata = {"nama": "kelvin", "umur": 20, "semester": 1}
print(biodata["nama"])
print(biodata["umur"])
print(biodata["semester"])

# metode
print("\n==== METODE ====")

# len
print("\nLEN")
LEN_DICT = len(biodata)
print(LEN_DICT)

# CHECKING KEY
print("\nCHECKING KEY")
KEY = "anjay"
CHECK_KEY = KEY in biodata
hasil = ""
if CHECK_KEY:
    hasil = "ada"
else:
    hasil = "tidak ada"

print(f"{KEY} {hasil} di biodata")

# get value
print("\nGETTING VALUE")
hasil = biodata.get("nama", "maaf anda kurang beruntung.")
print(f"nama di biodata adalah {hasil}")

# update
print("\nupdate")
biodata.update({"prodi": "teknologi informasi"})
biodata.update({"umur": 30})
print(biodata)

# delete
print("\ndelete")
del biodata["umur"]
print(biodata, "\n")

# looping pada dictionary
print(" LOOPING PD DICT ".center(30, "="))

# untuk mendapat keys
print("\nuntuk mendapat key")
for keterangan in biodata:
    print(keterangan)

# untuk mendapat item pada key
print("\nuntuk mendapat item")
for item in biodata.values():
    print(f"{item}")

# untuk mendapat key dan value
print("\nuntuk mendapat key dan value")
for key, value in biodata.items():
    print(f"{key} : {value}")
