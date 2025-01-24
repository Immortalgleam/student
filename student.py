#!/usr/bin/env python3

def main():
    msg = "hi hello again"
    print(msg) 
   
    with open("data.txt","r", encoding="utf-8") as file_:
        for line in file_:
            try:
                fio, login = line.split(";")
            
                print(f"fio = {fio} login = {login}")
            except ValueError as err:
                print(f"Cannot parse file: {err}")
                return

if __name__ == "__main__":
    main()







