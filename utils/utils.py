
def get_lines(file_path: str):

    lines = []
    with open(file_path) as file:
        # Traitement du fichier
        for line in file.readlines():
            lines.append(line.replace("\n", ""))

    return lines