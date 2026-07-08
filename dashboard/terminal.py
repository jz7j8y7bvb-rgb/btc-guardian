from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def show_dashboard(snapshot, indicators=None, analysis=None):

    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Bitcoin Guardian[/bold cyan]",
            subtitle="v1.1-alpha",
        )
    )

    prices = Table(show_header=False)

    prices.add_row("BTC/USD", f"${snapshot.btc_usd:,.2f}")
    prices.add_row("BTC/EUR", f"€{snapshot.btc_eur:,.2f}")

    console.print(prices)

    if indicators:

        table = Table(title="Technical Indicators")

        table.add_column("Indicator")
        table.add_column("Value")
        table.add_column("Signal")

        emoji = {
            "VERY_BULLISH": "🟢🟢",
            "BULLISH": "🟢",
            "NEUTRAL": "🟡",
            "BEARISH": "🟠",
            "VERY_BEARISH": "🔴",
        }

        for indicator in indicators:

            table.add_row(
                indicator.name,
                f"{indicator.value:.2f}",
                emoji[indicator.signal.name],
            )

        console.print(table)

    if analysis:

        recommendation_color = {
            "BUY": "green",
            "HOLD": "yellow",
            "REDUCE": "orange3",
            "DEFENSIVE": "red",
        }

        panel = Panel.fit(
            f"""
[bold]Guardian Score:[/bold] {analysis.score}/100

[bold]Recommendation:[/bold] [{recommendation_color[analysis.recommendation]}]{analysis.recommendation}[/{recommendation_color[analysis.recommendation]}]

[bold]Confidence:[/bold] {analysis.confidence}%
""",
            title="Guardian Analysis",
        )

        console.print(panel)

        console.print("[bold]Evidence[/bold]")

        for line in analysis.explanation:
            console.print(f" • {line}")