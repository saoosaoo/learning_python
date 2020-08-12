import os

if not os.path.exists("행성"):
    os.mkdir("행성")

for i in range(1, 9):
    with open(f"행성\지구{i}.txt", 'w') as f:
        f.write(f"화성{i}이 되고 싶은 지구{i}입니다.")
