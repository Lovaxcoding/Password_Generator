import customtkinter as ctk
from password_generator import generate_password # Importe votre fonction du fichier précédent

class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Générateur de Mot de Passe Sécurisé")
        self.geometry("500x550") # Augmenter légèrement la taille pour plus d'espace
        self.resizable(False, False) # Empêche le redimensionnement

        # --- Configuration du thème global ---
        # Essayez différents thèmes et couleurs pour voir ce qui vous plaît le plus
        ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
        ctk.set_default_color_theme("blue") # "blue", "green", "dark-blue", "sweet-red" (personnalisé)

        # --- Configuration de la grille principale pour un meilleur espacement ---
        self.grid_columnconfigure(0, weight=1) # Permet à la colonne de s'étendre
        # Ajustez les poids des lignes pour donner plus d'espace aux sections importantes
        self.grid_rowconfigure(0, weight=2)   # Pour le titre
        self.grid_rowconfigure((1, 2, 3, 4), weight=1) # Pour les options et le slider
        self.grid_rowconfigure(5, weight=2)   # Pour le bouton Générer
        self.grid_rowconfigure(6, weight=2)   # Pour le champ du mot de passe
        self.grid_rowconfigure(7, weight=1)   # Pour le bouton Copier
        self.grid_rowconfigure(8, weight=0)   # Pour le message (pas besoin de beaucoup d'espace)


        # --- Widgets de l'interface ---

        # Titre (plus grand, plus audacieux)
        self.title_label = ctk.CTkLabel(self,
                                        text="🔒 Générateur de Mot de Passe",
                                        font=ctk.CTkFont(family="Arial", size=30, weight="bold"))
        self.title_label.grid(row=0, column=0, pady=30, padx=20, sticky="nsew") # Centré avec padding


        # --- Section Longueur du mot de passe ---
        # Utilisation d'un cadre (frame) pour grouper visuellement les éléments de longueur
        self.length_frame = ctk.CTkFrame(self)
        self.length_frame.grid(row=1, column=0, pady=10, padx=40, sticky="ew") # Placer le cadre

        self.length_frame.grid_columnconfigure(0, weight=1)
        self.length_frame.grid_columnconfigure(1, weight=3) # Plus d'espace pour le slider
        self.length_frame.grid_columnconfigure(2, weight=1) # Pour l'affichage numérique

        self.length_label = ctk.CTkLabel(self.length_frame,
                                         text="Longueur :",
                                         font=ctk.CTkFont(size=15))
        self.length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.length_slider = ctk.CTkSlider(self.length_frame,
                                           from_=4, to=32, number_of_steps=28,
                                           command=self.update_length_label)
        self.length_slider.set(12) # Valeur par défaut
        self.length_slider.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.length_value_label = ctk.CTkLabel(self.length_frame,
                                                text="12",
                                                font=ctk.CTkFont(size=15, weight="bold"))
        self.length_value_label.grid(row=0, column=2, padx=10, pady=5, sticky="e")


        # --- Section Options de caractères ---
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.grid(row=2, column=0, pady=10, padx=40, sticky="ew") # Placer le cadre

        self.options_frame.grid_columnconfigure(0, weight=1) # Une seule colonne pour les checkboxes

        self.digits_checkbox = ctk.CTkCheckBox(self.options_frame,
                                               text="Inclure des chiffres (0-9)",
                                               font=ctk.CTkFont(size=14))
        self.digits_checkbox.select() # Sélectionné par défaut
        self.digits_checkbox.grid(row=0, column=0, pady=5, padx=20, sticky="w") # Espacement interne au cadre

        self.symbols_checkbox = ctk.CTkCheckBox(self.options_frame,
                                                text="Inclure des symboles (!@#$...)",
                                                font=ctk.CTkFont(size=14))
        self.symbols_checkbox.select() # Sélectionné par défaut
        self.symbols_checkbox.grid(row=1, column=0, pady=5, padx=20, sticky="w")


        # --- Bouton Générer ---
        self.generate_button = ctk.CTkButton(self,
                                             text="Générer Mot de Passe",
                                             command=self.generate_and_display_password,
                                             font=ctk.CTkFont(size=18, weight="bold"),
                                             height=45, # Hauteur légèrement augmentée
                                             corner_radius=10) # Bords arrondis
        self.generate_button.grid(row=3, column=0, pady=25, padx=40, sticky="ew")


        # --- Affichage du mot de passe ---
        self.password_entry = ctk.CTkEntry(self,
                                           width=350, # Largeur augmentée
                                           height=40, # Hauteur augmentée
                                           justify="center",
                                           font=ctk.CTkFont(size=18, weight="bold"),
                                           placeholder_text="Votre mot de passe apparaîtra ici...", # Texte indicatif
                                           fg_color=("white", "gray20")) # Couleur de fond cohérente avec le thème
        self.password_entry.grid(row=4, column=0, pady=10, padx=40, sticky="ew")


        # --- Bouton Copier ---
        self.copy_button = ctk.CTkButton(self,
                                         text="Copier",
                                         command=self.copy_password,
                                         font=ctk.CTkFont(size=16),
                                         fg_color="gray", # Couleur de fond différente
                                         hover_color="darkgray", # Couleur au survol
                                         corner_radius=10)
        self.copy_button.grid(row=5, column=0, pady=10, padx=40, sticky="ew")


        # --- Message d'erreur/succès ---
        self.message_label = ctk.CTkLabel(self, text="", text_color="red", font=ctk.CTkFont(size=13))
        self.message_label.grid(row=6, column=0, pady=5)


    # --- Fonctions des Callbacks (inchangées) ---

    def update_length_label(self, value):
        """Met à jour l'affichage de la longueur du mot de passe."""
        self.length_value_label.configure(text=f"{int(value)}")

    def generate_and_display_password(self):
        """Génère un mot de passe et l'affiche dans le champ."""
        try:
            length = int(self.length_slider.get())
            include_digits = bool(self.digits_checkbox.get())
            include_symbols = bool(self.symbols_checkbox.get())

            password = generate_password(length, include_digits, include_symbols)
            self.password_entry.delete(0, ctk.END) # Efface l'ancien mot de passe
            self.password_entry.insert(0, password) # Insère le nouveau
            self.message_label.configure(text="Mot de passe généré !", text_color="green")
        except ValueError as e:
            self.message_label.configure(text=f"Erreur : {e}", text_color="red")
        except Exception as e:
            self.message_label.configure(text=f"Une erreur inattendue est survenue: {e}", text_color="red")


    def copy_password(self):
        """Copie le mot de passe affiché dans le presse-papiers."""
        password_to_copy = self.password_entry.get()
        if password_to_copy:
            self.clipboard_clear() # Efface le presse-papiers
            self.clipboard_append(password_to_copy) # Ajoute le mot de passe
            self.message_label.configure(text="Mot de passe copié !", text_color="blue")
        else:
            self.message_label.configure(text="Aucun mot de passe à copier.", text_color="red")

# --- Lancement de l'application ---
if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()