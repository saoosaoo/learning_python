greeting = "hello world"
code = {"h": "i", "e": "m"}

암호 = ""
for i in greeting:
    암호 = 암호 + code[i]

print(암호)

원래말 = ""
decode = [v: k for k, v in code.items()]
for i in 암호:
    원래말 = 원래말 + decode[i]

print(원래말)