#!/usr/bin/env python3
"""Studenut module
get_logins parses data.txt with fio and login, example:

pfrfm;tata
Невеличка Проблема;annetto-
Най Буде;anetto-2

"""
def get_logins(filename):
    """Get fio and logins from file filename
    
    Args:
        filename - path to file with fio and logins. Example:
           pfrfm;tata
           Невеличка Проблема;annetto-
           Най Буде;anetto-2
    Returns:
        None
    """
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
    """Main func
    """
    filename = "data.txt"
    get_logins(filename)

if __name__ == "__main__":
    main()







