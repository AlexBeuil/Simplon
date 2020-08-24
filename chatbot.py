

import random

premiereQuestions = ["Comment allez-vous?","Pourquoi venez-vous me voir?",
                     "Comment s'est passé votre journée?"]
motCle = ["père","mère","copain","copine","maman","papa","ami","amie"]

deuxiemesQuestion = ["Comment va votre {0}?","La relation avec votre {0} "
                     "vous pose-t-elle problème?",
                     "Pourquoi pensez vous en ce moment a votre {0}?"]

reponseQuestionUser = ["Pourquoi me posez-vous cette question ?",
                       "Oseriez-vous posez cette question a un humain?",
                       "Je ne peux malheureusement pas répondre a cette question."]

reponseAffUser = ["J'entends bien","Je sens une pointe de regret",
                  "Est-ce une bonne nouvelle?","Oui c'est ça le problème",
                  "Pensez-vous ce que vous dites?","Hum ... Il se peut"]
print(random.choice(premiereQuestions))
reponse = input()
i = 0
while i != len(motCle):
    if reponse.find(motCle[i]) != -1 :
        print(random.choice(deuxiemesQuestion).format(motCle[i]))
        reponse = input()
        if reponse == "?":
            print(random.choice(reponseQuestionUser))
            break
        else:
            print(random.choice(reponseAffUser))
            break
    i+=1

