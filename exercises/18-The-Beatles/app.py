# Your code here!!
def sing():
    result = ""
    for i in range(11):
        if i == 4:
            result += "whisper words of wisdom, "
        elif i == 10:
            result += "there will be an answer, let it be"
        else:
            result += "let it be, "
    return result


print(sing())
