def read_file(filename: str) -> list[str]:
	"""Read a text file one line at a time and return its lines."""
	lines = []
	with open(filename, "r", encoding="utf-8") as file:
		for line in file:
			lines.append(line.rstrip("\n"))
	return lines

nouns = read_file("nouns.txt")
print(nouns)

adjectives = read_file("adjectives.txt")
print(adjectives)
