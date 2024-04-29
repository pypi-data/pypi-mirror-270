import os
import subprocess

cpp_file = "test.cpp"

executable_file = "test.exe"

output_directory = "D:\\Study"

output_executable_path = os.path.join(output_directory, executable_file)

compile_command = f"g++ -o \"{output_executable_path}\" {cpp_file}"


class TranslatorFor:

    @staticmethod
    def reading():
        # Запуск процесса компиляции
        try:
            subprocess.run(compile_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при компиляции: {e}")
            exit(1)

        # Команда для запуска исполняемого файла
        run_command = f"\"{output_executable_path}\""

        # Запуск исполняемого файла
        try:
            subprocess.run(run_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при запуске исполняемого файла: {e}")
            exit(1)
