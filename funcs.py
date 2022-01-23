def mirror(word, idx):
	if isinstance(word, str):
		if -len(word) <= idx < len(word):
			first_part = word[0:idx + 1]
			print(first_part)
			second_part = first_part[::-1]
			print(second_part)
			final_mirrored = first_part + second_part
			return final_mirrored
		else:
			raise IndexError
	else:
		raise TypeError
