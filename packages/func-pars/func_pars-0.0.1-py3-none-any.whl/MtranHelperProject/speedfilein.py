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

        if os.path.getsize(cpp_file) == 0:
            print("Code 0")
            return

        # Проверка содержимого файла на наличие кода
        with open(cpp_file, 'r', encoding='utf-8') as f:
            code_lines = f.readlines()

        has_code = any(line.strip() and not line.strip().startswith('//') for line in code_lines)
        if not has_code:
            print("In your file isn't compilation code")
            return

        # Запуск процесса компиляции
        try:
            subprocess.run(compile_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            exit(1)

        # Команда для запуска исполняемого файла
        run_command = f"\"{output_executable_path}\""

        # Запуск исполняемого файла
        try:
            subprocess.run(run_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            exit(1)
