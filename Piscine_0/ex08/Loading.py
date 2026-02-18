import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)

    for i, elem in enumerate(lst, 1):
        percent = i / total
        width = os.get_terminal_size().columns
        bar_size = width - 30
        if bar_size < 10:
            bar_size = 10

        filled = int(bar_size * percent)
        bar = "=" * filled + ">" + " " * (bar_size - filled - 1)

        print(
            f"\r{int(percent*100)}%|[{bar}]| {i}/{total}",
            end="",
            flush=True
        )

        yield elem

    print()
