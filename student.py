#!/usr/bin/env python3

def get_logins(filename):
    res = []
   
    with open(filename,"r", encoding="utf-8") as file_:
        for line in file_:
            try:
                fio, login = line.split(";")
                fio = fio.strip()                
                login = login.strip()
            
                print(f"fio = {fio} login = {login}")
                res.append({
                    "fio": fio,
                    "login": login,
                })
            except ValueError as err:
                print(f"Cannot parse file: {err}")
                return

    print(res)

def main():
    filename = "data.txt"
    get_logins(filename)

if __name__ == "__main__":
    main()







