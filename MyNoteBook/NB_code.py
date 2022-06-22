import pandas as pd
def append_work(data): #принимать данные через data
    works = input("Введите запланированные дела через запятую: ").split(',')
    csv_file = pd.read_csv('note.csv')
    data['Dela'] = works
    data['Status'] = ["Не выполнено"] * len(works)
    tmp = input("Введите время через запятую: ").split(',')
    data['Time'] = tmp

    df = pd.concat([csv_file, pd.DataFrame(data)], ignore_index = False)
    df.to_csv('note.csv', index=None)
    print(df)

data = {'Dela': [], "Status": [], "Time":[]}
append_work(data)
while True: #endless cycle
    what = input("1 - add time, 2 - change status, 3 stop cycle")
    if what == "1":
        append_work(data)
    elif what == "2":
        sts = input("Вввести индекс и статус дела через пробел: ").split(',')
        csv_file = pd.read_csv("note.csv")
        df = pd.concat([csv_file, pd.DataFrame(data)], ignore_index=False)
        status = list(df['Status'])
        status[int(sts[0])] = sts[1]
        #статус с каким-то индексом будет равен статусу что ввел пользователь
        df["Status"] = status

        pd.DataFrame(df).to_csv("note.csv", index=None)
        print(pd.DataFrame(df))
    elif what == '3':
        break #завершаем цикл


