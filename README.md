# Script para o preenchimento automático de documentos

## 💻 Setup

Pra poder rodar esse script você vai precisar de duas coisas

   1. O módulo docx do python, que pode ser instalado com: ```pip install docx``` 
   2. O programa unoconv no Linux (ou WSL/Mac), que pode ser instalado com:
   ```sudo apt install unoconv -y``` ou similares
   3. Se quiser buildar do vai precisar do tkinter, do FreeSimpleGUI e do pyinstaller, mas não recomendo tentar se não souber o que tá fazendo

## 🐍 O Python

### 🧐 Lendo e editando o arquivo
É aqui que usamos primeiramente o módulo docx do Python, pra buscar e substituir os dados que queremos no arquivo. Só isso mesmo, ele faz uma busca pelas palavras-chave que tem que ser mudadas e substitui elas pelo que você indicar.

### 📊 A planilha
Isso aqui tem que ser na gambiarra um pouco.

### 🔄 Convertendo pra PDF
Pra isso a gente uso o unoconv, que vai ter que instalar o Libreoffice pra ter essa função de converter, mas é a vida 🤷. Pra usar ele dentro do script, basicamente criamos um *subprocess* no Python que vai rodar o comando `doc2pdf Saida.docx` e fazer o processo de conversão pra gente.

### A interface de usuário
Fiz uma interface de usuário com FreeSimpleGUI pra deixar mais fácil ainda o uso disso, só selecionar os arquivos normal e rodar bem mais fácil

## 😆 Como usar (do jeito fácil)
Só rodar o programa *./GeradorDocs* e seguir as coisas que estão na tela :)


## 🤔 Como usar (do jeito difícil)
1. Colocar o arquivo *'Sample.docx'*, que é o arquivo que você quer preencher em 'Entrada'
2. Criar ou completar a planilha *'Substituicao.csv'*, tendo na primeira linha os campos/palavras-chave que você quer substituir e nas outras linhas os dados que você quer colocar
3. Rodar o Script
4. Na pasta Saida vai ter os PDFs :)
5. Só como observação, nem todas as palavras-chaves funcionam direito por algum problema interno da função que edita o docx, então por exemplo eu tentei num_CPF e não funcionou a substituição mas CPF_num deu certo, então vai um pouco de tentativa e erro de ver se tá dando certo ou não, mas recomendo só usar um underline _ na frente das coisas que geralmente funciona
6. Alternativamente pode rodar *./generate_docs.py <Arquivo csv> <Arquivo Docx> <Diretorio de saida>* pra especificar onde esses arquivos estão