import click
from .generator import gen_usernames
from pathlib import Path

@click.command()
@click.option("-f", "--first", required=True, help="First Value")
@click.option("-s", "--second", required=True, help="Second Value")
@click.option("-o", "--output", type=click.Path(), help="Save output to a file")
@click.option("-v", "--verbose", is_flag=True, help="Verbose output")
def main(first, second, output, verbose):
    banner_path = Path(__file__)/"banner.txt" #
    if banner_path.exists():
        print(banner_path.read_text())
    
    usernames = gen_usernames(first, second)

    if verbose:
        click.echo(click.style(f"[*] Generating usernames for: {first} {second}", fg="blue"))
    
    for username in usernames:
        click.echo(click.style(username))
    
    if output:
        with open(output, "w") as f:
            f.write("\n".join(usernames))
        click.echo(click.style(f"[!] Successfully saved {len(usernames)} usernames to {output}.", fg="green"))