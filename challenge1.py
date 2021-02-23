
import json

def main():
        with open("challenge.json", "r") as chall1:
            chall1string = chall1.read()
        
        chall1decoded = json.loads(chall1string)

        print(chall1decoded)

        for element in chall1decoded:
            print("Name : ", {element["name"]})
            print("Email: ", {element["email"]})
            print("Phone: ", {element["phone"]})
            print("Adress: ", {element["address"]})

if __name__ == "__main__":
    main()


