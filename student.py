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
        lists of dicts with "fio" and "login" parsed filename
        Example:
        [
          {'fio': 'pfrfm', 'login': 'tata'},
          {'fio': 'Невеличка Проблема', 'login': 'annetto-'},
          {'fio': 'Най Буде', 'login': 'anetto-2'}
        ]

     Raises:
         ValueError: if bad filename format (no ; in line)
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
                raise

    return res

def main():
    """Main func
    """
    filename = "data.txt"
    return get_logins(filename)

if __name__ == "__main__":
    print (main())







