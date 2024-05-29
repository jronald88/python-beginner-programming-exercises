# ✅↓ Write your code here ↓✅
def sing():
    chorus = ""
    for i in range(11):
        if i == 4:
            chorus += "there will be an answer,\n"
        elif i == 10:
            chorus += "whisper words of wisdom, let it be"
        else:
            chorus += "let it be,\n"
    return(chorus)

sing()
