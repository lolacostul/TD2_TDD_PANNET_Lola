def mirror(word, idx):
	if isinstance(word, str) and isinstance(idx, int):
		if -len(word) <= idx < len(word):
			if 0 <= idx < len(word):
				first_part = word[:idx + 1]
			elif -len(word) <= idx < 0:
				first_part = word[idx:]
			second_part = first_part[::-1]
			final_mirrored = first_part + second_part
			return final_mirrored
		else:
			raise IndexError
	else:
		raise TypeError
