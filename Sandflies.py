# Sandflies - Sam Harris: 2024
import sys
import time
import msvcrt 

def print(text, delay=0.06):
    for char in text:
        if msvcrt.kbhit():
            sys.stdout.write(text[text.index(char):])
            sys.stdout.flush()
            break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def chapter1_intro_airport():
    print("Sandflies - Written and programmed by: Sam Harris / Gordon.mdl")
    print("\n2006, The Iraq War have just met the half way mark. Violence had only grew and there have been continuous anti-coalition attacks.")
    print("But during all this, another problem had just begun...")
    print("\nYou are Leon, part of the Service and Clarification Group (S.C.G), assigned by the CIA to recover a")
    print("highly classified weapon which is held by a group, planning to release the toxic gas on the USA.")
    print("The mission is to find out why they're doing it, and prevent the group from releasing it.")
    print("\nOperation Sandflies: ACTIVE")
    print("\nWARNING: This game focuses on the choices you make, characters will remember what you say or act.")
    print("Be smart with your choices, good luck...")
    print("\nChapter 1: Code 2")
    print("\nYou stare out into the airplane window, looking at the lights below. You've now landed in Iraq, Karma.")
    print("You gather your gear and exit the airport to meet up with your friend, Myles.")
    print("An old pal you met when you joined the S.C.G, the last time you spoke to him was about 2 years ago. Time flys doesn't it?")
    print("You see a silhouette of him in the distance, you walk over and meet him face to face.")
    print("\nLeon: \"No time, no see.\"")
    print("\nMyles doesn't reply... He looks around a bit, he seems conscious.")
    print("\nLeon: \"You alright, Myles?\"")
    print("Myles: \"I’m fine, it’s just... I'm just worried, don't want anything to go rogue.\"")
    print("Leon: \"We need to stay sharp on this mission.\"")
    print("Myles: \"I know, I know...\"")
    print("\nThe both of you wait for the S.C.G crew to come pick you up, what conversation should you bring up in the meantime?")
    print("\nChoices:")
    print("1: Ask more about the mission.")
    print("2: Ask about Myles' past incident.")

def chapter1_choice_airport():
    choice = input("\nEnter your choice (1 or 2): ")
    global is_player_aware_of_leader
    if choice == "1":
        is_player_aware_of_leader = True
        print("\nLeon: \"Have you got any more intel about this mission?\"")
        print("Myles: \"Yeah, I've got some information. The leader of this group is Rurik. His family died in a US-caused bomb during the start of the Iraq war.")
        print("He worked alongside Osama Bin Laden until he formed his own group here.\"")
        print("\nNew information: Group Leader")
    elif choice == "2":
        is_player_aware_of_leader = False
        print("\nLeon: \"How are you after that incident?\"")
        print("Myles: \"Is that important?\"")
        print("Leon: \"I just wanted to know, it's a tough thing to handle.\"")
        print("Myles: \"I'm fine.\"")
        print("\nMyles will remember that...")
    else:
        print("Invalid choice. Please enter 1 or 2.")

def chapter1_scene_van():
    print("\nJust before you know it, the S.C.G crew comes driving in a white van. One of them gets out and goes to meet both of you.")
    print("\nMember #1: \"Hey, are you guys ready for this?\"")
    print("Leon: \"Ready as a fiddle.\"")
    print("Member #1: \"Let's do this then...\"")
    print("\nYou and Myles enter the back of the van, gearing up with goverment equipment.") 
    print("Once you're dressed in combat armor the driver steps on it, taking you to the last known location of the group.")
    print("The S.C.G members exchange glances with you, it's starts to get awkward until someone breaks the silence.")
    print("\nMember #1: \"What’s the plan?\"")
    print("Myles: \"Well, I say me and my friend sneak around the back of the building. We'll take them out one by one, don't wanna draw any attention.\"")
    print("Member #1: \"What about us?\"")
    print("Myles: \"If anything goes to shit, we'll contact you on our radio.\"")
    print("Member #3: \"Sound like a plan...\"")
    print("Member #1: \"Who’s this group leader anyway?\"")

    # Response based on previous choice
    if is_player_aware_of_leader:
        print("Leon: \"His name's Rurik, he worked alongside Osama Bin Laden before forming his own group.\"")
        print("Member #1: \"Osama Bin Laden? What's his deal?\"")
        print("Leon: \"His family died in a explosion, it was caused by the US. That's his deal, to get revenge for what they did.")
    else:
        print("Myles: \"His name is Rurik, his family died in a explosion, and he worked for Osama Bin Laden before. Now he’s got his own group.\"")
        print("\nNew information: Group Leader")

    print("\nMember #4: \"Guys, we're here. Lock and load, everyone.\"")
    print("\nThe car pulls up to an old abandoned building in the middle of nowhere.")
    print("The group exits the van, You and Myles head around to the back while the rest of the crew waits by the van.")
    print("\nLeon: \"Remember Myles, we gotta stay sharp.\"")
    print("Myles: \"You don't need to tell me twice.\"")
    print("\nYou're now at the back door, how should you apporach?")
    print("\nChoices:")
    print("1: Go in and stick with the plan.")
    print("2: Let's do it the old fashioned way.")

def chapter1_choice_old_building():
    global is_gun_loud
    is_gun_loud = False
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ")
        
        if choice == "1":
            is_gun_loud = False
            print("\nYou decide to stick with the plan, you and Myles enter the building quietly. You quickly find out no-one is here, they must of gotten away before you showed up.")
            print("\nMyles: \"Code 2, This is Myles. They're not here, I repeat. They're not here...\"")
            print("Leon: \"They must've relocated awhile ago.\"")
            print("Myles: \"Leon, how about we search the second floor while the rest of the crew search the first floor.\"")
            print("Leon: \"All good, Myles.\"")
            print("\nYou decide to split up on the second level. The rest of the crew come through and search the first level.")
            print("You check every room, everything feels old and dusty and you find nothing.")
            print("Once your done, you realise you misseed one more room. Searching it you find a note laying on a desk.")
            print("it reads, \"This note is for the last remaining group who missed the meeting. We're moving our postion to the west, we found a lake not too far. You'll find us...\"")
            print("\nNew information: Group Postion")

            break
        elif choice == "2":
            is_gun_loud = True
            print("\nLeon: \"Myles, how about we do it the old fashioned way?\"")
            print("Myles: \"You're joking, right?\"")
            print("Leon: \"Come on, I know it's not smart but it'll just be like old times!\"")
            print("Myles: \"Leon, I think you're the one who needs to stay sharp here.\"")
            print("\nMyles will remember that...")
        else:
            print("Invalid choice. Please enter 1 or 2.")

def chapter1_scene_old_building():
    print("\nYou exit the room, getting down stairs to join back up with the crew.")
    print("Leon: \"Everyone, I found something.\"")
    print("Member #4: \"What is it?\"")
    print("\nYou read the note, everyone quickly turns silent.")
    print("\nMyles: \"Pass me that real quick...\"")
    print("You hand the note over to Myles, he seems confused.")
    print("\nLeon: \"I say we head over to the west now.")
    print("Myles: \"No, We shouldn't do this.")
    print("Leon: \"What's wrong?\"")
    print("Myles: \"Doesn't this strike something? What if it's an ambush, why would they leave a note like this behind?\"")    
    print("Member #2: \"Wait, how would they know we were coming?\"")
    print("Myles: \"I... I don't know, but I don't wanna find out.\"")
    
    # Response based on previous choice
    if is_player_aware_of_leader:
        print("Leon: \"Myles, even if it is, they could've waited for that long. In fact, they might be moving destenations arleady! This note's pretty old...")
        print("\nThe room is filled with silence with only you waiting for Myles' response.")
        print("\nMyles: \"Alright, alright.. I'll do it, only becuase of you Leon...")
        print("\nYou have calmed down Myles, He will remember that...")
    else:
        print("Leon: \"Myles, calm down... You've got to trust me on this. You've always have, and it always worked out.")
        print("\nThe room is filled with silence with only you waiting for Myles' response.")
        print("He looks down a bit, hesitant to agree on this choice of yours.")
        print("\nMyles: \"Alright, alright... I'll do it then.")

    print("\nAfter the conflict, everyone leaves the old building behind to collect more dust and moss.")
    print("You get in the van, the crew is looking around a bit until you storm in.")
    print("\nLeon: \"Alright... We need to head west, there should be a lake or some sort of camp going that way. Driver, step on it!\"")
    print("\nThe driver hits the pedal hard and the car speeds away to the main road...")
    print("\nChapter 2: \"I have business to be dealt with.\"")

def end_game():
    print("\nOperation Sandflies: CLOSED")
    choice = input("Would you like to restart? (Type 'restart' to play again, If not just close the window.): ").strip().lower()
    
    if choice == 'restart':
        start_sandflies()
    else:
        exit()

def start_sandflies():
    chapter1_intro_airport()
    chapter1_choice_airport()
    chapter1_scene_van()
    chapter1_choice_old_building()
    chapter1_scene_old_building()
    end_game()

# Start the game
start_sandflies()