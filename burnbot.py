import random

print("There it is! The bridge of death! Look, There's the old man from scene 24! What is he doing here? He is the keeper of the Bridge of Death, he asks each traveler three questions. Five questions. Five questions! He who answeres the Three questions-  Five questions. May cross safely. Else you are cast into the gorge of eternal peril.")
print("Ask me the questions bridgekeeper, I am not afraid!")
name = input("WHAT is your name?")
quest = input("WHAT is your quest?")
dob = input("WHAT is your place of birth?")
occ = input("WHAT is your occupation?")
num =  random.randrange(2,4)
thirdone = ''
inthepit = False
if num == 2:
    thirdone = input('WHAT is your favorite color?')
    print(f"right,{name} from {dob} the {occ}. Off you go.")
elif num == 3:
    thirdone = input('WHAT is the airspeed velocity of an unlaiden swallow?')
    inthepit = True
    if thirdone.lower() == "what do you mean? an african or european swallow?":
        print("'well I don't know that! AAAAAaaaaah' the bridgekeeper hollars before he himself falls victim to his own trap.")
        quit()

else:
    thridone = input("WHAT is the capital of Assyria")
if inthepit == True:
    print(f"'Well I don't know that!AAAAAaaaahh' you exclaim as you are magically flung from the bridge into the gorge of eternal peril. 'sir {name} the {occ} of {dob} really was a stupid one, i bet they didn't even know the airspeed velocity of an unlaiden swallow!' is the last thing you hear before plummeting into the gorge of eternal peril. They never wouldve completed their quest, i mean '{quest}' isnt really even that hard, yet they seemed to be making no progress whatsoever.")
