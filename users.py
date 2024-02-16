import pandas as pd

class UserManager:
    def __init__(self):
        self.users_df = pd.DataFrame(columns=['id', 'name', 'email'])

    def insert_user(self, user_id, name, email):
        new_user = pd.DataFrame([[user_id, name, email]], columns=['id', 'name', 'email'])
        self.users_df = pd.concat([self.users_df, new_user], ignore_index=True)

    def get_user_by_id(self, user_id):
        user = self.users_df[self.users_df['id'] == user_id]
        return user if not user.empty else None

    def delete_user_by_id(self, user_id):
        self.users_df = self.users_df[self.users_df['id'] != user_id]

    def get_all_users(self):
        return self.users_df
    

def initDb():
    

    # Creazione di una lista di utenti di default
    default_users = [
        (1, 'Alice', 'alice@example.com'),
        (2, 'Bob', 'bob@example.com'),
        (3, 'Charlie', 'charlie@example.com')
    ]

    # Creazione di un gestore degli utenti e inserimento degli utenti di default
    user_manager = UserManager()
    for user_id, name, email in default_users:
        user_manager.insert_user(user_id, name, email)

    return user_manager

if __name__ == '__main__':
# Esempio di utilizzo dei metodi
    user_manager = UserManager()
    print("Lista di tutti gli utenti:")
    print(user_manager.get_all_users())

    print("\nUtente con ID 2:")
    user_2 = user_manager.get_user_by_id(2)
    if user_2 is not None:
        print(user_2)
    else:
        print("Nessun utente trovato con ID 2")

    print("\nEliminazione dell'utente con ID 1:")
    user_manager.delete_user_by_id(1)
    print(user_manager.get_all_users())
