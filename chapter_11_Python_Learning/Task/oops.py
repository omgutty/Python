class person:
    name= None
    id=None
    age= None


    def talk(s):
        print("I can talk")

    def sleep(s, name):
        print("I can sleep ")
        print("sleep", name)

    # def sleep(s,name):
    #     print ("I can sleep 2 ")
    #     return None

def functionoutsite():
    print ("output")

siva= person()
om= person()

print (siva.name)
om.sleep("omk")

