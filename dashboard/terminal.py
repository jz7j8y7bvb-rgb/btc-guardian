from rich.console import Console
from rich.table import Table

console = Console()


def show_dashboard(snapshot):

    table = Table(title="Bitcoin Guardian")

    table.add_column("Currency", style="cyan")

    table.add_column("Price", justify="right")

    table.add_row("BTC / USD", f"${snapshot.btc_usd:,.2f}")

    table.add_row("BTC / EUR", f"€{snapshot.btc_eur:,.2f}")

    console.print(table)