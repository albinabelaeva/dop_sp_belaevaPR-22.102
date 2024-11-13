def fun(q1,q2,a):
    listt = [(a[i], i) for i in range(q1)]  # Создаем список кортежей (значение, индекс)
    listt.sort()  # Сортируем по первому элементу (значению)
    cislo = listt[:q2]  # Берем первые q2 элементов
    # summ = sum(value for value, index in cislo)  
    for b in range(q2-1):
        a.append(cislo[b][1])
        # a=cislo[b][1]
    print("s", max(a)+1)
    
a = input("введите количество пробирок в магазине и количество пробирок, которое нужно купить, соответственно: ").split(" ")
q1, q2 = map(int, a)

a = input("введите стоимость каждой пробирки: ").split(" ")
a = list(map(int, a))

fun(q1,q2,a)






        






