history = []
is_running = True
while is_running:
    print('Привет! Я твой ИИ-Аналитик здоровья.')
    try:
        Weight = float(input('Введите ваш вес в килограммах:'))
    except ValueError:
         print("Некорректный ввод данных")
         continue
    print(Weight)
    if Weight <= 0:
        print('Некорректный ввод данных')
        continue
    try:
        Metters = float(input('Введите ваш рост в метрах (Пример: 1.75):'))
    except ValueError:
        print("Некорректный ввод данных")
        continue
    if Metters <= 0:
        print('Некорректный ввод данных.')
        continue
    imt = round(float(Weight) / float(Metters)**2, 3)
    history.append(imt)
    print('Ваш ИМТ:', imt)
    if imt < 18.5:
        print("У вас дефицит веса. Рекомендуется набор массы и профицит калорий.")
    elif imt <= 25:
        print('У вас идеальный вес! Поддерживайте форму')
    else:
        print('У вас избыточный вес. Рекомендуется похудение и дефицит калорий')
    user_choice = input('Хотите продолжить вычисления?: (Y/N)').upper()
    if user_choice == 'Y':
        is_running = True
    elif user_choice == 'N':
        is_running = False
        summa = sum(history) / len(history)
        print('Выход из программы.')
        print('---ИИ АНАЛИТИКА СОХРАНЕННЫХ ДАННЫХ---')
        print('Ваши сохраненные данные:', history)
        print('Всего проанализированно людей:', len(history))
        print('Средний ИМТ вашей группы:', summa)
        print('До свидания!')
