import boto3
import json
from botocore.exceptions import NoCredentialsError

class GestionSondage:
    def __init__(self):
        self.aws_access_key_id = 'AKIAWUBR7KZH34UZJA2F'
        self.aws_secret_access_key = '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'
        self.bucket_name = 'devoirpythonan'
        self.file_name_s3 = 'reponses_sondage.json'

    def save_to_aws(self):
        s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key)
        try:
            s3.upload_file(self.file_name_s3, self.bucket_name, self.file_name_s3)
            print("Données téléchargées avec succès sur S3.")
            return True
        except NoCredentialsError:
            print("Les identifiants AWS sont incorrects.")
            return False

    def savefichier(self, data, file_path):
        with open(file_path, 'a') as json_file:
            json.dump(data, json_file, indent=2)
            json_file.write('\n')

    def repondre_sondage(self):
        q1 = "Intentions de quitter le pays"
        q2 = "Tranche dage"
        q3 = "Niveau detudes"
        q4 = "Pays vise"
        q5 = "Raison du depart"
        q6 = "Objectif du depart"
        q7 = "Duree prevue à letranger"
        q8 = "Intention de retour dans le pays dorigine"

        r1 = ["Oui", "Non", "Incertain"]
        r2 = ["Moins de 20 ans", "20-24 ans", "25-29 ans", "30-34 ans", "35 ans et plus"]
        r3 = ["Licence 1", "Licence 2", "Licence 3", "Licence 4", "DUT 1", "DUT 2"]
        r4 = ["Etats-Unis", "Canada", "Royaume-Uni", "Australie", "France", "Autre"]
        r5 = ["Opportunites professionnelles", "Recherche academique", "Qualite de vie", "Autre"]
        r6 = ["Etudes supplementaires", "Raisons professionnelles", "Raisons personnelles"]
        r7 = ["Moins d'un an", "1-2 ans", "3-5 ans", "Plus de 5 ans"]
        r8 = ["Oui", "Non", "Incertain"]

        questions = [q1, q2, q3, q4, q5, q6, q7, q8]
        reponses = [r1, r2, r3, r4, r5, r6, r7, r8]

        reponse_etudiant = {}
        nom = input("Entrer votre nom: ")
        reponse_etudiant = {"Nom": nom}
        for i in range(len(questions)):
            print(f"Question {i + 1}: {questions[i]}")
            if isinstance(reponses[i], list):
                for j in range(len(reponses[i])):
                    print(f"    {j + 1}. {reponses[i][j]}")
            else:
                print(f"    {reponses[i]}")

            reponse = input(f"Choisissez la lettre de votre reponse: ")
            reponse = int(reponse)

            while reponse > len(reponses[i]):
                reponse = input("La reponse choisie n'est pas convenable: ")
                reponse = int(reponse)

            r = reponses[i][reponse - 1]
            reponse_etudiant[questions[i]] = r
        self.savefichier(reponse_etudiant, "reponses_sondage.json")
        self.save_to_aws()


