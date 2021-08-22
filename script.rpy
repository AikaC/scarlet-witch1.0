# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Cecil = Character("Cecil")
define Crowd = Character(_("Crowd"))
define Ditte = Character("Ditte")
define King = Character(_("King"))
define NPC = Character(_("Farmer wife"))
define NPC2 = Character(_("Farmer"))
define NPC3 = Character(_("Vendor"))
define Sha = Character(_("The Shadow"))
define Rud = Character("Rudolph")
define icognito = ("???")

# background images

image capital = "BG_capital.png"
image effect = "BG_effect.jpg"
image farmerHouse = "BG_Farmer_House.jpg"
image forest_hut = "BG_Forest_Hut.jpg"
image hut = "BG_Forest_Hut2.jpg"
image kingOffice = "BG_office.jpg"
image runAway = "BG_RunAway.png"
image village = "BG_Small_Village.jpg"

# Characters images

# Cecil

image Cecil body = "Cecil_body.png"
image CecilBaby = "Cecil_body2-a.png"
image Cecil2 = "Cecil_body2.png"
image Cworry = "Cecil_worryFace.png"
image Cworry2 = "Cecil_worryFace2.png"
image Chappy = "Cecil_happyFace.png"
image Crugas = "CecilRugas.png"
image Cshappy = "Cecil_happyFace2.png"

#Ditte

image Dt = "Ditte.png"
image DAFace = "DitteAngryFace.png"
image DSFace = "DitteSadFace.png"
image DBody = "DitteBody.png"
image DBody2 = "DitteBodyHurt.png"

#King
image Kingbody = "King_body.png"
image KingAngryF = "King_angryF.png"

# NPC
image NPCbody = "NPC_body.png"
image NPCangryFace = "NPC_angryF.png"
image NPCsadFace = "NPC_SadF.png"

# NPC2
image NPC2body = "NPC2_body.png"
image NPC2angryFace = "NPC2_angryF.png"

#NPC3
image NPC3body = "NPC3_body.png"
image NPC3angry = "NPC3_angryFace.png"
image NPC3happy = "NPC3_happyFace.png"

# Rudolph
image Rudbody = "Rudolph_body.png"
image Rudangry = "Rudolph_angryF.png"
image Rudhappy = "Rudolph_happyFace.png"
image Rudsad = "Rudolph_sadF.png"
image Rudsup = "Rudolph_supF.png"

#Shadow
image shadowBody = "Shadow_body.png"
image shadoweyes = "Shadow_eyesIDLE.png"
image shadoweyes2 = "Shadow_eyes2.png"
image shadoweyes3 = "Shadow_eyes3.png"

# The game starts here.

label start:

    show forest_hut
    show Cecil body
    show Cworry

    play music "audio/HUT.mp3"

    Cecil "I know I shouldn't be walking around pregnant in the forest."
    Cecil "I'm about to give birth at any moment..."
    Cecil "But the villagers still don't like me..."
    Cecil "I need to make sure I have everything I need with me. {w}At least for a few days."
    Cecil "I won't have the strength to walk around doing heavy tasks by myself."

    hide Cworry
    show Chappy

    Cecil "It is going to be only you and me, child."

    play sound "audio/447211__gamba-studio__buhos.wav"

    "Cecil heard an owl complain from far away."
    Cecil "... You, me and Ditte. {i}She corrected herself.{/i}"

    hide Chappy
    show Cshappy

    Cecil "Sorry, Ditte. {w}Didn't know you were already up."
    "Cecil found the small key and opened the door."

    hide Cshappy
    show Chappy

    Cecil "And when you are big enough, you’re going to have your own familiar. {i}She said, hyped.{/i}"
    Cecil "An animal willing to seal a contract of mutual protection with you.{p}A life for a life."

    hide Cecil body
    hide Chappy

    "Cecil grabbed the basket again, walked through the door and locked it."

    show hut 
    show Cecil body
    show Chappy
    with dissolve
    hide forest_hut

    Cecil "Everything’s going to be fine."
    "She caressed the big belly, feeling slightly guilty inside for lying about their future."

    hide Cecil body
    hide Chappy
    show effect
    with dissolve

    "It´s been some time since Cecil started living in that hut."
    "It was close enough to go to the village that she secretly assisted but not close enough to completely scare them."
    "Every witch has its own mark. {p}Cecil knew that her red eyes could tell her real nature..."
    "... but there was nothing she could say that would make the villagers believe she was a healer."
    
    show village
    with fade
    hide hut
    hide effect

    #stop music

    #Small Village Scene
    #play music

    "Meanwhile, rumors were running wild in the small village next to the river."

    show NPCbody
    show NPCsadFace

    NPC "Oh lord... Oh lord..."
    NPC "That red-eyed woman in the forest hut..."
    NPC "She is definitely the witch who had decimated entire villages without even blinking!"


    menu:
        "It has to be her!":
            
            hide NPCsadFace
            show NPCangryFace

            NPC "I know, right!?"
            NPC "She is hardly seen in public during the daylight."
            NPC "And everyone here is too scared to face her."
            NPC "After all, this is a really small village, only a few families live here..."

            hide NPCangryFace
            show NPCangryFace

            NPC "... Even fewer after the rumor of the wood’s witch."
            NPC "So, clearly, there are no heroes to save us."

            hide village
            hide NPCbody
            hide NPCangryFace

            jump farmer_house
        "How can you be so sure?":

            hide NPCsadFace
            show NPCsadFace

            NPC "There are numerous stories of a woman with shiny eyes like the blood moon causing the chaos."

            hide NPCsadFace
            show NPCangryFace

            NPC "How can {b}you{/b} be so sure is not her?{p}Why don´t you go there and ask then?"

            hide NPCangryFace
            show NPCsadFace

            NPC "\"Excuse me miss, is it you who are destroying everything you put your foot on?\""

            menu:
                "...":
                    hide NPCsadFace
                    show NPCangryFace

                    NPC "Thought so..."

                    hide NPCangryFace
                    show NPCsadFace

                    NPC "Don't worry. You're not the only one."
                    NPC "We're all scared of her."
                    NPC "There are no heroes to save us from the evil witch in this small village..."

                    hide village
                    hide NPCbody
                    hide NPCsadFace

                    jump farmer_house
                "You look way braver than me.":
                    NPC "Oh... me?!"
                    NPC "I have to ask my husband for help even to catch the snakes that appear on our farm."
                    NPC "All the families here are too weak to make big travels and escape from the witch's grip."

                    hide NPCsadFace
                    show NPCangryFace

                    NPC "I'm not brave.{w}There are no heroes in this small village..."

                    hide village
                    hide NPCbody
                    hide NPCangryFace
                    jump farmer_house

    label farmer_house:

    #play music
    show farmerHouse
    show Rudbody
    show Rudhappy
    with fade

    Rud "I can defeat the witch! {i}The son of the farmers shouted with a sparkle in his eyes.{/i}"

    show Rudbody at right
    show Rudhappy at right
    show NPCbody at left
    show NPCangryFace at left
    with moveinright

    NPC "Sit down and finish your dinner. {i}His mother said sharply.{/i}"
    NPC "You are only twelve, {w}you can't even plow the land without complaining."

    hide NPCbody
    hide NPCangryFace
    hide Rudhappy
    show Rudsad at right

    Rud "But that's different mother, I can be a hero and-"

    show NPC2body at left
    show NPC2angryFace at left
    with moveinleft
    hide Rudsad
    show Rudangry at right
    with dissolve

    NPC2 "No, you can´t."
    NPC2 "When you finish your dinner, you´re going to sleep."
    NPC2 "Looks like you're not getting enough work in the morning."

    hide NPC2body
    hide NPC2angryFace
    show Rudbody at center
    show Rudangry at center
    with moveinleft

    "Rudolph went to his room sulking."
    "He laid down in his bed and waited for the moon to reach the highest spot in the sky.{p}That way, he would be sure everyone was sleeping."
    "So he grabbed a garden grubber and walked to the hut."

    play music "audio/Sneaking in the night.mp3" fadein 1.0
    show forest_hut
    with move
    hide Rudbody
    hide Rudangry

    "The full moon was the only light that illuminated his path."

    show forest_hut
    with vpunch
    hide farmerHouse

    Cecil "Aaaaaah!"

    show Rudbody
    show Rudsup
    with dissolve

    Rud "{i}What is that?{/i}"

    hide Rudbody
    hide Rudsup
    show forest_hut
    with vpunch

    Cecil "{b}Aaaaaah!{/b}"

    show Rudbody
    show Rudsup
    with dissolve

    Rud "{i}Is coming from the hut.{/i}"

    hide Rudbody
    hide Rudsup
    show forest_hut
    with vpunch

    Cecil "{b}AAAAAAH!{/b}"

    show Rudbody
    show Rudsad
    with dissolve

    Rud "..."
    Rud "Make it stop!"
    Rud "..."
    Rud "{i}It stopped...{/i}"
    " Rudolph started to hear a baby crying so he went to the closest window and looked inside."

    hide forest_hut
    hide Rudbody
    hide Rudsad
    show hut
    show Rudbody
    show Rudsup
    with dissolve

    Rud "The Scarlet Witch just gave birth to a son. {i}He whispered in a low tone{/i}"
    "But it was enough for the witch to turn her head in his direction."

    show Rudbody at left
    show Rudsup at left
    show Cecil body at right
    show Cworry at right
    with moveinleft

    Cecil "Who is there?"
    "They locked eyes.{p}Both of them were surprised."
    "They stayed that way for what looked like an eternity..."

    hide Rudbody
    hide Rudsup
    hide Cecil body
    hide Cworry

    menu:
        "Do something":

            show Rudbody
            show Rudangry

            Rud "... I am a hero!{p}I need to do something..."

            hide Rudangry
            show Rudsad

            Rud "But what?"
            "Rudolph looked around searching for the front door."

            hide Rudsad
            show Rudangry

            "He tried to open but it was locked."
            "He raised the garden grubber and..."

            hide Rudangry
            show Rudsad

            "Sudenly an owl snapped it out of his hand and shooshed him."
            "Rudolph started running back to his village."

            hide Rudbody
            hide Rudsad
            hide hut

            jump shout_village
        "Run away":
            "... Until Rudolph broke the hypnosis{w} and ran away."

            hide hut
            jump shout_village

    label shout_village:

    #play music
    show village
    show Rudbody
    show Rudsad
    with fade

    Rud "The Scarlet Witch had a son!{p}The Scarlet Witch had a son!"
    "Wherever Rudolph went through lights started to glow..."
    "... All the villagers listened to the scared boy running in despair in the middle of dawn."

    hide village
    hide Rudsad
    hide Rudbody

    # King´s castle

    play music "audio/SHADOW.mp3" fadein 1.0

    show effect
    with fade

    "The king’s Shadow opened the heavy doors from the royal office."

    show kingOffice
    show shadowBody
    show shadoweyes
    with dissolve
    hide effect

    "She silently knelt in reverence."
    "All her senses were completely aware of any uncommon movement."

    hide shadowBody
    hide shadoweyes
    show Kingbody at right
    show KingAngryF at right
    with dissolve

    King "I’ve heard that a bunch of rebels are gathering in the Weastern Capital to plan an attack against the crown."

    "The king started to talk without looking away from his papers."
    "The Shadow stayed completely mute."

    King "I think you already know where I'm getting into."
    King "Make them an example of what happens to those who oppose me."

    show shadowBody at left
    show shadoweyes at left
    hide Kingbody
    hide KingAngryF
    with dissolve

    Sha "Yes, my king. {i}She finally answered.{/i}"

    hide shadowBody
    hide shadoweyes
    show Kingbody at right
    show KingAngryF at right
    with dissolve

    King "And I don't need to remind you that you are a shadow that can't be revealed."
    King "No one shall suspect that there is a witch working for the king."

    show shadowBody at left
    show shadoweyes at left
    hide Kingbody
    hide KingAngryF
    with dissolve

    Sha "Your wish is an order."

    hide shadowBody
    hide shadoweyes
    with pixellate

    "This was nothing more than a far away whispering{w} since her body was already turning into dark smoke...{w} Like the real shadows."

    hide kingOffice
    show effect
    with fade

    "The king’s witch then went to the Weastern Capital."

    hide effect
    show hut
    with fade

    #forest hut

    play music "audio/HUT.mp3" fadein 1.0

    "Cecil woke up early and realized she had lost consciousness soon after she saw the child at her window."
    "When she came to her senses, the first thing she did was check the baby cradled in her arms..."
    "... His face was swollen, clearly from crying."

    show CecilBaby
    show Chappy
    with dissolve

    Cecil "Welcome, dear. {i}She pressed a kiss on his forehead and then looked around.{/i}"
    Cecil "Now{w} look at this mess!{p}I think it´s cleaning time."

    hide CecilBaby
    hide Chappy
    show Cecil2
    show Cshappy
    with fade

    Cecil "Arf...{w} All done!"

    hide Cshappy
    show Cworry

    Cecil "But that kid from yesterday..."
    Cecil "I can't take that out of my head..."
    Cecil "Are we really safe?{p}Should I investigate?"

    menu:
        "Of course!":
            hide Cworry
            show Cshappy
            Cecil "Yes, one can never be too careful!"

            stop music            
            jump go_to_village

        "It's not that serious":
            Cecil "I shouldn't be worried, it's just a kid."

            hide hut
            hide Cecil2
            hide Cworry

            stop music
            jump dead_end

    label dead_end:

    play music "audio/The chase.mp3"
    show effect
    with fade

    "Both mother and child were in deep sleep that rainy evening."
    "Cecil started getting weak and tired way more easily than before so she needed the double amount of rest."

    show forest_hut
    with fade

    "Ditte was guarding the hut."

    show Dt
    with dissolve

    Ditte "{i}Well,{w} there's nothing to be done about it.{/i}"
    Ditte "{i}I need to protect this place until my master restores her powers again.{/i}"
    Ditte "{i}Thankfully, everything is calm here.{/i}"
    "But a dim light appeared on the horizon."
    Ditte "{i}The villagers are coming this way!?{/i}"
    Ditte "{i}I need to do something before it's too late.{/i}"

    hide Dt
    show NPC2body
    show NPC2angryFace
    with fade

    NPC2 "Together we can do this."

    hide NPC2body
    hide NPC2angryFace
    show Dt
    with dissolve

    "Ditte flew towards them trying to stop their advance."
    Ditte "Stop! You're going after the wrong person!"

    hide Dt
    with pixellate

    "He spoke as he transformed into his humanoid form."

    show DBody
    show DAFace
    with pixellate

    "But his warning was drowned out by a thunder that echoed through the skies."

    "Ditte landed in front of the small crowd that was perilously close to the cabin."

    hide DBody
    hide DAFace
    show NPCbody
    show NPCsadFace
    with dissolve

    NPC "The guardian of the creature!"

    show DBody
    show DAFace
    hide NPCbody
    hide NPCsadFace
    with dissolve

    Ditte "No-"

    hide DBody
    hide DAFace
    show DBody2
    show DSFace
    with dissolve

    "He started, but a long blade pierced his body from behind."
    "The glow in Ditte's eyes was slowly fading."
    Ditte "{i}Sorry, master…{/i} were his last thoughts."

    hide DBody2
    hide DSFace
    show hut
    show Cecil2
    show Cworry
    with fade
    #play music

    Cecil "Ditte!{p}{i}Cecil woke up suddenly with her heart sinking.{/i}"
    Cecil "I can feel it...{p}The contract is breaking..."
    Cecil "A life for a life. That's the deal."
    "Cecil looked at the peacefully sleeping child, a tear began to flow in a silent cry."
    Cecil "I'm sorry my dear. {w} I won't have time to do anything for you"
    Cecil "I can already feel the lifespan leaving me..."
    Cecil "I love you with all my heart."

    hide Cecil2
    hide Cworry
    hide hut
    with fade

    "As fast as the rain started, it ended, as if someone had magically summoned it."

    show NPC2body
    show NPC2angryFace
    with dissolve

    NPC2 "We’re sticking to the plan."
    "Then, not knowing that the Scarlet Witch was no longer in that world..."
    "... the farmer lit a torch and threw it into the wooden hut."
    "A short time later they heard a child crying."

    show NPC2body at right
    show NPC2angryFace at right
    show NPCbody at left
    show NPCsadFace at left
    with moveinright

    NPC "This is too cruel."
    NPC2 "But it's necessary."

    hide NPC2body
    hide NPC2angryFace
    hide NPCbody
    hide NPCsadFace

    "They stayed there until the crying stopped."
    "Until the fire burned the entire hut."
    "Until dawn, when the fire had long gone out and all that was left was scorched rubble."

    return

    label go_to_village:
    play music "audio/HUT.mp3"

    "With everything in order, Cecil opened the window."
    "A slight whistle was all it took for Ditte to appear on her sill."

    hide Cecil2
    hide Cshappy
    show Dt
    with dissolve

    play sound "audio/447211__gamba-studio__buhos.wav"

    Ditte "Hoo."

    show Cecil2
    show Chappy
    with dissolve

    Cecil "I know it's your bedtime,{w} but would you mind taking care of my child while I go out?"

    hide Cecil2
    hide Chappy
    with dissolve

    Ditte "hooo... {i}The owl flew to the baby and curled up on the edge of the crib.{/i}"

    show Cecil2
    show Cshappy
    with dissolve

    Cecil "Thanks."

    hide Cshappy
    show Cworry

    Cecil "I need to see the boy from last night."
    Cecil "A witch has her power temporarily almost nullified when giving birth to a child."
    Cecil "But a simple masquerade spell wouldn't wear me out…{w} Too much."

    hide hut
    hide Dt
    hide Cecil2
    show village
    show NPC3body
    show NPC3happy
    with fade

    #village reunion
    #play music

    NPC3 "Granny Cecil, how are you?"
    "The villagers believed that Cecil was actually an old lady who lived in a village shack with her grandchildren."
    "Of course. Anyone who tried to get to that shack would conveniently forget where he was going."
    NPC3 "I see you heard about the meeting in the square."
    NPC3 " Your grandchildren aren't with you?"

    hide NPC3body
    hide NPC3happy
    show Cecil2
    show Cshappy
    show Crugas
    with dissolve

    Cecil "I asked them to go ahead. {i}She lied.{/i}"

    hide Cecil2
    hide Cshappy
    hide Crugas
    show NPC3body
    show NPC3angry
    with dissolve

    NPC3 "That's not right, you shouldn't be unaccompanied like that."

    hide NPC3angry
    show NPC3happy

    NPC3 "Come on, {w}I'll take you."

    menu:
        "Shall we?":

            hide NPC3body
            hide NPC3happy
            show Cecil2
            show Cshappy
            show Crugas
            with dissolve

            Cecil "Really kind of you, let's go together."

            hide Cecil2
            hide Cshappy
            hide Crugas
            jump square

        "No, thanks":
            hide NPC3body
            hide NPC3happy
            show Cecil2
            show Cshappy
            show Crugas
            with dissolve

            Cecil "Really kind of you, {w}but could you remind me why the commotion?"

            hide Cecil2
            hide Cshappy
            hide Crugas
            show NPC3body
            show NPC3angry
            with dissolve

            NPC3 "I'm surprised you didn't hear little Rudolph yesterday."
            NPC3 "He ran all over the village screaming about the witch having a child."
            NPC3 "We are having a meeting to find out what's going on."

            hide NPC3body
            hide NPC3angry
            show Cecil2
            show Cworry2
            show Crugas
            with dissolve

            Cecil "Oh my... {i}Cecil did the best to keep her expression neutral.{/i}"

            hide Cworry2
            show Cshappy

            Cecil "Go ahead sweetie, {w}I need to rest my legs a little."
            "That wasn't entirely a lie."
            "Cecil felt her legs go weak."
            Cecil "I'll catch up with you kids in no time."

            hide Cecil2
            hide Cshappy
            hide Crugas
            show NPC3body
            show NPC3angry
            with dissolve

            NPC3 "Are you really sure?"

            hide NPC3body
            hide NPC3angry
            show Cecil2
            show Cshappy
            show Crugas
            with dissolve

            Cecil "Absolutely, I don't want you to miss the meeting because of me."

            hide Cecil2
            hide Cshappy
            hide Crugas
            show NPC3body
            show NPC3angry
            with dissolve

            NPC3 "If you insist…{p}Get some rest then."

            hide Cworry
            hide NPC3body
            hide NPC3angry
            with moveinright
            show Cecil2
            show Cworry2
            show Crugas
            with dissolve

            Cecil "Oh no..."
            Cecil "Right now, I don't have any power to protect my son from the villagers"
            Cecil "We need to go far away from here..."
            Cecil "We need to get ready before the villagers make any decisions!"
            "Cecil ran as fast as she could, {w}her body weakening, {w}all she could do was think about her baby."

            hide Crugas
            hide Cworry2
            show Cworry
            with dissolve

            "Despair consumed her..."
            "... So much so that she didn't notice when she cut her arm on a dry branch..."
            "... And left a trail of blood in her way."
            "She kept running because her son's life depended on it."

            hide village
            show forest_hut
            with fade
            hide Cecil2
            hide Cworry2

            "When she finally caught sight of the all-too-familiar cabin..."

            hide forest_hut
            hide Cworry
            hide farmerHouse
            with fade

            "... Her vision blurred."
            "The weak body and the loss of blood were too much for Cecil to take."

            scene effect
            with dissolve
            #pause

            "She then passed out."

            hide effect

            jump square

    label square:
    #small village square
    play music "audio/Sneaking in the night.mp3" fadein 1.0

    show village
    show Rudbody
    show Rudsup
    with fade

    Rud "I saw it with my own eyes!"
    Rud "The witch looked into my soul..."
    Rud "... She was holding a child covered in blood!"
    "The father hugged him, comforting him."

    hide Rudbody
    hide Rudsup
    show NPC2body
    show NPC2angryFace
    with dissolve

    NPC2 "Enough. It is enough."

    hide NPC2body
    hide NPC2angryFace
    with dissolve

    Crowd "We can't keep quiet about this!"
    Crowd "We must take action before something serious happens!"
    "A murmur started."
    "By now, they were all convinced that the woman was a bad witch and her child, the child of the devil."

    show NPC2body
    show NPC2angryFace
    with dissolve

    NPC2 "It is said that the witch leaves the magical shelter of the hut every night. We'll attack by surprise tonight."

    hide NPC2body
    hide NPC2angryFace
    with dissolve

    "The crowd roared in agreement."
    "The collective feeling encouraged them and everyone went to their home to prepare."

    hide Village
    show capital
    play music "audio/SHADOW.mp3" fadein 1.0
    with fade

    #Weastern Capital
    #play music

    "The king's Shadow special mark was the lack of substance,"
    "the light passed through, making her body hardly noticeable."
    "That was the main reason for being chosen by the king."

    show shadowBody
    show shadoweyes
    with dissolve

    Sha "Now that I have spent all my day gathering information I finally have found out where the meeting is going to be."
    Sha "It was really hard to find this location..."
    Sha "Luckly, I came earlier, so there's still plenty of time."
    "She then snuggled into the branches at the top of the tree, thinking about how to make this an unforgettable show for the capital."
    "Looking up at the already dark sky, she saw a shooting star passing by as the rebels appeared in the courtyard."

    hide shadoweyes
    show shadoweyes2

    Sha "That's it!"

    hide shadoweyes2
    show shadoweyes3

    "The king's Shadow began to cast a mighty spell, and heavy rain fell on the capital."
    "At lightning speed everyone was dead."

    hide shadowBody
    hide shadoweyes3
    hide village
    with dissolve
    stop music
    hide Cworry
    #forest hut
    hide capital
    play music "audio/HUT.mp3" fadein 1.0
    show effect
    with dissolve
    "Cecil opened her eyes, feeling the heavy rain on her body."

    

    icognito "Master!"

    hide effect
    show forest_hut
    with fade

    "She looked at whoever was beside her, it wasn't a person."

    show DBody
    show DSFace
    with dissolve
    pause

    hide DBody
    hide DSFace
    show Cecil2
    show Cworry
    with dissolve

    Cecil "Ditte, did you heal me? {w}Thanks."

    hide Cecil2
    hide Cworry
    show DBody
    show DSFace
    with dissolve

    Ditte "Master!"
    Ditte "We don't have time!{p}The humans are coming!"
    "That was enough to get Cecil to her feet."

    hide DBody
    hide DSFace
    show Cecil2
    show Cworry
    with dissolve

    Cecil "I don't have enough strength to run"
    Cecil "You also don't have enough strength to transport us three..."

    hide Cecil2
    hide Cworry
    with dissolve

    "The scarlet witch then used every last bit of magic to turn the nearest tree into a carriage."
    "But that costed her dearly."

    show Cecil2
    show Cworry
    with dissolve

    Cecil "Ditte, go get the horses, get us as far away as possible… {w}quickly!"

    hide Cecil2
    hide Cworry
    show DBody
    show DSFace
    with dissolve

    play sound "audio/447211__gamba-studio__buhos.wav"

    Ditte "Aye!"

    hide DBody
    hide DSFace
    with dissolve

    "Ditte then handed the baby to Cecil and did everything as told."
    "When the crowd could be heard on the horizon, they left."

    hide forest_hut
    show effect
    with fade
    play music "audio/The chase.mp3" fadein 1.0
    "The storm echoed, thunder filled the forest sky."
    "There, on a muddy road through the trees, was a carriage at frantic speed, threatening to overturn at every turn."

    hide effect
    show runAway
    show DBody
    show DSFace
    with dissolve

    Ditte "Faster! Faster!"

    hide DBody
    hide DSFace
    with dissolve

    "Inside the carriage, the baby was screaming, crying, frightened by the storm."
    "His mother was with him, but nothing she did soothes the baby, he felt his mother was equally terrified."
    "They were on the run."

    menu:
        "Turn left":
            #play music

            "But, what was destined to happen, happened."
            "A bolt of lightning streaked through the carriage, causing Ditte to lose consciousness."
            "Out of control then, the carriage fell off a cliff."
            "That marked the end of the Scarlet Witch."

            hide runAway
            return

        "Turn right":
            #play music

            "But, what was destined to happen, happened."
            "At a sharp bend, the carriage door flew open and both mother and child fell."
            "Her broken body, thrown to the side of the road."
            "She could only watch as the out-of-control carriage disappeared into the trees,"
            "as she tried to reach the image that was already disappearing from the horizon with a trembling hand."
            "She hugged the baby tighter, giving him her last vital energies"

            show CecilBaby
            show Cworry

            Cecil "Live, child, live..."

            hide CecilBaby
            hide Cworry
            show effect
            with fade
            play music "audio/SHADOW.mp3" fadein 1.0

            "The king's Shadow was ready to return and report the completed mission to the kingdom."
            
            hide effect
            show shadowBody
            show shadoweyes
            with dissolve

            Sha "The lightning show marking the royal coat of arms would no doubt leave a message of who is in power."
            Sha "I already made sure."
            Sha "There are no survivors."
            
            hide shadowBody
            hide shadoweyes
            with dissolve

            "The Shadow was ready to leave, {w}but a soft cry stopped it."
            "Then she saw, in the forest,{w} a child in his already lifeless mother's arms."
            "All wet from the storm she caused, bloodied with blood that wasn't his own."

            show shadowBody
            show shadoweyes
            with dissolve

            Sha "You are a warrior."
            "She whispered, {w}recognizing in that fragile creature's aura something as black as her own."
            Sha "From now on, you will be my successor."

            hide shadowBody
            hide shadoweyes
            with dissolve

            "The two left, leaving the lifeless broken body in the forest."

    # This ends the game.

    return
