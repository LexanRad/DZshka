import os


def create_names(names, ending):
    """
    Function for creating list of names of files
    :param names: blank list of names
    :param ending: ending of files
    :return: list of names
    """
    for name_of_file in lines:
        if name_of_file.strip().endswith(ending):
            names.append(name_of_file.strip())
        elif name_of_file.strip().startswith('|--'):
            break
    return names


def create_files(names):
    """
    Function of creation files in directory
    :param names: names of files
    :return: nothing
    """
    needed_dir_path = os.path.join(main_dir_name, f.readline().strip()[3:])
    if os.path.exists(needed_dir_path):
        os.chdir(needed_dir_path)
        for name_of_file in names:
            open(name_of_file.strip()[6:], 'w', encoding='utf-8')
    os.chdir('../..')
    return


# открываем файл конфига
with open('config.yaml', 'r', encoding='utf-8') as f:
    # читаем
    lines = f.readlines()
    seconds_dir_names = []
    # вытаскиваем главную и вторичные директории
    for line in lines:
        if line.startswith('|--'):
            main_dir_name = line.strip()[3:]
        elif line.startswith('   |--'):
            seconds_dir_names.append(line.strip()[3:])
    # создаем пути
    for dir_name in seconds_dir_names:
        dir_path = os.path.join(main_dir_name, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    # нумерацию для seek находил методом из методички
    f.seek(36)
    lines = f.readlines()
    # вытаскиваем имена файлов для папки settings
    names_of_files_in_settings = []
    create_names(names_of_files_in_settings, '.py')
    f.seek(20)
    # создаем файлы в ней
    create_files(names_of_files_in_settings)
    f.seek(108)
    # пытался пихнуть lines в функцию, но тогда скрипт стал все .py ставить во все папки.
    lines = f.readlines()
    names_of_files_in_mainapp = []
    # вытаскиваем имена файлов для mainapp
    create_names(names_of_files_in_mainapp, '.py')
    f.seek(93)
    # создаем файлы
    create_files(names_of_files_in_mainapp)
    f.seek(278)
    lines = f.readlines()
    names_of_files_in_authapp = []
    # имена для authapp
    create_names(names_of_files_in_authapp, '.py')
    f.seek(263)
    # создаем
    create_files(names_of_files_in_authapp)
    # не хотел делать чек напрямую, но не получилось.
    os.chdir('my_cool_project/authapp')
    f.seek(339)
    new_lines = f.readlines()
    # смотрим существует ли необходимая директория для оставшихся файлов
    for line in new_lines:
        if line.startswith('   |  |--'):
            second_dir_name = line.strip()[6:]
        elif line.startswith('   |     |--'):
            third_dir_name = line.strip()[9:]
    dir_path = os.path.join(second_dir_name, third_dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # чекаем ее
    os.chdir(dir_path)
    names_in_temp_auth = []
    f.seek(359)
    lines = f.readlines()
    # создаем имена для нее (в этот раз файлы html)
    create_names(names_in_temp_auth, '.html')
    # создаем сами файлы
    for file_name in names_in_temp_auth:
        open(file_name.strip()[12:], 'w', encoding='utf-8')
