def read_data():
    inputPath = "input.txt"
    inputTextFile = open(inputPath, "r")
    inputText = inputTextFile.read()
    text_split = inputText.split()

    inputTextFile.close()
    return text_split

input_list = read_data()
save_dict = {}
top5Dict = []

for i in range(len(input_list) // 4):
    if input_list[i * 4 + 1] in save_dict:
        save_dict[input_list[i * 4 + 1]] += 1
    else:
        save_dict[input_list[i * 4 + 1]] = 1

print("요청된 Object의 수 -", len(save_dict))

# print(save_dict)
top5Dict.append(input_list[0 * 4 + 1]) # 일단 [1]의 값을 최대 호출로

for i in save_dict:
    for j in range(len(top5Dict)):
        if j >= 5: #상위 5개 넘어가면 나가버리게
            break
        if save_dict[i] > save_dict[top5Dict[j]]:
            top5Dict.insert(j, i)
            break
print()

print("가장 많이 요청된 Object ID와, 요청 횟수")
print("Object ID -", top5Dict[0])
print("요청 횟수  -", save_dict[top5Dict[0]])

print()
print("상위 5개의 요청에 대한 Object ID와 각각의 요청 횟수 ")
print("---------------------")
print("Object ID | 요청 횟수")
print("---------------------")
for i in range(5):
    # print(top5Dict[i],"|",save_dict[top5Dict[i]])
    print("%-9s | %d" % (str(top5Dict[i]), save_dict[top5Dict[i]]))




