import string

dictionary = dict(list(zip(string.ascii_lowercase, string.ascii_lowercase[::-1])) + list(zip(string.ascii_uppercase, string.ascii_uppercase[::-1])) + list(zip(string.digits + string.punctuation, string.digits + string.punctuation)))

def cipher(dictin, instr):
	return ''.join([dictin[i] for i in instr])

print(cipher(dictionary, "foobar"))
print(cipher(dictionary, "/r/dailyprogrammer"))