import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)

print("한글".encode())
print("한글".encode().decode())

print(ord("한"),chr(ord("한")))