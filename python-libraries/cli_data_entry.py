from rich.console import Console
from rich.table import Table
import json
import os


console = Console()


def display_example_recipe():
    table = Table(title="Recipe Example: Spaghetti Carbonara")

    table.add_column("Ingredient", justify="left", style="cyan", no_wrap=True)
    table.add_column("Amount", justify="center", style="magenta")

    table.add_row("Spaghetti", "200g")
    table.add_row("Pancetta", "100g")
    table.add_row("Egg yolks", "2")
    table.add_row("Parmesan", "50g")
    table.add_row("Black Pepper", "to taste")

    console.print(table)


def get_user_input():
    recipe_name = console.input("[cyan]Enter the recipe name: [/cyan]")
    ingredients = console.input("[magenta]Enter the ingredients (comma-separated): [/magenta]")
    cooking_time = console.input("[green]Enter the cooking time (in minutes): [/green]")
    serving_size = console.input("[yellow]Enter the serving size: [/yellow]")
    instructions = console.input("[bold]Enter the cooking instructions: [/bold]")

    ingredient_list = [ingredient.strip() for ingredient in ingredients.split(",")]

    return {
        "Recipe Name": recipe_name,
        "Ingredients": ingredient_list,
        "Cooking Time": cooking_time,
        "Serving Size": serving_size,
        "Instructions": instructions
    }

ingredients_books = []
while True:
    ingredients_book = get_user_input()
    
    console.print(f'Recipe Name:{ingredients_book['Recipe Name']}')
    console.print(f'Ingredients:{ingredients_book['Ingredients']}')
    console.print(f'Cooking Time:{ingredients_book['Cooking Time']}')
    console.print(f'Serving Size:{ingredients_book['Serving Size']}')
    console.print(f'Instructions:{ingredients_book['Instructions']}')
    confirmation = console.input(("Is this data correct? (yes/no): ").strip().lower())
    if confirmation == 'yes':
        ingredients_books.append(ingredients_book)
        break
    else:
        console.print("You will have to enter your data again. ")
  
   


file_path = os.path.join(os.getcwd(), 'ingredients.json')
with open(file_path, 'w') as file:
    json.dump(ingredients_books, file)
console.print(f'\n[bold green] Stores in {file_path}[/bold green]')


