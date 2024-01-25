# Outras bibliotecas: pygames; pyqt

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

alunos=[
    {
        "matricula":1,
        "nome":"Jonas Lopes",
        "idade": 22,
        "curso":"Javascript",
        "novato": False
    }
]

matricula_atual = 1
index = 0


def limparCampos():
    txtMatricula.config(state=NORMAL)
    txtMatricula.delete(0,END)
    txtMatricula.config(state=DISABLED)
    txtNome.delete(0, END)
    txtIdade.delete(0, END)
    comboCursos.set("")  # deletando do comboBox
    opcao.set(False)
    return None

def preencherCampos(event)->None:
    global index
    linha_selecionada = tabela.selection() # coleta o valor selecionado
    index = tabela.index(linha_selecionada)
    aluno = alunos[index]
    limparCampos()
    txtMatricula.config(state=NORMAL)
    txtMatricula.insert(END,str(aluno["matricula"]))
    txtMatricula.config(state=DISABLED)
    txtNome.insert(END,aluno["nome"])
    txtIdade.insert(END, str(aluno["idade"]))
    comboCursos.insert(END, aluno["curso"])


def atualizarTabela()->None:
    for linha in tabela.get_children(): #get_children() -> Retorna todas as linhas da tabela
        tabela.delete(linha)

    for aluno in alunos:
        tabela.insert("",END,values=(aluno["matricula"],
                                     aluno["nome"],
                                     aluno["idade"],
                                     aluno["curso"],
                                     aluno["novato"]))

def AdicionarAluno()->None:
    global matricula_atual, alunos

    matricula_atual+=1

    nome = txtNome.get()
    idade = int(txtIdade.get())
    curso = comboCursos.get()
    novato = opcao.get()
    aluno = {
        "matricula": matricula_atual,
        "nome":nome,
        "idade": idade,
        "curso":curso,
        "novato":novato
    }
    messagebox.showinfo("Sucesso!", f"Aluno {nome} adicionado com sucesso")
    alunos.append(aluno)

    # Limpar campos
    limparCampos()
    atualizarTabela()



#----------------------Configurações da janela-------------------#
backGroundColor = "#141414"
fontColor = "#f0470a"
cinza = "#6e6b6b"

janela = Tk()

janela.title("Alunos - Infinity")
janela.config(bg=backGroundColor)

# janela.geometry("800x650")

#---------------------Labels---------------------------#
labelMatricula = Label(janela,text="Matricula:",font="Times 18 bold",
                       fg=fontColor,bg=backGroundColor)
labelMatricula.grid(row=0,column=0,sticky=E)

txtMatricula = Entry(janela,font="Times 16",bg=cinza, width=26,state=DISABLED)
txtMatricula.grid(row=0,column=1,sticky=W)

labelNome = Label(janela, font="Times 18 bold", text="Nome:",
                  fg=fontColor,bg=backGroundColor)
labelNome.grid(row=1, column=0,sticky=E)

txtNome = Entry(janela,font="Tahoma 16",bg=cinza, width=26)
txtNome.grid(row=1,column=1,sticky=W)

labelIdade = Label(janela,text="Idade:", font="Times 18 bold",
                   fg=fontColor,bg=backGroundColor)
labelIdade.grid(row=2,column=0,sticky=E)

txtIdade = Entry(janela,font="Tahoma 16",bg=cinza, width=26)
txtIdade.grid(row=2,column=1,sticky=W)

labelCurso = Label(janela,text="Curso", font="Times 18 bold",
                   fg=fontColor,bg=backGroundColor)
labelCurso.grid(row=3,column=0,sticky=E)

cursos = ["Javascript","Python","React","NodeJs"]
comboCursos = ttk.Combobox(janela,font="Times 16",values=cursos)
comboCursos.grid(row=3,column=1,sticky=W)

labelNovato = Label(janela,text="Novato?",font="Times 18 bold",
                    fg=fontColor,bg=backGroundColor)
labelNovato.grid(row=4,column=0,sticky=E)

opcao=BooleanVar(value= False)
checkNovato = ttk.Checkbutton(janela,variable=opcao)
checkNovato.grid(row=4,column=1,sticky=W)


#-------------------Botões------------------#

btnAdicionar = Button(janela,text="Adicionar",
                      font="Times 18 bold", fg=backGroundColor,
                      bg="#00ffa3",height=1,width=8,command=AdicionarAluno)
btnAdicionar.grid(row=5,column=0)

btnEditar = Button(janela,text="Editar",font="Times 18 bold",
                   fg=backGroundColor,bg="#00ffa3",height=1,width=8)
btnEditar.grid(row=5,column=1)

btnApagar = Button(janela,text="Apagar",font="Times 18 bold",
                   fg=backGroundColor,bg="#00ffa3",height=1,width=8)
btnApagar.grid(row=5,column=2)


# ----------------------Tabela --------------------#
colunas = ["Matricula","Nome","Idade","Curso","Novato"]
tabela = ttk.Treeview(janela,columns=colunas,show="headings")

for coluna in colunas:
    tabela.heading(coluna,text=coluna) #acessando cada cabeçalho
    tabela.column(coluna,width=110)

tabela.grid(row=6,columnspan=3)
tabela.bind("<ButtonRelease-1>",preencherCampos)












atualizarTabela()
janela.mainloop()