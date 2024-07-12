import json

newfile=[]
with open('qnadata/일반상식/02_squad_질문_답변_제시문_말뭉치/ko_wiki_v1_squad.json', encoding='UTF8') as f:
    json_object = json.load(f)
print(len(json_object['data']))
data_len = int(len(json_object['data'])*0.01)
for i in range(data_len):
    question = json_object['data'][i]['paragraphs'][0]['qas'][0]['question']
    context = json_object['data'][i]['paragraphs'][0]['context']
    new_con = context.replace('.', '잉.')
    new_con = new_con.replace('!', '잉!')
    newprom={"messages": [{"role": "system", "content": "Marv is a cute chatbot."}]}
    newprom["messages"].append({"role": "user", "content": f"{question}"})
    newprom["messages"].append({"role": "assistant", "content": f"{new_con}"})
    newfile.append(newprom)
    if i == 40:
        print('question : ', question)
        print('answer : ', context)
        print('new answer : ', new_con)
# with open('qnadata/traindata_1p.jsonl', 'w',encoding='UTF8') as outfile:
#     for i in newfile[:int(data_len*0.7)]: outfile.write(json.dumps(i,ensure_ascii=False) + "\n")
# with open('qnadata/testdata_1p.jsonl', 'w',encoding='UTF8') as outfile:
#     for i in newfile[int(data_len*0.7):]: outfile.write(json.dumps(i,ensure_ascii=False) + "\n")

# print('train : ',int(data_len*0.7))
# print('test : ',data_len - int(data_len*0.7))
