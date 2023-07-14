data = []
with open('./data/test.bin', 'wb') as file:
    file.write("안녕하세요".encode())
with open('./data/test.bin', 'rb') as file:
    s = file.read()
    print(s.decode())