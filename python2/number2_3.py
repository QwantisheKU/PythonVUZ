def f23(table):
    pred = [[f"{elem[2].split()[0]}", elem[3][2:], 'N' if elem[4].split()[0] == 'Не' else 'Y', elem[6].replace('@', '[at]')] for elem in table]
    final = []
    for elem in pred:
        if elem not in final:
            final.append(elem)
    final = list(map(list, zip(*final)))
    return final

# just1 = f23([
#     [None, None, 'Бизебянц М.Д.', '2004/04/10', 'Не выполнено', '2004/04/10', 'bizebanz4@gmail.com'],
#     [None, None, 'Фулли А.А.', '2001/10/20', 'Не выполнено', '2001/10/20', 'fulli41@mail.ru'],
#     [None, None, 'Лефий И.Ч.', '2000/09/17', 'Не выполнено', '2000/09/17', 'lefij98@mail.ru'],
#     [None, None, 'Тинезян С.Т.', '2001/01/14', 'Выполнено', '2001/01/14', 'tinezan11@yahoo.com'],
# ])
# just2 = f23([
#     [None, None, 'Ферев И.Б.', '2000/01/11', 'Не выполнено', '2000/01/11', 'ferev1@yahoo.com'],
#     [None, None, 'Барак Д.И.', '2002/08/07', 'Не выполнено', '2002/08/07', 'barak10@yahoo.com'],
#     [None, None, 'Цатобли П.Е.', '2003/03/09', 'Не выполнено', '2003/03/09', 'zatobli51@rambler.ru'],
# ])
# print(just1)
# print(just2)