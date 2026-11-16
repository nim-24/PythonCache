bind - связывает событие с функцией  
entry.bind("<Return>", add_task)  
Читается так: «когда в поле entry нажали Enter, запусти функцию add_task».

squares = []
for x in range(10):
    squares.append(x**2)

squares

squares = list(map(lambda x: x**2, range(10)))

map() - некое хранилище/объект

list = [1,2,6,8,9,5,4]
print(set(list))
set() - множество   список преобразовали во множество
