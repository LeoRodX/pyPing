import subprocess
import platform

# Используем пинг для проверки доступности хотя бы одного из двух хостов с учетом особенностей
# операционной системы
def ping_host(host0, host1):
    try:
        # Проверка операционной системы
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'
        # Выполняем команду ping
        command0 = ['ping', parameter, '1', host0]
        output0 = subprocess.run(command0, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True)
        command1 = ['ping', parameter, '1', host1]
        output1 = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True)
        # Если код возврата 0, хост доступен
        if output0.returncode == 0 or output1.returncode == 0:
            print(f"Хост {output0.returncode} or {output1.returncode} доступен.")
        else:
            print(f"Хост {output0.returncode} or {output1.returncode} недоступен.")

    except Exception as e:
        print(f"Ошибка при выполнении ping: {e}")


# Пример использования
host_0 = ("yandex.ru")
host_1 = ("y2andex.ru")
ping_host(host_0, host_1)
