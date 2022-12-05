# try -> something that might cause exception
try:
    files = open("file_never_exist.txt")
# except -> do this if there was exception
except FileNotFoundError:
    print("error")
# else -> do this if there was no exception
else:
    print("there was no error")
# finally -> this will run after try either have exception or not
finally:
    print("my code run!!")

user = int(input("masukan angka 1 - 5 :"))

if user > 5:
    # raise -> for making our own exception
    raise ValueError("angka tidak bisa lebih besar drpd 5")
