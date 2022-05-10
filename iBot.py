import time

name={"ATE186":"Murali","A":"b","ATE223":"Sivathanu"}

id=input("EMP ID: ")

for i in name:
    if i ==id.upper():
        print("Hi "+name[id.upper()])

        time.sleep(5)
        reply = input("How are you...?")
        if reply.upper()=="FINE":
            print("Good to hear")

        time.sleep(5)

        reply1 = input("How was your testing..?")

        if reply1.lower()=="bad":
            print("\U0001f600\U0001f600\U0001f600\U0001f600\U0001f600\U0001f600")
            time.sleep(5)
            print("Don't warry you will get lot of bugs tomorrow")

            time.sleep(2)
            print("Don't Give up")
            time.sleep(2)
            print("Thank you dear")


        elif reply1.lower()=="good":
            time.sleep(2)
            print("Sooper, Got lot of bugs...!")
            time.sleep(2)
            print("Thank you dear")


