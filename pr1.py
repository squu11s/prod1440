def min_points_to_cover_segments(file_name):
    with open(file_name, 'r') as f:
        segments = [list(map(int, line.split())) for line in f]
    
    segments.sort(key=lambda s: s[1])
    
    points = []  # Список точек
    last_point = None  # Последняя используемая точка
    
    for left, right in segments:
        if not points or left > last_point:
            # Добавляем новую точку, если текущий отрезок не покрыт предыдущей точкой
            points.append(right)
            last_point = right
    
    return len(points)

# Запуск программы
file_name = input('Введите имя файла с отрезками: ')
try:
    result = min_points_to_cover_segments(file_name)
    print(f'Минимальное количество точек: {result}')
except FileNotFoundError:
    print('Файл не найден!')
except Exception as err:
    print(f'Возникла ошибка: {err}')