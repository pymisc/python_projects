""" this program demonstrate file handling """

# READONLY FILE

F1 = open('/tmp/file1', 'r', encoding="utf-8")

#print(F1.read())

print(F1.readline(), end="")
print(F1.readline(), end="")

# FILE WRITES (no printing on screen)
F2 = open('/tmp/file2', 'w', encoding="utf-8")
F2.write("Something I wanted to write\n")
F2.write("Something else I wanted to write\n")
F2.close()

# FILE READ (the one written in previous step)
F3 = open('/tmp/file2', 'r', encoding="utf=8")
print(F3.read())
