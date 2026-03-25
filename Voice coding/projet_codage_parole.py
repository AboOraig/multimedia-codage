# Import des modules nécessaires
import tkinter as tk  # Import de la bibliothèque Tkinter pour l'interface graphique
from tkinter import filedialog  # Import de filedialog pour la boîte de dialogue de sélection de fichier
import speech_recognition as sr  # Import de speech_recognition pour la reconnaissance vocale
from PIL import Image, ImageTk  # Import de Image et ImageTk depuis PIL pour la manipulation des images


def reconnaître_et_count_audio(chemin_fichier, mot_cible):
    # Créer un objet Recognizer
    recognizer = sr.Recognizer()
    '''
    record(source) : Cette méthode permet de lire l'audio à partir
    d'une source spécifiée et de le stocker pour une utilisation ultérieure
    dans la reconnaissance vocale.
    '''
    # Charger le fichier audio
    with sr.AudioFile(chemin_fichier) as source:
        # Lire l'audio du fichier
        audio_data = recognizer.record(source)
    '''
    recognize_google(audio_data, language) : Cette méthode utilise le service
    Google Speech Recognition pour transcrire l'audio en texte.
    On peux spécifier la langue de l'audio à l'aide du paramètre language.
    '''
    try:
        # Utiliser Google Speech Recognition pour transcrire l'audio en texte
        text = recognizer.recognize_google(audio_data, language='fr-FR')
        # Compter le nombre d'occurrences du mot cible dans le texte transcrit
        count = text.lower().count(mot_cible.lower())
        # Mettre à jour l'étiquette de résultat avec le nombre d'occurrences
        result_label.config(text="Le mot '{}' est prononcé {} fois dans le fichier audio.".format(mot_cible, count))
    except sr.UnknownValueError:
        # Si la reconnaissance vocale échoue à reconnaître l'audio
        # Mettre à jour l'étiquette de résultat avec un message d'erreur
        result_label.config(text="Impossible de reconnaître l'audio.")
    except sr.RequestError as e:
        # Si une erreur se produit lors de la demande au service Google Speech Recognition
        # Mettre à jour l'étiquette de résultat avec un message d'erreur détaillé
        result_label.config(text="Erreur lors de la demande au service Google Speech Recognition ; {0}".format(e))

def choisir_fichier_audio():
    # Ouvrir une boîte de dialogue pour sélectionner un fichier audio au format WAV
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers audio", "*.wav")])
    # Supprimer le texte actuel de l'entrée de fichier audio
    audio_file_entry.delete(0, tk.END)
    # Insérer le chemin du fichier sélectionné dans l'entrée de fichier audio
    audio_file_entry.insert(0, file_path)

def nombre_mot():
    # Obtenir le chemin du fichier audio à partir de l'entrée de fichier audio
    audio_file_path = audio_file_entry.get()
    # Obtenir le mot cible à partir de l'entrée de mot
    target_word = word_entry.get()
    # Vérifier si le chemin du fichier audio et le mot cible sont spécifiés
    if audio_file_path and target_word:
    # Si oui, appeler la fonction reconnaître_et_count_audio pour transcrire l'audio et compter le mot cible
        reconnaître_et_count_audio(audio_file_path, target_word)
    # Si l'un des champs est vide, afficher un message d'erreur
    else:
        result_label.config(text="Veuillez sélectionner un fichier audio et entrer un mot.")

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Reconnaissance Vocale")
root.geometry("560x400")
root.config(bg='#dcdcdc')  



tk.Label(root, text="Réalisé par:\nMohammed ABO ORAIG", fg="black", bg='#dcdcdc', font=("Times", 10)).place(relx = 0.3, rely = 0.8, anchor = 'center')
# Étiquette pour l'année
tk.Label(root, text="2023-2024", fg="black", bg='#dcdcdc', font=("Times", 8)).pack(side = 'bottom')


# Frame pour choisir le fichier audio
file_frame = tk.Frame(root)
file_frame.pack(pady=10)

audio_file_label = tk.Label(file_frame, text="Choisir un fichier audio:")
audio_file_label.grid(row=0, column=0)

# Entrée pour afficher le chemin du fichier audio sélectionné
audio_file_entry = tk.Entry(file_frame, width=50)
audio_file_entry.grid(row=0, column=1)

# Bouton pour parcourir et choisir un fichier audio
browse_button = tk.Button(file_frame, text="Parcourir", command=choisir_fichier_audio)
browse_button.grid(row=0, column=2)

# Frame pour entrer le mot recherché
word_frame = tk.Frame(root)
word_frame.pack(pady=10)

word_label = tk.Label(word_frame, text="Mot recherché:")
word_label.grid(row=0, column=0)

# Entrée pour saisir le mot recherché
word_entry = tk.Entry(word_frame, width=30)
word_entry.grid(row=0, column=1)

# Bouton pour compter le nombre d'occurrences du mot
count_button = tk.Button(root, text="Compter", command=nombre_mot)
count_button.pack(pady=10)

# Frame pour afficher le résultat
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

# Étiquette pour afficher le résultat (nombre d'occurrences du mot)
result_label = tk.Label(result_frame, text="")
result_label.pack()

# Lancer la boucle principale Tkinter
root.mainloop()
