import csv
import os
import re
from itertools import chain
from datetime import datetime
from typing import Generator, Any



file = r'C:\Users\Guilh\OneDrive\Documentos\GitHub\rename_files\names.csv'


def reader_csv_file() -> Generator[list[dict[str | Any, str | Any]], None, None]:
      """Leitura do excel com a referencia e o nome da loja"""
      with open(file, newline='', encoding='latin-1') as csvfile:
        try:
            reader = csv.DictReader(
                csvfile, delimiter=";", skipinitialspace=True)
            rows = [row for row in reader]
            yield rows
    
        except:
            print("erro file")

   
def get_pdf_files(*args, **kwargs) -> Generator[dict[str, Any], None, None]:
    """Leitura do diretorio dos arquivos pdf"""
    path_pdf = r'C:\Users\Guilh\OneDrive\Documentos\GitHub\rename_files\pdffiles'
    excel_file = [{**file} for file in args]
   
    pdfs = os.listdir(path_pdf)
    cont = len(excel_file)
    i = 0
    while i < cont:
        str(excel_file[i]['id'])+str('.pdf')
        value = str(excel_file[i]['id'])+str('.pdf')
        """Verifica os nomes com as referencias do id compativeis e retorna em um dicionario"""
        teste = [item.split()[-1].replace("março-","") for item in pdfs if value in item]

        new_path = 'seleção março-'+str(next(chain(teste)))
        dict_file = {
            "id":excel_file[i]['id'],
            "loja":excel_file[i]['name'],
            "name":new_path}
      
        yield dict_file

    
        i+=1

   #print(os.listdir(os.path.join(os.getcwd(),'pdffiles')))

def get_names() -> Generator[Generator[dict[str, Any], None, None], None, None]:
    list_dicts = reader_csv_file()
    row = [rows for rows in list_dicts]
    cont = len(row)

    i = 0
    while i < cont:
        row[i]
        file = get_pdf_files(*row[i])
        yield file
        
        i+=1

def raname_files() -> None:
    now = str(datetime.now()).split()[0]
 
    path = r"C:\Users\Guilh\OneDrive\Documentos\GitHub\rename_files\pdffiles"
    dict_files = next(get_names())
    try:
        for dict in dict_files:
            if dict['name'] in os.listdir(path):
                teste = os.rename(os.path.join(path,dict['name']),dict['loja']+'id_'+str(dict['id'])+'_'+str(now)+'.pdf')
                print(teste)
    except Exception as e:
        print(e)
         


raname_files()