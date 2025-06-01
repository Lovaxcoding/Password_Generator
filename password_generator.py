import random
import string

def generate_password(length=12, include_digits=True, include_symbols=True):
    """
    Génère un mot de passe aléatoire avec des options personnalisables.

    Args:
        length (int): La longueur du mot de passe.
        include_digits (bool): Inclure des chiffres (0-9).
        include_symbols (bool): Inclure des symboles (!@#$%...).

    Returns:
        str: Le mot de passe généré.
    """
    characters = string.ascii_letters # Toujours inclure les lettres

    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters: # Au cas où toutes les options seraient désactivées
        raise ValueError("Au moins un type de caractère doit être sélectionné.")

    # Assure qu'au moins un caractère de chaque type sélectionné est présent
    password_list = []
    if include_digits:
        password_list.append(random.choice(string.digits))
    if include_symbols:
        password_list.append(random.choice(string.punctuation))
    password_list.append(random.choice(string.ascii_letters)) # Assurer au moins une lettre

    # Remplir le reste de la longueur avec des caractères aléatoires
    while len(password_list) < length:
        password_list.append(random.choice(characters))

    # Mélanger la liste pour randomiser l'ordre
    random.shuffle(password_list)

    return ''.join(password_list[:length]) # Prendre les 'length' premiers caractères après mélange

# Note : Nous enlevons la fonction main() ici car elle sera gérée par l'interface graphique.
# Si vous exécutez ce fichier directement, il ne fera rien, ce qui est normal.