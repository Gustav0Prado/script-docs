#!/usr/bin/python3

from docx import Document
import docxedit, os, subprocess, sys, contextlib, io

if len(sys.argv) == 2 and sys.argv[1] == '-h':
   print('Uso do programa: ')
   print('./generate_docs.py -> Gera automaticamente a partir dos diretorios padrao')
   print('./generate_docs.py <Arquivo csv> <Arquivo Docx> <Diretorio de saida> -> Gera a partir dos arquivos especificados')

if len(sys.argv) == 1:
   arquivo_csv  = 'Entrada/Substituicao.csv'
   arquivo_docx = 'Entrada/Sample.docx'
   dir_saida    = 'Saida/'
elif len(sys.argv) == 4:
   arquivo_csv  = sys.argv[1]
   arquivo_docx = sys.argv[2]
   dir_saida    = sys.argv[3]
else:
   print('Erro ao passar entrada ao programa, verifique se a quantidade de parametros esta certa')

file = open(arquivo_csv, 'r')

campos = file.readline().strip('\n').split(';')

# print('campos:', campos)

# Isso aqui só tira da tela o monte de saidas que essas funcoes tem
with contextlib.redirect_stdout(io.StringIO()):
   for line in file:
      document = Document(arquivo_docx)
      for i in range(len(campos)):
         if i == 0:
            Nome = line.split(';')[i]
         docxedit.replace_string(document, old_string=campos[i], new_string=line.split(';')[i])
      document.save(dir_saida+f'{Nome}.docx')

# Pra cada DOCX gerado, converte pra PDF
for filename in os.listdir(dir_saida):
    f = os.path.join(dir_saida, filename)

    # Printa os nomes da saida pra saber que deu certo, mas so os PDFs finais
    if ('.docx' in filename):
       print(filename[:-5] + ' ✓')
    # checking if it is a file
    if os.path.isfile(f):
        subprocess.run(['doc2pdf', dir_saida+f'{filename}'], stderr=subprocess.DEVNULL)
