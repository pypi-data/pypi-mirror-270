import os

cpp_file = "test.cpp"

executable_file = "test.exe"

output_directory = "D:\\Study"

output_executable_path = os.path.join(output_directory, executable_file)

compile_command = f"g++ -o \"{output_executable_path}\" {cpp_file}"