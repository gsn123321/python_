# import cowsay

# cowsay.cow('hello world')

# print(cowsay.char_names)

# cowsay.beavis('he he he he he')



# import art

# art.tprint('hello')



from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title='List')

table.add_column('Name', style='cyan')
table.add_column('Project', style='magenta')

table.add_row('Anton', 'Game')
table.add_row('NAstya', 'Chat-bot')

console.print(table)
