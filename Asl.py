import subprocess
import os
import time
import shutil

"""KO'RSATILGAN PAPKA ICHIDAGI SIGNALLARNI 5 TADAN OLIB PC GA TASHAYDI VA 180 SEKUNDDA YOPADI"""
def process_files(directory_path, program_path):
    files = os.listdir(directory_path)
    num_files = len(files)
    num_groups = num_files // 5
    remaining_files = num_files % 5

    for group_index in range(num_groups):
        file_group = files[group_index * 5 : (group_index + 1) * 5]
        processes = []
        for file_name in file_group:
            file_path = os.path.join(directory_path, file_name)
            process = subprocess.Popen([program_path, file_path])
            processes.append(process)

        time.sleep(1)

        time.sleep(180)

        for process in processes:
            process.terminate()

    if remaining_files > 0:
        remaining_group = files[-remaining_files:]
        processes = []
        for file_name in remaining_group:
            file_path = os.path.join(directory_path, file_name)
            process = subprocess.Popen([program_path, file_path])
            processes.append(process)

        time.sleep(1)

        time.sleep(180)

        for process in processes:
            process.terminate()


directory_path = "D:\\__Kunlik signallar\\_Ochilgan signallar\\15.08.2023\\1-смена Абдиганиев А.А"
program_path = "D:\\__Kunlik signallar\\PCF new 2021\\PCMonitor.exe"

process_files(directory_path, program_path)

"""KO'RSATILGAN PAPKA ICHIDAGI HAR BITTA PAPKANI ICHIDAGI BERILGAN KENGAYTMALI FAYLLARNI KO'CHIRIB KO'RSATILGAN PAPKAGA O'TKAZADI"""
def move_files_with_extensions(source_directory, destination_directory, extensions):
    for root, directories, files in os.walk(source_directory):
        for file_name in files:
            file_extension = os.path.splitext(file_name)[1].lower().strip()
            if file_extension in extensions:
                source_path = os.path.join(root, file_name)
                destination_path = os.path.join(destination_directory, file_name)
                shutil.move(source_path, destination_path)


source_directory = r"D:\\__Kunlik signallar\\_Ochilgan signallar\\15.08.2023\\1-смена Абдиганиев А.А"
destination_directory = r"D:\\__Kunlik signallar\\_Ochilgan signallar\\ochilgan"
extensions = [".tif", ".docx", ".DOC", ".png", ".pdf"]  # Ma'lum kengaytmalarni o'zgartiring kerak

has_files = False

for root, directories, files in os.walk(source_directory):
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1].lower().strip()
        if file_extension in extensions:
            has_files = True
            break
    if has_files:
        break

if not has_files:
    print()
else:
    move_files_with_extensions(source_directory, destination_directory, extensions)


