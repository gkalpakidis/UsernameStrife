def gen_usernames(first, second):
    first = first.lower()
    second = second.lower()
    combinations = set()

    initials = first[0]
    combos = [
        f"{initials}{second}",
        f"{initials}.{second}",
        f"{first}.{second}",
        f"{first}{second}",
        f"{second}{first}",
        f"{second}.{first}",
        f"{second}{initials}",
        f"{second}.{initials}",
        f"{initials}{second[0]}",
        f"{first}_{second}",
        f"{first}-{second}",
        f"{second}_{first}",
    ]

    combinations.update(combos)
    return sorted(combinations)