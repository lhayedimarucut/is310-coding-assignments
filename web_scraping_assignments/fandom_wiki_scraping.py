import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

console = Console()

def get_character_relations(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    relations = []

    relations_section = soup.find('span', id='Relations')
    if relations_section:
        relations_content = relations_section.find_parent('h2').find_next_sibling()
        while relations_content and relations_content.name != 'h2':
            if relations_content.name in ['ul', 'ol']:
                for relation_item in relations_content.find_all('li'):
                    
                    relation_text = relation_item.get_text()
                    if ' - ' in relation_text:
                        
                        relation_name, relation_description = relation_text.split(' - ', 1)
                    elif ':' in relation_text:
                        
                        relation_name, relation_description = relation_text.split(':', 1)
                    else:
                        relation_name = relation_text.strip() 
                        relation_description = "No description available"

                    relations.append({
                        "name": relation_name.strip(),
                        "description": relation_description.strip()
                    })

            relations_content = relations_content.find_next_sibling()

    return relations

def display_character_relations(url, character_name):
    console.print(f"Processing relations for {character_name}...")


    relations = get_character_relations(url)

    relations_table = Table(title=f"{character_name} - Relations")
    relations_table.add_column("Relation Name", style="cyan")
    relations_table.add_column("Description", style="magenta")

    if relations: 
        for relation in relations:
            relations_table.add_row(relation['name'], relation['description'])
    else:
        relations_table.add_row("No relations found", "")

    console.print(relations_table)

character_url = "https://strawberryshortcakeberrybitty.fandom.com/wiki/Strawberry_Shortcake"
character_name = "Strawberry Shortcake"

display_character_relations(character_url, character_name)

