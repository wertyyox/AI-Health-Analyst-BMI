import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

history = []

def calculate_imt_gui():
    try:
        Weight = weight_entry.get()
        Metters = meters_entry.get()
        
        imt = round(float(Weight) / float(Metters)**2, 3)
        history.append(imt)
        
        if imt < 18.5:
            verdict = "У вас дефицит веса. Рекомендуется набор массы и профицит калорий."
        elif 18.5 <= imt <= 24.9:
            verdict = "У вас идеальный вес! Поддерживайте форму"
        elif imt >= 25:
            verdict = "У вас избыточный вес. Рекомендуется похудение и дефицит калорий"
            
        summa = round(sum(history) / len(history), 2)
        
        result_label.configure(
            text=f"Ваш ИМТ: {imt}\n\nВердикт:\n{verdict}"
        )
        
        analytics_label.configure(
            text=f"Ваши сохраненные данные: {history}\n"
                 f"Всего проанализировано людей: {len(history)}\n"
                 f"Средний ИМТ вашей группы: {summa}"
        )
        
    except ValueError:
        result_label.configure(text="Ошибка: Введите корректные числа!")
app = ctk.CTk()
app.title("ИИ-Аналитик здоровья")
app.geometry("450x550")
title_label = ctk.CTkLabel(app, text="ИИ-Аналитик здоровья", font=("Arial", 20, "bold"))
title_label.pack(pady=20)
weight_entry = ctk.CTkEntry(app, placeholder_text="Введите ваш вес в килограммах:")
weight_entry.pack(pady=10, fill="x", padx=40)
meters_entry = ctk.CTkEntry(app, placeholder_text="Введите ваш рост в метрах (например, 1.75):")
meters_entry.pack(pady=10, fill="x", padx=40)
calc_button = ctk.CTkButton(app, text="Рассчитать", command=calculate_imt_gui, font=("Arial", 14, "bold"))
calc_button.pack(pady=20)
result_label = ctk.CTkLabel(app, text="Результат отобразится здесь", font=("Arial", 13), text_color="#A0A0A0")
result_label.pack(pady=10)
divider = ctk.CTkLabel(app, text="----------------------------------------------------------", text_color="gray")
divider.pack(pady=15)
analytics_title = ctk.CTkLabel(app, text="--- ИИ АНАЛИТИКА СОХРАНЕННЫХ ДАННЫХ ---", font=("Arial", 12, "bold"), text_color="#3B8ED0")
analytics_title.pack()
analytics_label = ctk.CTkLabel(app, text="История пуста. Введите данные первого человека.", font=("Arial", 12), text_color="gray")
analytics_label.pack(pady=10)
app.mainloop()