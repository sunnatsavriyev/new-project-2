


lst = [
    {
        "name":"apple",
        "nima olasiz":["notebook","telefon","soat"],
        "telefon turi":["11pro","12pro","13pro"],
        "notebook turi":["hp","acer","lenovo","asus"],
        "notebook xotirasi":["1 terrabayt","500 gigabayt","250 gigabayt"],
        "soat turi":["iwatch","iwatchpro","i15"],
        "colors":["oq","qora","yashil"],
    },
    {
        "name":"samsung",
        "nima olasiz":["notebook","televizor","telefon"],
        "notebook turi":["hp","acer","lenovo","asus"],
        "notebook xotirasi":["1 terrabayt","500 gigabayt","250 gigabayt"],
        "televizor turi":["32dyumli","42dyumli","52dyumli"],
        "telefon turi":["11s","12s","13s"],
        "colors":["oq","qora","yashil"],
    },
    {
        "name":"artel",
        "nima olasiz":["notebook","televizor","telefon"],
        "notebook turi":["hp","acer","lenovo","asus"],
        "notebook xotirasi":["1 terrabayt","500 gigabayt","250 gigabayt"],
        "televizor turi":["32dyumli","42dyumli","52dyumli"],
        "telefon turi":["1p","2p","3p"],
        "colors":["oq","qora","yashil"],
    }
]

menyu = input("qaysi brendni tanlaysiz(apple/samsung/artel): ")


class Bozor():
    def __init__(self,lst,menyu):
        self.lst = lst
        self.menyu = menyu

    def Apple(self):
        mahsulot = input(self.lst[0]["nima olasiz"])
        if mahsulot == "telefon":
            t = input(self.lst[0]["telefon turi" ])
            if t == "11pro":
                r = input(self.lst[0]["colors" ])
                if r == "oq":
                    print("oq rangli 11promiz 200$!, to'lovni kartangiz orqali  amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 11promiz 400$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 11promiz 600$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "12pro":
                r = input(self.lst[0]["colors" ])
                if r == "oq":
                    print("oq rangli 12promiz 200$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 12promiz 400$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 12promiz 600$ to'lovni kartangiz orqali amalga oshiring!")

            else :
                r = input(self.lst[0]["colors" ])
                if r == "oq":
                    print("oq rangli 13promiz 200$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 13promiz 400$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 13promiz 600$ to'lovni kartangiz orqali amalga oshiring!")

        elif mahsulot == "notebook":
            t = input(self.lst[0]["notebook turi"])
            if t == "hp":
                s = input(self.lst[0]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik hp notebookimiz 700$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik hp notebookimiz 500$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik hp notebookimiz 300$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "acer":
                s = input(self.lst[0]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik acer notebookimiz 800$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik acer notebookimiz 600$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik acer notebookimiz 400$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "lenovo":
                s = input(self.lst[0]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik lenovo notebookimiz 600$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik lenovo notebookimiz 400$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik lenovo notebookimiz 200$ to'lovni kartangiz orqali amalga oshiring!")

            else :
                s = input(self.lst[0]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik asus notebookimiz 1000$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik asus notebookimiz 800$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik asus notebookimiz 500$ to'lovni kartangiz orqali amalga oshiring!")

        else :
            t = input (self.lst[0]["soat turi"])
            if t == "iwatch":
                r = input(self.lst[0]["colors" ])
                if r == "oq":
                    print("oq rangli iwatchmiz 100$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli iwatchmiz 200$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli iwatchmiz 300$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "iwatchpro":
                r = input(self.lst[0]["colors" ])
                if r == "oq":
                    print("oq rangli iwatchpromiz 150$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli iwatchpromiz 250$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli iwatchpromiz 350$ to'lovni kartangiz orqali amalga oshiring!")

            else :
                r = input(self.lst[0]["colors" ])
                if r == "oq":
                    print("oq rangli i15miz 200$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli i15miz 300$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli i15miz 350$ to'lovni kartangiz orqali amalga oshiring!")

    def Samsung(self):
        mahsulot = input(self.lst[1]["nima olasiz"])
        if mahsulot == "telefon":
            t = input(self.lst[1][" telefon turi"])
            if t == "11s":
                r = input(self.lst[1]["colors" ])
                if r == "oq":
                    print("oq rangli 11s miz 100$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 11s miz 300$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 11s miz 500$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "12s":
                r = input(self.lst[1]["colors" ])
                if r == "oq":
                    print("oq rangli 12s miz 100$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 12s miz 300$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 12s miz 500$ to'lovni kartangiz orqali amalga oshiring!")

            else :
                r = input(self.lst[1]["colors" ])
                if r == "oq":
                    print("oq rangli 13s miz 100$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 13s miz 300$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 13s miz 500$ to'lovni kartangiz orqali amalga oshiring!")

        elif mahsulot == "notebook":
            t = input(self.lst[1]["notebook turi"])
            if t == "hp":
                s = input(self.lst[1]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik hp notebookimiz 700$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik hp notebookimiz 500$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik hp notebookimiz 300$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "acer":
                s = input(self.lst[1]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik acer notebookimiz 800$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik acer notebookimiz 600$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik acer notebookimiz 400$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "lenovo":
                s = input(self.lst[1]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik lenovo notebookimiz 600$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik lenovo notebookimiz 400$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik lenovo notebookimiz 200$ to'lovni kartangiz orqali amalga oshiring!")

            else :
                s = input(self.lst[1]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik asus notebookimiz 1000$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik asus notebookimiz 800$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik asus notebookimiz 500$ to'lovni kartangiz orqali amalga oshiring!")

        else :
            tt = input(self.lst[1]["televizor turi"])
            if tt == "32dyumli":
                print ("32dyumli televizorimiz 300$ to'lovni kartangiz orqali amalga oshiring!")
            elif tt == "42dyumli":
                print ("42dyumli televizorimiz 400$ to'lovni kartangiz orqali amalga oshiring!")
            else :
                print ("52dyumli televizorimiz 500$ to'lovni kartangiz orqali amalga oshiring!")



    def Artel(self):
        mahsulot = input (self.lst[2]["nima olasiz"])
        if mahsulot == "telefon":
            t = input (self.lst[2]["telefon turi"])
            if t == "1p":
                r = input(self.lst[2]["colors" ])
                if r == "oq":
                    print("oq rangli 1p miz 300$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 1p smiz 500$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 1p miz 800$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "2p":
                r = input(self.lst[2]["colors" ])
                if r == "oq":
                    print("oq rangli 2p miz 300$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 2p miz 500$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 2p miz 800$ to'lovni kartangiz orqali amalga oshiring!")

            else :
                r = input(self.lst[2]["colors" ])
                if r == "oq":
                    print("oq rangli 3p miz 300$! to'lovni kartangiz orqali amalga oshiring!")
                elif r == "qora":
                    print("qora rangli 3p miz 500$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print("yashil rangli 3p miz 800$ to'lovni kartangiz orqali amalga oshiring!")
        
        elif mahsulot == "notebook":
            t = input(self.lst[2]["notebook turi"])
            if t == "hp":
                s = input(self.lst[2]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik hp notebookimiz 700$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik hp notebookimiz 500$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik hp notebookimiz 300$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "acer":
                s = input(self.lst[2]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik acer notebookimiz 800$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik acer notebookimiz 600$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik acer notebookimiz 400$ to'lovni kartangiz orqali amalga oshiring!")

            elif t == "lenovo":
                s = input(self.lst[2]["notebook xotirasi"])
                if s == "1 terrabayt":
                    print ("1 terrabaytlik lenovo notebookimiz 600$ to'lovni kartangiz orqali amalga oshiring!")
                elif s == "500 gigabayt":
                    print ("500 gigabaytlik lenovo notebookimiz 400$ to'lovni kartangiz orqali amalga oshiring!")
                else:
                    print ("250 gigabaytlik lenovo notebookimiz 200$ to'lovni kartangiz orqali amalga oshiring!")

        else :
            tt = input(self.lst[1]["televizor turi"])
            if tt == "32dyumli":
                print ("32dyumli televizorimiz 200$ to'lovni kartangiz orqali amalga oshiring!")
            elif tt == "42dyumli":
                print ("42dyumli televizorimiz 300$ to'lovni kartangiz orqali amalga oshiring!")
            else :
                print ("52dyumli televizorimiz 500$ to'lovni kartangiz orqali amalga oshiring!")

newclass = Bozor(lst,menyu)

if menyu == "apple":
    newclass.Apple()
elif menyu == "samsung":
    newclass.Samsung()
else:
    newclass.Artel()