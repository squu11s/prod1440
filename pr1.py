def min_points_to_cover_segments(file_name):
    with open(file_name, 'r') as f:
        segments = [list(map(int, line.split())) for line in f]
    
    segments.sort(key=lambda s: s[1])
    
    points = []  
    last_point = None  
    
    for left, right in segments:
        if not points or left > last_point:
            
            points.append(right)
            last_point = right
    
    return len(points)


file_name = input('Введите имя файла с отрезками: ')
try:
    result = min_points_to_cover_segments(file_name)
    print(f'Минимальное количество точек: {result}')
except FileNotFoundError:
    print('Файл не найден!')
except Exception as err:
    print(f'Возникла ошибка: {err}')