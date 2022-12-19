#Creating a Function
def name():
    print("Preeti")

#Calling a Function
    
def name():
    print("Preeti")
name()

#Arguments

def arg(fname):
    print("Bachelor's Of  " + fname)

arg("engineering ")
arg("Computer Application")
arg("Commerce")
arg("Science")


  # Arbitrary Arguments *args

def hobby(*hobbies):
     print("My Hobbies are " + hobbies[3])

hobby("Reading ","Writing","Gardening","Searching New things on the Internet")

  #Keyword Arguments

def hobby(hobby1, hobby2,hobby3,hobby4):
     print("My Hobbies are " + hobby1)

hobby(hobby1="Reading ",hobby2="Writing",hobby3="Gardening",hobby4="Searching New things on the Internet")


