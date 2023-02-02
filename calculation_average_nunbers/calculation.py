import csv
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))

file_name = "entrada.csv"

def calculate_average(list_number): 
    
    total_number = len(list_number) 
    result = int(total_number / 2)

    if total_number > 1 and total_number % 2 == 0:
        return round((list_number[result]+list_number[result-1])/2, 1)
    
    else: 
        return round(list_number[int(result)],1)
    

def validate_total_lines(total_lines, total_lines_doc):
    return total_lines == total_lines_doc


def writer_file(list_writer:list):
    new_list = []
    for row in list_writer: 
        new_list.append([f"{row}"])
    new_list.insert(0,[f"{len(list_writer)}"])
    new_list.insert(0,["numbers"])

    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter= ',')
        for item in new_list:
            writer.writerow(item)

def reader_file(): 
    list_return = []
    average = 0
    total_lines_doc = 0

    with open(file_name, 'r') as file:
        readerInput = csv.DictReader(file, delimiter=",")
        
        for index, row in enumerate(readerInput):
            if index == 0: 
                total_lines_doc = int(row['numbers'])
                print(f"Total de numeros no arquivo: {total_lines_doc}")
                continue
                
            list_return.append(int(row['numbers']))

            average = calculate_average(list_number=list_return)
            
            print(row['numbers'])

    if not validate_total_lines(total_lines_doc=total_lines_doc, total_lines=len(list_return)): 
        print("Arquivo de entrada invalido! Favor corrigir e executar novamente!")
        sys.exit()

    return list_return, average
