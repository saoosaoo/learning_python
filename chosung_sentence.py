

# print(hgtk.letter.decompose('감'))

# print(hgtk.text.decompose('학교종이 땡땡땡! hello world 1234567890 ㅋㅋ!'))

#sentence를 분해한뒤 ᴥ를 기준으로 split, 각각의 덩어리 중 [0]을 인덱스로 뽑아내어 프린트
import hgtk


def sen_to_cho(sentence):
    chosung_sentence = ""
    a = hgtk.text.decompose(sentence)
    for i in range(len(a.split('ᴥ')) - 1):
        chosung_sentence = chosung_sentence + a.split('ᴥ')[i][0]
    return chosung_sentence

print(sen_to_cho('안녕하세요'))

# a = hgtk.text.decompose('안녕하슈')
# for i in range(len(a.split('ᴥ')) - 1):
#     print(a.split('ᴥ')[i][0])


# n = len(a.split('ᴥ')) - 2
# print(a.split('ᴥ')[0][0])
# print(a.split('ᴥ')[n][0])

