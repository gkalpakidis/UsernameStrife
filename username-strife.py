#!/usr/bin/env python3

import click

BANNER = r"""
███    █▄  ███▄▄▄▄      ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████     ███        ▄████████  ▄█     ▄████████    ▄████████ 
███    ███ ███▀▀▀██▄   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ ▀█████████▄   ███    ███ ███    ███    ███   ███    ███ 
███    ███ ███   ███   ███    ███ ███   ███   ███   ███    █▀    ███    █▀     ▀███▀▀██   ███    ███ ███▌   ███    █▀    ███    █▀  
███    ███ ███   ███   ███    ███ ███   ███   ███  ▄███▄▄▄       ███            ███   ▀  ▄███▄▄▄▄██▀ ███▌  ▄███▄▄▄      ▄███▄▄▄     
███    ███ ███   ███ ▀███████████ ███   ███   ███ ▀▀███▀▀▀     ▀███████████     ███     ▀▀███▀▀▀▀▀   ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀     
███    ███ ███   ███   ███    ███ ███   ███   ███   ███    █▄           ███     ███     ▀███████████ ███    ███          ███    █▄  
███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███    ▄█    ███     ███       ███    ███ ███    ███          ███    ███ 
████████▀   ▀█   █▀    ███    █▀   ▀█   ███   █▀    ██████████  ▄████████▀     ▄████▀     ███    ███ █▀     ███          ██████████ 
                                                                                          ███    ███                                v0.1

Username-Strife (Python Edition)
"""

def gen_username(first, second):
    first = first.lower()
    second = second.lower()
    f = first[0]
    s = second[0]

    combos = {
        f"{f}{second}",
        f"{f}.{second}",
        f"{first}.{second}",
        f"{first}{second}",
        f"{second}{f}",
        f"{second}.{f}",
        f"{second}{first}",
        f"{second}.{first}",
        f"{f}{s}",
        f"{first}_{second}",
        f"{first}-{second}",
        f"{second}_{first}",
        f"{first}{s}",
        f"{f}{second}{s}",
    }
    return sorted(combos)

@click.command()
@click.option("-f", "--first", required=True, help="First value.")
@click.option("-s", "--second", required=True, help="Second value.")
@click.option("-o", "--output", type=click.Path(), help="Output file.")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose output.")
def main(first, second, output, verbose):
    click.echo(click.style(BANNER, fg="red"))

    if verbose:
        click.echo(click.style(f"[*] Generating usernames for: {first} {second}", fg="blue"))
        click.echo()
    
    usernames = gen_username(first, second)

    for u in usernames:
        click.echo(click.style(u, fg="green"))
    
    if output:
        try:
            with open(output, "w") as f:
                f.write("\n".join(usernames))
            click.echo()
            click.echo(click.style(f"[!] Successfully saved to {output}", fg="green"))
        except Exception as e:
            click.echo(click.style(f"[!] Failed to write to file: {e}", fg="red"))

if __name__ == "__main__":
    main()