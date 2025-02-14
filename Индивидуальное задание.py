import os
import random
import string

# Глобальная переменная для хранения найденных файлов
found_files = []

def create_random_directory_tree(base_path, depth=10, max_subdirs=3, max_files=5):
    """Рекурсивно создаёт случайную структуру каталогов и файлов"""
    if depth == 0:
        return

    os.makedirs(base_path, exist_ok=True)

    # Генерируем случайные файлы
    extensions = ['.txt', '.log', '.csv', '.json', '.xml']
    for _ in range(random.randint(1, max_files)):
        filename = ''.join(random.choices(string.ascii_letters, k=8)) + random.choice(extensions)
        with open(os.path.join(base_path, filename), 'w') as f:
            f.write("Sample data")

    # Генерируем случайные подкаталоги
    for _ in range(random.randint(1, max_subdirs)):
        subdir_name = ''.join(random.choices(string.ascii_letters, k=5))
        create_random_directory_tree(os.path.join(base_path, subdir_name), depth - 1, max_subdirs, max_files)


def iterative_deepening_search(root_path, extension=".log", max_depth=10):
    """Поиск файлов с заданным расширением методом итеративного углубления"""
    for depth in range(1, max_depth + 1):
        found = depth_limited_search(root_path, extension, depth)
        if found:
            return found
    return None


def depth_limited_search(path, extension, depth):
    """Поиск с ограничением глубины"""
    global found_files
    if depth < 0:
        return False

    try:
        for entry in os.scandir(path):
            if entry.is_file() and entry.name.endswith(extension):
                found_files.append(entry.path)
            elif entry.is_dir():
                depth_limited_search(entry.path, extension, depth - 1)
    except PermissionError:
        pass

    return bool(found_files)


# Создаём виртуальное дерево файлов в папке "virtual_disk"
base_directory = "virtual_disk"
create_random_directory_tree(base_directory)

# Запускаем поиск файлов с расширением .log
iterative_deepening_search(base_directory, ".log")

# Вывод результатов
print("\nНайденные файлы .log:")
for file in found_files:
    print(file)
