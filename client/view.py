from prompt_toolkit import prompt
from tabulate import tabulate

def display_books(books):
    print(tabulate([[b.id, b.title, b.author, b.available_copies] for b in books],
                   headers=["ID", "Title", "Author", "Available"]))

def get_user_input(prompt_text):
    return prompt(prompt_text)
