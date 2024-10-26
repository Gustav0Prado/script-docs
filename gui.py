#!/usr/bin/python3

import FreeSimpleGUI as sg
import subprocess

file_list_column = [
    [
        sg.Text("Arquivo Docx Base"),
        sg.In(size=(25, 10), enable_events=True, key="-DOCX-"),
        sg.FileBrowse(file_types=(('Arquivo docx', '*.docx'),))
    ],
    [
        sg.Text("Arquivo .csv          "),
        sg.In(size=(25, 1), enable_events=True, key="-CSV-"),
        sg.FileBrowse(file_types=(('Arquivo csx', '*.csv'),))
    ],
    [
        sg.Text("Diretório de Saída  "),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse()
    ],
    [
        sg.Button(button_text='Gerar documentos', key="-RUN-")
    ]
]


# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column, element_justification='center'),
    ],
]

window = sg.Window("Gerador de Docs", layout,  location=(400, 300), grab_anywhere=True)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-RUN-":
        arquivo_docx = window['-DOCX-'].get()
        arquivo_csv  = window['-CSV-'].get()
        dir_saida    = window['-FOLDER-'].get()

        if (not arquivo_docx) or (not arquivo_csv) or (not dir_saida):
            sg.popup("ERRO!! Insira todos os dados pedidos", location=(500, 400))
        else:
            s = subprocess.run(['./generate_docs.py', arquivo_csv, arquivo_docx, dir_saida+'/'], capture_output=True)
            sg.popup(f'{s.stdout.decode()}\nArquivos gerados com sucesso!!', location=(500, 400))
        

window.close()