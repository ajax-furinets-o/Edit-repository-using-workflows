import re
import click

from pathlib import Path


@click.command()
@click.option("--epic-name")
def main(epic_name):
    file_path = Path().parent.absolute().joinpath("feature_file.feature")

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    modified_content = re.sub(r'@epic:\w+', f"@{epic_name}", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)


if __name__ == '__main__':
    main()
