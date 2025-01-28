#!/usr/bin/env python3
"""Studenut module
get_logins parses data.txt with fio and login, example:

Невеличка Проблема ; Immortalgleam
Най Буде;annetto-2

"""
import requests

def get_logins(filename, url="https://github.com/"):
    """Get fio and logins from file filename
    
    Args:
        filename - path to file with fio and logins. Example:
           Невеличка Проблема ; Immortalgleam
           Най Буде;anetto-2

    Returns:
        lists of dicts with "fio" and "login" parsed filename
        Example:
        [
          {'fio': 'Невеличка Проблема', 'login': 'Immortalgleam'},
          {'fio': 'Най Буде', 'login': 'anetto-2'}
        ]

     Raises:
         ValueError: if bad filename format (no ; in line)
         RuntimeError: if no login found at github.com
    """
    res = []
   
    with open(filename,"r", encoding="utf-8") as file_:
        for line in file_:
            try:
                fio, login = line.split(";")
                fio = fio.strip()                
                login = login.strip()
            
                print(f"fio={fio} login={login}")
                res.append({
                    "fio": fio,
                    "login": login,
                })
                repo_url = f"{url}{login}"
                print(f"repo is {repo_url}")
                responce = requests.get(repo_url)
                print(responce)
                if responce.status_code != 200:
                    raise RuntimeError("no such user")
            except ValueError as err:
                print(f"Cannot parse file: {err}")
                raise

    return res

def main():
    """Main func
    """
    filename = "data/data.txt"
    return get_logins(filename)

if __name__ == "__main__":
    print (main())







