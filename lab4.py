import numpy as np
import pandas as pd


class ExpertGroup:
    def __init__(self, objects):
        self.objects = objects

    def generate_table_2_4(self, total_scores, average_scores, max_scores):
        # Створення таблиці з результатами розрахунків з пункту 2.4

        table_data = {
            "Сумарне значення оцінки (вираз 1.1)": total_scores,
            "Середнє значення оцінки (вираз 1.2)": average_scores,
            "Нормативне значення оцінки (вираз 1.3)": max_scores
        }

        table = pd.DataFrame(table_data, index=self.objects[:len(total_scores)])
        print("Таблиця 1.1:")
        print(table)

    def calculate_consistency(self, evaluations):
        # Розрахунок узгодженості результатів з пункту 2.5

        # Варіація показників
        variations = np.var(list(evaluations.values()))

        # Середнє значення оцінки кожного об'єкта
        mean_scores = np.mean(list(evaluations.values()))

        # Дисперсія
        variance = np.var(list(evaluations.values()))

        # Середнє квадратичне відхилення
        std_deviation = np.std(list(evaluations.values()))

        # Коефіцієнт варіації
        coefficient_of_variation = std_deviation / mean_scores

        # Належність кожної кількісної оцінки об'єктів до довірчого інтервалу

        print("Таблиця 3:")
        print(f"Варіація показників: {variations}")
        print(f"Середнє значення оцінки кожного об'єкта: {mean_scores}")
        print(f"Дисперсія: {variance}")
        print(f"Середнє квадратичне відхилення: {std_deviation}")
        print(f"Коефіцієнт варіації: {coefficient_of_variation}")

    def generate_table_2_6(self, rankings):
        # Створення таблиці з результатами розрахунків з пункту 2.6

        table_data = {
            "Ранги об'єктів": [rankings[obj] for obj in self.objects],
            "Сумарне значення рангу": [sum(rankings[obj]) for obj in self.objects],
            "Результуюче значення рангу": [sum(rankings[obj]) / len(rankings[obj]) for obj in self.objects]
        }

        table = pd.DataFrame(table_data, index=self.objects)
        print("Таблиця 2:")
        print(table)

    def calculate_rank_correlation(self, rankings):
        # Обчислення рангової кореляції з пункту 2.7

        # Тут потрібно використати відповідні статистичні методи для обчислення кореляції
        pass

    def exclude_expert(self, expert):
        # Виключення експерта з групи згідно з пунктом 2.8
        pass

    def pairwise_comparison(self):
        # Виконання попарних порівнянь з пункту 2.10
        pass


# Створення екземпляру групи експертів
group = ExpertGroup(["obj_1", "obj_2", "obj_3", "obj_4", "obj_5"])

# Розрахунки для таблиць 2.4, 2.5, 2.6
total_scores = [41, 47, 36, 32, 31]
average_scores = [6.83, 7.83, 6, 5.33, 5.17]
max_scores = [0.22, 0.25, 0.19, 0.17, 0.17]
group.generate_table_2_4(total_scores, average_scores, max_scores)

evaluations = {
    "obj_1": [6, 7, 8],
    "obj_2": [7, 8, 9],
    "obj_3": [6, 7, 8]
}
group.calculate_consistency(evaluations)

rankings = {
    "obj_1": [1, 2, 3],
    "obj_2": [2, 3, 4],
    "obj_3": [3, 4, 5],
    "obj_4": [4, 5, 6],
    "obj_5": [5, 6, 7]
}
group.generate_table_2_6(rankings)

# Рангова кореляція з пункту 2.7
group.calculate_rank_correlation(rankings)

# Виключення експерта з групи згідно з пунктом 2.8
group.exclude_expert("expert_1")

# Виконання попарних порівнянь з пункту 2.10
group.pairwise_comparison()
