print "welcome to pypet!"

cat ={
"name" : "fluffy",
"age" : 5,
"weight" : 9.5,
"hungry" : False,
"play" : False,
"sleep" : True,  
"photo" : "(=^o.o^=)___",
}

mouse ={
  "name" : "squeaker",
  "age" : 6,
  "weight" : 1.5,
  "hungry" : True,
  "play" : True,
  "sleep" : False,
  "photo" : "<:3 )~~~"
}

pets = [cat, mouse]


print "hello" + cat["name"]
print cat["photo"]
print "hello" + mouse["name"]
print mouse["photo"]

def feed(pet):
  if pet["hungry"] == True:
    pet["hungry"] = False
    pet["weight"] = pet["weight"] + 1
    print "nomnomnom!"
  else:
    print "The pypet is not hungry!"
    
def play(pet):
  if pet["play"] == True:
    pet["play"] = False
    print "I want to play!"
  else:
    print "The pypet does not want to play!"

def sleep(pet):
  if pet["sleep"] == True:
    pet["sleep"] = False
    print "ZZZZZZZZZZZ"
  else:
    print "Not Sleepy!!"
    
    
for pet in pets:
  print "______________________"
  print "Hello" + pet ["name"] + "!"
  print pet["photo"]
  print 'Weight: ' + str(pet['weight'])
  play(pet)
  feed(pet)
  sleep(pet)
  print 'Weight: ' + str(pet['weight'])
  print "__________________________"
