#!/usr/bin/python3

from docx import Document
import docxedit, os, subprocess, contextlib, io

file = open('Entrada/Substituicao.csv', 'r')

campos = file.readline().strip('\n').split(';')

print('campos:', campos)

# Isso aqui só tira da tela o monte de saidas que essas funcoes tem
with contextlib.redirect_stdout(io.StringIO()):
   for line in file:
      document = Document('Entrada/Sample.docx')
      for i in range(len(campos)):
         if i == 0:
            Nome = line.split(';')[i]
         docxedit.replace_string(document, old_string=campos[i], new_string=line.split(';')[i])
      document.save(f'./Saida/{Nome}.docx')

# Pra cada DOCX gerado, converte pra PDF
for filename in os.listdir('Saida'):
    f = os.path.join('Saida', filename)
    
    # Printa os nomes da saida pra saber que deu certo, mas so os PDFs finais
    if ('.pdf' in filename):
       print(filename)
    # checking if it is a file
    if os.path.isfile(f):
        subprocess.run(['doc2pdf', f'Saida/{filename}'], stderr=subprocess.DEVNULL)
