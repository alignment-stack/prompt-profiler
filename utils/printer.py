from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def print_results(metrics):
    table = Table(title="Prompt Profiler Results", box=box.ROUNDED, show_lines=True)
    table.add_column("Metric", style="bold magenta")
    table.add_column("Value", style="bold cyan")
    for key, value in metrics.items():
        if key == 'words':
            continue  # Don't print full word list
        table.add_row(str(key), str(value))
    console.print(table)
