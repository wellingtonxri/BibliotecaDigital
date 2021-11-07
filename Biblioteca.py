from Conexão_BD import * #Importando recursos da ConexãoOfc.py
from PyQt5 import uic,QtWidgets,QtGui
import time

def chama_sistema_geral():
    time.strftime('%H%M', time.localtime())
    hora=time.strftime('%H%M', time.localtime())
    login_entrar.label_2.setText ( "" )
    nome_usuario=login_entrar.lineEdit.text()
    bem=nome_usuario
    senha=login_entrar.lineEdit_2.text()
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(nome_usuario))
        senha_bd = cursor.fetchall()
        if  senha == senha_bd[0][0] :
            login_entrar.close()
            nome_usuario=login_entrar.lineEdit.setText("")
            senha=login_entrar.lineEdit_2.setText("")
            sistema_geral.show()
            if hora >= '0600' and hora <='1259':
                sistema_geral.label_11.setText('Bom dia'+bem+'!')
            elif hora >= '1300' and hora <='1759':
               sistema_geral.label_11.setText('Boa tarde'+bem+'!')
            elif hora >= '1800' and hora <='2359':
                sistema_geral.label_11.setText('Boa noite '+bem+'!')
            else:
                sistema_geral.label_11.setText("Já é madrugada, vá dormir e venha amanhã!")     
        else :
            login_entrar.label_2.setText("Usuário ou Senha inválidos!")
    except:
        login_entrar.label_2.setText("Usuário ou Senha inválidos!")

def tela_adm_cadastro():
    
    login_entrar.close()
    adm_cadastro.show()

def login_adm():
    admlogin=adm_cadastro.adm.text()
    admsenha=adm_cadastro.admsenha.text()
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM adm WHERE login = '{}'".format(admlogin))
        senha_db = cursor.fetchall()
        if admsenha == senha_db[0][0] :
            abre_tela_cadastro()
            adm_cadastro.erro.setText("")
            adm_cadastro.adm.setText("")
            adm_cadastro.admsenha.setText("")
        else:
            adm_cadastro.erro.setText("Usuário ou Senha inválidos!")
    except:
        adm_cadastro.erro.setText("Usuário ou Senha inválidos!")

def voltar_adm_cadastro():
    adm_cadastro.adm.setText("")
    adm_cadastro.admsenha.setText("")
    adm_cadastro.erro.setText("")
    adm_cadastro.close()
    login_entrar.show()

def sair_geral():
    banco.close
    login_entrar.close()

def logout():
    sistema_geral.close()
    login_entrar.show()
    
def abre_tela_cadastro():
    adm_cadastro.close()
    tela_cadastro.show()

def voltar_login_entrar():
    tela_cadastro.label_6.setText("")
    tela_cadastro.close()
    login_entrar.show()

def cadastrar():
    tela_cadastro.label_7.setText("")
    tela_cadastro.label_6.setText("")
    nome=tela_cadastro.lineEdit.text()
    login=tela_cadastro.lineEdit_2.text()
    senha=tela_cadastro.lineEdit_3.text()
    c_senha=tela_cadastro.lineEdit_4.text()
    try:
        if (senha == c_senha):
            try:
                cursor = banco.cursor()
                comando_SQL = "INSERT INTO cadastro (nome, login, senha) VALUES (%s,%s,%s)"
                dados = (nome,login,senha)
                cursor.execute(comando_SQL,dados)
                banco.commit()
                tela_cadastro.label_6.setText("Usuário cadastrado com sucesso")
                nome=tela_cadastro.lineEdit.setText("")
                login=tela_cadastro.lineEdit_2.setText("")
                senha=tela_cadastro.lineEdit_3.setText("")
                c_senha=tela_cadastro.lineEdit_4.setText("")

            except ValueError:
                print("Erro ao inserir os dados")
            except:
                tela_cadastro.label_8.setText("Para cadastrar um novo usúario, volte para a tela Login ")
        else:
            tela_cadastro.label_7.setText("As senhas digitadas estão diferentes")
    except AttributeError:
        print("Erro Now")

def alunos():
    sistema_geral.close()
    alunos_a.show()

def voltar_sistema_geral():
    alunos_a.close()
    sistema_geral.show()

def abre_listar_alunos():
    alunos_a.close()
    listar_alunos.show()
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM alunos')
    dados_lidos=cursor.fetchall()
    listar_alunos.tableWidget.setRowCount(len(dados_lidos))
    listar_alunos.tableWidget.setColumnCount(4)
    listar_alunos.tableWidget.setColumnWidth(0, 73)
    listar_alunos.tableWidget.setColumnWidth(1, 300)
    listar_alunos.tableWidget.setColumnWidth(2, 45)
    listar_alunos.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    listar_alunos.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            listar_alunos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def voltar_listar_alunos():
    listar_alunos.close()
    alunos_a.show()

def abrir_tela_editar_aluno():
    alunos_a.close()
    tela_editar_aluno.show()

def voltar_editar_aluno():
    tela_editar_aluno.close()
    alunos_a.show()
    tela_editar_aluno.label_2.setText("")

def editar_aluno():
    try:
        tela_editar_aluno.label_3.setText("")
        tela_editar_aluno.label_7.setText("")
        matricula=int(tela_editar_aluno.matricula.text())
        serie=tela_editar_aluno.serie.text()
        contato=tela_editar_aluno.contato.text()
        cursor = banco.cursor()
        comando_SQL = "UPDATE alunos SET serie = %s , contato_aluno = %s  WHERE aluno_matricula = %s"
        dados = (serie,contato,matricula)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        tela_editar_aluno.label_2.setText("Alterações feitas com sucesso")
        matricula=tela_editar_aluno.matricula.setText("")
        serie=tela_editar_aluno.serie.setText("")
        contato=tela_editar_aluno.contato.setText("")           
    except ValueError:
        tela_editar_aluno.label_3.setText("Matrícula invalida")
    except:
        tela_editar_aluno.label_7.setText("Série invalida, digite dessa forma (1º C)")

def abrir_tela_cadastrar_alunos():
    alunos_a.close()
    tela_cadastrar_aluno.show()

def voltar_cadastrar_aluno():
    tela_cadastrar_aluno.close()
    alunos_a.show()
    tela_cadastrar_aluno.label_2.setText("")

def cadastrar_aluno():
    try:
        tela_cadastrar_aluno.label_7.setText("")
        nome=tela_cadastrar_aluno.nome.text()
        serie=tela_cadastrar_aluno.serie.text()
        contato=tela_cadastrar_aluno.contato.text()
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO alunos (nome_aluno, serie, contato_aluno) VALUES (%s,%s,%s)"
        dados = (nome,serie,contato)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        tela_cadastrar_aluno.label_2.setText("Aluno cadastrado com sucesso")
        nome=tela_cadastrar_aluno.nome.setText("")
        serie=tela_cadastrar_aluno.serie.setText("")
        contato=tela_cadastrar_aluno.contato.setText("")
    except:
        tela_cadastrar_aluno.label_7.setText("Série invalida, digite dessa forma (1º C)")

def abrir_tela_excluir_aluno():
    alunos_a.close()
    tela_excluir_aluno.show()

def voltar_excluir_aluno():
    tela_excluir_aluno.nome.setText("")
    tela_excluir_aluno.serie.setText("")
    tela_excluir_aluno.contato.setText("")
    tela_excluir_aluno.matricula.setText("")
    tela_excluir_aluno.label_11.setText("")
    tela_excluir_aluno.label_10.setText("")
    tela_excluir_aluno.label_12.setText("")
    tela_excluir_aluno.close()
    alunos_a.show()

def excluir_aluno_pesq():
    try:
        achei = 0
        tela_excluir_aluno.label_10.setText("")
        tela_excluir_aluno.label_12.setText("")
        cursor = banco.cursor()
        comando_SQL = 'select * from alunos'
        cursor.execute(comando_SQL)
        matricula=int(tela_excluir_aluno.matricula.text())
        valores_lidos = cursor.fetchall()
        for i in valores_lidos:
            if i[0] == matricula:
                tela_excluir_aluno.nome.setText(i[1])
                tela_excluir_aluno.serie.setText(i[2])
                tela_excluir_aluno.contato.setText(i[3])
                achei = 1
        if achei == 0:
            tela_excluir_aluno.label_10.setText("Matrícula não encontrada")
            tela_excluir_aluno.nome.setText("")
            tela_excluir_aluno.serie.setText("")
            tela_excluir_aluno.contato.setText("")
            banco.commit()
    except:
        tela_excluir_aluno.label_11.setText("Insira apenas números inteiros")
    finally:
        print("Opa kk")

def excluir_aluno():
    try:
        tela_excluir_aluno.label_12.setText("")
        matricula=int(tela_excluir_aluno.matricula.text())
        cursor = banco.cursor()
        comando_SQL2 = "DELETE FROM alunos WHERE aluno_matricula = {}".format(matricula)
        cursor.execute(comando_SQL2)
        banco.commit()
        tela_excluir_aluno.label_12.setText("Aluno excluido com sucesso")
        tela_excluir_aluno.nome.setText("")
        tela_excluir_aluno.serie.setText("")
        tela_excluir_aluno.contato.setText("")
        tela_excluir_aluno.matricula.setText("")
    except ValueError:
        tela_excluir_aluno.label_11.setText("Insira apenas números inteiros")
    
def abrir_tela_pesquisar_aluno():
    alunos_a.close()
    tela_pesquisar_aluno.show()

def voltar_pesquisar_aluno():
    tela_pesquisar_aluno.label_3.setText("")
    tela_pesquisar_aluno.matricula.setText("")
    tela_pesquisar_aluno.aluno.setText("")
    tela_pesquisar_aluno.serie.setText("")
    tela_pesquisar_aluno.contato.setText("")
    nome=tela_pesquisar_aluno.nome_3.setText("")
    tela_pesquisar_aluno.label_13.setText("")
    tela_pesquisar_aluno.close()  
    alunos_a.show()

def pesquisar_aluno():
    try:
        achei = 0
        cursor = banco.cursor()
        comando_SQL = 'SELECT * FROM alunos'
        cursor.execute(comando_SQL)
        nome=tela_pesquisar_aluno.nome_3.text()
        valores_lidos = cursor.fetchall()
        for i in valores_lidos:
            if i[1] == nome:
                x = i[0]
                y = ''
                a = y + str(x)
                tela_pesquisar_aluno.matricula.setText(a)
                tela_pesquisar_aluno.aluno.setText(i[1])
                tela_pesquisar_aluno.serie.setText(i[2])
                tela_pesquisar_aluno.contato.setText(i[3])
                tela_pesquisar_aluno.label_3.setText("")
                achei = 1
                tela_pesquisar_aluno.label_13.setText("Pesquisa realizada")
        if achei == 0:
            tela_pesquisar_aluno.label_3.setText("Aluno não encontrado!")
            tela_pesquisar_aluno.label_13.setText("")
            tela_pesquisar_aluno.matricula.setText("")
            tela_pesquisar_aluno.aluno.setText("")
            tela_pesquisar_aluno.serie.setText("")
            tela_pesquisar_aluno.contato.setText("")
            banco.commit()
    except:
        print("OPS")
    finally:
        print("Hehe")

def voltar_tela_livros():
    tela_livros.close()
    sistema_geral.show()

def abrir_tela_livros():
    sistema_geral.close()
    tela_livros.show()

def voltar_tela_listar_livros():
    tela_listar_livros.close()
    tela_livros.show()

def abrir_tela_listar_livros():
    tela_livros.close()
    tela_listar_livros.show()
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM livros')
    dados_lidos=cursor.fetchall()
    tela_listar_livros.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_livros.tableWidget.setColumnCount(6)
    tela_listar_livros.tableWidget.setColumnWidth(0, 175)
    tela_listar_livros.tableWidget.setColumnWidth(1, 200)
    tela_listar_livros.tableWidget.setColumnWidth(2, 480)
    tela_listar_livros.tableWidget.setColumnWidth(3, 270)
    tela_listar_livros.tableWidget.setColumnWidth(4, 250)
    tela_listar_livros.tableWidget.setColumnWidth(5, 140)
    tela_listar_livros.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tela_listar_livros.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            tela_listar_livros.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def abrir_tela_editar_livros():
    tela_livros.close()
    tela_editar_livro.show()

def voltar_tela_editar_livro():
    tela_editar_livro.label_2.setText("")
    tela_editar_livro.label_3.setText("")
    tela_editar_livro.ISBN.setText("")
    tela_editar_livro.genero.setText("")
    tela_editar_livro.editora.setText("")
    tela_editar_livro.close()
    tela_livros.show()

def isbn_editar():
    try:
        isbn=tela_editar_livro.ISBN.text()
        cursor = banco.cursor()
        cursor.execute("SELECT isbn FROM livros WHERE isbn = '{}'".format(isbn))
        isbn_db = cursor.fetchall()
        if isbn == isbn_db[0][0] :
            tela_editar_livro.label_3.setText("")
            editar_livro()
        else:
            tela_editar_livro.label_3.setText("ISBN inválido")
    except:
        tela_editar_livro.label_3.setText("ISBN inválido")

def editar_livro():
    isbn=tela_editar_livro.ISBN.text()
    genero=tela_editar_livro.genero.text()
    editora=tela_editar_livro.editora.text()
    cursor = banco.cursor()
    comando_SQL = "UPDATE livros SET genero = %s , editora = %s WHERE ISBN = %s "
    dados = (genero,editora,isbn)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    tela_editar_livro.label_2.setText("Alterações feitas com sucesso")
    isbn=tela_editar_livro.ISBN.setText("")
    genero=tela_editar_livro.genero.setText("")
    editora=tela_editar_livro.editora.setText("")

def abrir_tela_cadastrar_livro():
    tela_livros.close()
    tela_cadastrar_livro.show()

def voltar_tela_cadastrar_livros():
    tela_cadastrar_livro.label_3.setText("")
    tela_cadastrar_livro.label_10.setText("")
    tela_cadastrar_livro.ISBN.setText("")
    tela_cadastrar_livro.autor.setText("")
    tela_cadastrar_livro.livro.setText("")
    tela_cadastrar_livro.genero.setText("")
    tela_cadastrar_livro.editora.setText("")
    tela_cadastrar_livro.label_9.setText("")
    tela_cadastrar_livro.ano.setText("")
    tela_cadastrar_livro.close()
    tela_livros.show()

def isbn_cadastrar():
    try:
        isbn=tela_cadastrar_livro.ISBN.text()
        cursor = banco.cursor()
        cursor.execute("SELECT isbn FROM livros WHERE isbn = '{}'".format(isbn))
        isbn_db = cursor.fetchall()
        if isbn == isbn_db[0][0] :
            tela_cadastrar_livro.label_9.setText("")
            tela_cadastrar_livro.label_10.setText("")
            tela_cadastrar_livro.label_3.setText("ISBN já cadastrado")
        else:
            tela_cadastrar_livro.label_3.setText("")
            cadastrar_livro()
    except:
        tela_cadastrar_livro.label_3.setText("")
        cadastrar_livro()

def cadastrar_livro():
    try:
        isbn=tela_cadastrar_livro.ISBN.text()
        autor=tela_cadastrar_livro.autor.text()
        livro=tela_cadastrar_livro.livro.text()
        genero=tela_cadastrar_livro.genero.text()
        editora=tela_cadastrar_livro.editora.text()
        ano=int(tela_cadastrar_livro.ano.text())
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO livros (ISBN, autor, nome_livro, genero, editora, ano_publicacao) VALUES (%s, %s, %s, %s, %s, %s)"
        dados = (isbn,autor,livro,genero,editora,ano)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        tela_cadastrar_livro.label_10.setText("Cadastro realizado com sucesso")
        isbn=tela_cadastrar_livro.ISBN.setText("")
        autor=tela_cadastrar_livro.autor.setText("")
        livro=tela_cadastrar_livro.livro.setText("")
        genero=tela_cadastrar_livro.genero.setText("")
        editora=tela_cadastrar_livro.editora.setText("")
        tela_cadastrar_livro.label_9.setText("")
        tela_cadastrar_livro.ano.setText("")
    except ValueError:
        tela_cadastrar_livro.label_10.setText("")
        tela_cadastrar_livro.label_9.setText("Insira apena o ANO. Exemplo = (2011)")
    except:
        tela_cadastrar_livro.label_9.setText("Insira apena o ANO. Exemplo = (2011)")
        tela_cadastrar_livro.label_10.setText("")

def abrir_tela_excluir_livro():
    tela_livros.close()
    tela_excluir_livro.show()

def voltar_tela_excluir_livro():
    tela_excluir_livro.label_12.setText("")
    tela_excluir_livro.autor.setText("")
    tela_excluir_livro.livro.setText("")
    tela_excluir_livro.ano.setText("")
    tela_excluir_livro.ISBN.setText("")
    tela_excluir_livro.label_10.setText("")
    tela_excluir_livro.close()
    tela_livros.show()

def excluir_livro_pesq():
    tela_excluir_livro.label_12.setText("")
    tela_excluir_livro.label_10.setText("")
    achei = 0
    cursor = banco.cursor()
    comando_SQL = 'SELECT * FROM livros'
    cursor.execute(comando_SQL)
    isbn=tela_excluir_livro.ISBN.text()
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[0] == isbn:
            x = i[5]
            y = ''
            a = y + str(x)
            tela_excluir_livro.autor.setText(i[1])
            tela_excluir_livro.livro.setText(i[2])
            tela_excluir_livro.ano.setText(a)
            achei = 1
    if achei == 0:
        tela_excluir_livro.label_10.setText("ISBN não encontrada")
        tela_excluir_livro.autor.setText("")
        tela_excluir_livro.livro.setText("")
        tela_excluir_livro.ano.setText("")

def excluir_livro():
    isbn=tela_excluir_livro.ISBN.text()
    cursor = banco.cursor()
    comando_SQL2 = "DELETE FROM livros WHERE isbn = '{}'".format(isbn)
    cursor.execute(comando_SQL2)
    banco.commit()
    tela_excluir_livro.label_12.setText("")
    tela_excluir_livro.label_12.setText("Livro excluido com sucesso")
    tela_excluir_livro.autor.setText("")
    tela_excluir_livro.livro.setText("")
    tela_excluir_livro.ano.setText("")
    tela_excluir_livro.ISBN.setText("")
    
def abrir_tela_pesquisar_livro():
    tela_livros.close()
    tela_pesquisar_livro.show()

def voltar_tela_pesquisar_livro():
    tela_pesquisar_livro.label_15.setText("")
    tela_pesquisar_livro.ISBN.setText("")
    tela_pesquisar_livro.label_3.setText("")
    tela_pesquisar_livro.label_13.setText("")
    tela_pesquisar_livro.autor.setText("")
    tela_pesquisar_livro.livro.setText("")
    tela_pesquisar_livro.genero.setText("")
    tela_pesquisar_livro.editora.setText("")
    tela_pesquisar_livro.ano.setText("")
    tela_pesquisar_livro.close()
    tela_livros.show()

def pesquisar_livro():
    achei = 0
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM livros")
    isbn=tela_pesquisar_livro.ISBN.text()
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[0] == isbn:
            x = i[5]
            y = ''
            a = y + str(x)
            tela_pesquisar_livro.autor.setText(i[1])
            tela_pesquisar_livro.livro.setText(i[2])
            tela_pesquisar_livro.genero.setText(i[3])
            tela_pesquisar_livro.editora.setText(i[4])
            tela_pesquisar_livro.ano.setText(a)
            tela_pesquisar_livro.label_3.setText("")
            tela_pesquisar_livro.label_15.setText("Pesquisa realizada")
            achei = 1
    if achei == 0:
        tela_pesquisar_livro.label_15.setText("")
        tela_pesquisar_livro.autor.setText("")
        tela_pesquisar_livro.livro.setText("")
        tela_pesquisar_livro.genero.setText("")
        tela_pesquisar_livro.editora.setText("")
        tela_pesquisar_livro.ano.setText("")
        tela_pesquisar_livro.label_3.setText("ISBN não encontrado!")

def abrir_tela_funcionarios():
    sistema_geral.close()
    tela_funcionarios.show()

def voltar_tela_funcionarios():
    tela_funcionarios.close()
    sistema_geral.show()

def abrir_tela_listar_funcionarios():
    tela_funcionarios.close()
    tela_listar_funcionarios.show()
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM funcionario')
    dados_lidos=cursor.fetchall()
    tela_listar_funcionarios.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_funcionarios.tableWidget.setColumnCount(3)
    tela_listar_funcionarios.tableWidget.setColumnWidth(0, 55)
    tela_listar_funcionarios.tableWidget.setColumnWidth(1, 350)
    tela_listar_funcionarios.tableWidget.setColumnWidth(2, 120)
    tela_listar_funcionarios.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tela_listar_funcionarios.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_listar_funcionarios.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def voltar_tela_listar_funcionarios():
    tela_listar_funcionarios.close()
    tela_funcionarios.show()
    
def abrir_tela_editar_funcionario():
    tela_funcionarios.close()
    tela_editar_funcionario.show()

def voltar_tela_editar_funcionario():
    tela_editar_funcionario.label_2.setText("")
    tela_editar_funcionario.label_3.setText("")
    tela_editar_funcionario.cod.setText("")
    tela_editar_funcionario.turno.setText("")
    tela_editar_funcionario.close()
    tela_funcionarios.show()

def editar_funcionario():
    try:
        cod=int(tela_editar_funcionario.cod.text())
        turno=tela_editar_funcionario.turno.text()
        cursor = banco.cursor()
        comando_SQL = "UPDATE funcionario SET turno = %s WHERE cod_funcionario = %s"
        dados = (turno,cod)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        tela_editar_funcionario.label_2.setText("Alteração feitas com sucesso")
        tela_editar_funcionario.label_3.setText("")
        tela_editar_funcionario.cod.setText("")
        tela_editar_funcionario.turno.setText("")
    except ValueError:
        tela_editar_funcionario.label_3.setText("Código invalido")

def abrir_tela_cadastrar_funcionario():
    tela_funcionarios.close()
    tela_cadastrar_funcionario.show()

def voltar_tela_cadastrar_funcionario():
    tela_cadastrar_funcionario.label_7.setText("")
    tela_cadastrar_funcionario.label_8.setText("")
    tela_cadastrar_funcionario.nome.setText("")
    tela_cadastrar_funcionario.turno.setText("")
    tela_cadastrar_funcionario.label_4.setText("")
    tela_cadastrar_funcionario.close()
    tela_funcionarios.show()

def cadastrar_funcionario():
    try:
        nome=tela_cadastrar_funcionario.nome.text()
        turno=tela_cadastrar_funcionario.turno.text()
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO funcionario (nome_funcionario, turno) VALUES (%s,%s)"
        dados = (nome,turno)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        tela_cadastrar_funcionario.label_7.setText("")
        tela_cadastrar_funcionario.label_8.setText("")
        tela_cadastrar_funcionario.label_4.setText("Funcionário cadastrado com sucesso")
        tela_cadastrar_funcionario.nome.setText("")
        tela_cadastrar_funcionario.turno.setText("")
    except:
        tela_cadastrar_funcionario.label_7.setText("Parâmetro errado digite o turno dessa forma:")
        tela_cadastrar_funcionario.label_8.setText("(Vespertino, matutino e notruno)")
        tela_cadastrar_funcionario.turno.setText("")

def abrir_tela_excluir_funcionario():
    tela_funcionarios.close()
    tela_excluir_funcionario.show()

def voltar_tela_excluir_funcionario():
    tela_excluir_funcionario.nome.setText("")
    tela_excluir_funcionario.turno.setText("") 
    tela_excluir_funcionario.label_10.setText("")
    tela_excluir_funcionario.label_10.setText("")
    tela_excluir_funcionario.cod.setText("")
    tela_excluir_funcionario.close()
    tela_funcionarios.show()

def tela_excluir_funcionario_pesq():
    try:
        tela_excluir_funcionario.label_10.setText("")
        tela_excluir_funcionario.label_10.setText("")
        achei = 0
        cursor = banco.cursor()
        comando_SQL = 'SELECT * FROM funcionario'
        cursor.execute(comando_SQL)
        cod=int(tela_excluir_funcionario.cod.text())
        valores_lidos = cursor.fetchall()
        for i in valores_lidos:
            if i[0] == cod:
                tela_excluir_funcionario.nome.setText(i[1])
                tela_excluir_funcionario.turno.setText(i[2])
                achei = 1
        if achei == 0:
            tela_excluir_funcionario.label_10.setText("Código inválido")
            tela_excluir_funcionario.nome.setText("")
            tela_excluir_funcionario.turno.setText("") 
    except ValueError:
        tela_excluir_funcionario.label_10.setText("Insira apenas números inteiros")
    except:
        print("Pane geral")

def abrir_tela_pesquisar_funcionario():
    tela_funcionarios.close()
    tela_pesquisar_funcionario.show()

def voltar_tela_pesquisar_funcionario():
    tela_pesquisar_funcionario.cod.setText("")
    tela_pesquisar_funcionario.nomeresul.setText("")
    tela_pesquisar_funcionario.turno.setText("")
    tela_pesquisar_funcionario.label_15.setText("")
    tela_pesquisar_funcionario.label_3.setText("")
    tela_pesquisar_funcionario.label_15.setText("")
    tela_pesquisar_funcionario.nome.setText("")
    tela_pesquisar_funcionario.close()
    tela_funcionarios.show()

def pesquisar_funcionario():
    achei = 0
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM funcionario")
    nome=tela_pesquisar_funcionario.nome.text()
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
      if i[1] == nome:
          x = i[0]
          y = ''
          a = y + str(x)
          tela_pesquisar_funcionario.label_3.setText("")
          tela_pesquisar_funcionario.cod.setText(a)
          tela_pesquisar_funcionario.nomeresul.setText(i[1])
          tela_pesquisar_funcionario.turno.setText(i[2])
          tela_pesquisar_funcionario.label_15.setText("Pesquisa realizada")
          achei = 1
    if achei == 0:
        tela_pesquisar_funcionario.cod.setText("")
        tela_pesquisar_funcionario.nomeresul.setText("")
        tela_pesquisar_funcionario.turno.setText("")
        tela_pesquisar_funcionario.label_15.setText("")
        tela_pesquisar_funcionario.label_3.setText("Nome não encontrado")

def abrir_tela_emprestimo():
    sistema_geral.close()
    tela_emprestimo.show()

def voltar_tela_emprestimo():
    tela_emprestimo.close()
    sistema_geral.show()

def abrir_tela_opc():
    tela_emprestimo.close()
    tela_opc.show()

def voltar_tela_opc():
    tela_opc.close()
    tela_emprestimo.show()

def abrir_tela_listar_emprestimo():
    tela_opc.close()
    tela_listar_emprestimo.show()
    cursor = banco.cursor()
    cursor.execute('SELECT cod_emprestimo, datetime_emprestimo, previ_entrega, ISBN, cod_funcionario, aluno_matricula FROM emprestimo;')
    dados_lidos=cursor.fetchall()
    
    tela_listar_emprestimo.tableWidget.setRowCount(len(dados_lidos))
    
    tela_listar_emprestimo.tableWidget.setColumnCount(6)
    tela_listar_emprestimo.tableWidget.setColumnWidth(0, 68)
    tela_listar_emprestimo.tableWidget.setColumnWidth(1, 210)
    tela_listar_emprestimo.tableWidget.setColumnWidth(2, 150)
    tela_listar_emprestimo.tableWidget.setColumnWidth(3, 270)
    tela_listar_emprestimo.tableWidget.setColumnWidth(4, 250)
    tela_listar_emprestimo.tableWidget.setColumnWidth(5, 140)
    tela_listar_emprestimo.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tela_listar_emprestimo.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    for p in dados_lidos:
        for j in range(0, 1):
            tela_listar_emprestimo.tableWidget.setItem(p,j,QtWidgets.QTableWidgetItem(str(dados_lidos[p][j])))




    #for i in range(0, len(dados_lidos)):
     #       for j in range(0, 6):
       #         tela_listar_emprestimo.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    

    
    
    
    

   

    

def voltar_tela_listar_emprestimo():
    tela_listar_emprestimo.close()
    tela_emprestimo.show()








app=QtWidgets.QApplication([])

#Carregando os arquivos
login_entrar=uic.loadUi("login.ui")
sistema_geral=uic.loadUi("sistema_geral.ui")
tela_cadastro=uic.loadUi("tela_cadastro.ui")
alunos_a=uic.loadUi("alunos.ui")
listar_alunos=uic.loadUi("listar_alunos.ui")
tela_editar_aluno=uic.loadUi("tela_editar_aluno.ui")
tela_cadastrar_aluno=uic.loadUi("tela_cadastrar_aluno.ui")
tela_excluir_aluno=uic.loadUi("tela_excluir_aluno.ui")
tela_pesquisar_aluno=uic.loadUi("tela_pesquisar_aluno.ui")
tela_livros=uic.loadUi("tela_livros.ui")
adm_cadastro=uic.loadUi("adm_cadastro.ui")
tela_listar_livros=uic.loadUi("tela_listar_livros.ui")
tela_editar_livro=uic.loadUi("tela_editar_livro.ui")
tela_cadastrar_livro=uic.loadUi("tela_cadastrar_livro.ui")
tela_excluir_livro=uic.loadUi("tela_excluir_livro.ui")
tela_pesquisar_livro=uic.loadUi("tela_pesquisar_livro.ui")
tela_funcionarios=uic.loadUi("tela_funcionarios.ui")
tela_listar_funcionarios=uic.loadUi("tela_listar_funcionarios.ui")
tela_editar_funcionario=uic.loadUi("tela_editar_funcionario.ui")
tela_cadastrar_funcionario=uic.loadUi("tela_cadastrar_funcionario.ui")
tela_excluir_funcionario=uic.loadUi("tela_excluir_funcionario.ui")
tela_pesquisar_funcionario=uic.loadUi("tela_pesquisar_funcionario.ui")
tela_emprestimo=uic.loadUi("tela_emprestimo.ui")
tela_opc=uic.loadUi("opc_listar.ui")
tela_listar_emprestimo=uic.loadUi("tela_listar_emprestimo.ui")


#Execultando as funções de clicker
adm_cadastro.pushButton_7.clicked.connect(voltar_adm_cadastro)
login_entrar.pushButton.clicked.connect(chama_sistema_geral)
login_entrar.pushButton_3.clicked.connect(sair_geral)
sistema_geral.pushButton.clicked.connect(logout)
login_entrar.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
login_entrar.pushButton_2.clicked.connect(tela_adm_cadastro)
adm_cadastro.pushButton.clicked.connect(login_adm)
tela_cadastro.pushButton.clicked.connect(cadastrar)
tela_cadastro.pushButton_7.clicked.connect(voltar_login_entrar)
sistema_geral.pushButton_2.clicked.connect(alunos)
alunos_a.pushButton_7.clicked.connect(voltar_sistema_geral)
alunos_a.pushButton_2.clicked.connect(abre_listar_alunos)
listar_alunos.pushButton.clicked.connect(voltar_listar_alunos)
alunos_a.pushButton_4.clicked.connect(abrir_tela_editar_aluno)
tela_editar_aluno.pushButton.clicked.connect(editar_aluno)
tela_editar_aluno.pushButton_7.clicked.connect(voltar_editar_aluno)
alunos_a.pushButton_3.clicked.connect(abrir_tela_cadastrar_alunos)
tela_cadastrar_aluno.pushButton_4.clicked.connect(cadastrar_aluno)
tela_cadastrar_aluno.pushButton_3.clicked.connect(voltar_cadastrar_aluno)
alunos_a.pushButton_6.clicked.connect(abrir_tela_excluir_aluno)
tela_excluir_aluno.pushButton_3.clicked.connect(voltar_excluir_aluno)
tela_excluir_aluno.pushButton_4.clicked.connect(excluir_aluno_pesq)
tela_excluir_aluno.pushButton_2.clicked.connect(excluir_aluno)
alunos_a.pushButton_5.clicked.connect(abrir_tela_pesquisar_aluno)
tela_pesquisar_aluno.pushButton_7.clicked.connect(voltar_pesquisar_aluno)
tela_pesquisar_aluno.pushButton_4.clicked.connect(pesquisar_aluno)
sistema_geral.pushButton_3.clicked.connect(abrir_tela_livros)
tela_livros.pushButton_7.clicked.connect(voltar_tela_livros)
tela_livros.pushButton_2.clicked.connect(abrir_tela_listar_livros)
tela_listar_livros.pushButton.clicked.connect(voltar_tela_listar_livros)
tela_livros.pushButton_4.clicked.connect(abrir_tela_editar_livros)
tela_editar_livro.pushButton_7.clicked.connect(voltar_tela_editar_livro)
tela_editar_livro.pushButton.clicked.connect(isbn_editar)
tela_livros.pushButton_3.clicked.connect(abrir_tela_cadastrar_livro)
tela_cadastrar_livro.pushButton_3.clicked.connect(voltar_tela_cadastrar_livros)
tela_cadastrar_livro.pushButton.clicked.connect(isbn_cadastrar)
tela_livros.pushButton_6.clicked.connect(abrir_tela_excluir_livro)
tela_excluir_livro.pushButton_3.clicked.connect(voltar_tela_excluir_livro)
tela_excluir_livro.pushButton_4.clicked.connect(excluir_livro_pesq)
tela_excluir_livro.pushButton_2.clicked.connect(excluir_livro)
tela_livros.pushButton_5.clicked.connect(abrir_tela_pesquisar_livro)
tela_pesquisar_livro.pushButton_7.clicked.connect(voltar_tela_pesquisar_livro)
tela_pesquisar_livro.pushButton_4.clicked.connect(pesquisar_livro)
sistema_geral.pushButton_5.clicked.connect(abrir_tela_funcionarios)
tela_funcionarios.pushButton_7.clicked.connect(voltar_tela_funcionarios)
tela_funcionarios.pushButton_2.clicked.connect(abrir_tela_listar_funcionarios)
tela_listar_funcionarios.pushButton.clicked.connect(voltar_tela_listar_funcionarios)
tela_funcionarios.pushButton_4.clicked.connect(abrir_tela_editar_funcionario)
tela_editar_funcionario.pushButton_7.clicked.connect(voltar_tela_editar_funcionario)
tela_editar_funcionario.pushButton.clicked.connect(editar_funcionario)
tela_funcionarios.pushButton_3.clicked.connect(abrir_tela_cadastrar_funcionario)
tela_cadastrar_funcionario.pushButton_7.clicked.connect(voltar_tela_cadastrar_funcionario)
tela_cadastrar_funcionario.pushButton.clicked.connect(cadastrar_funcionario)
tela_funcionarios.pushButton_6.clicked.connect(abrir_tela_excluir_funcionario)
tela_excluir_funcionario.pushButton_3.clicked.connect(voltar_tela_excluir_funcionario)
tela_excluir_funcionario.pushButton_4.clicked.connect(tela_excluir_funcionario_pesq)
tela_funcionarios.pushButton_5.clicked.connect(abrir_tela_pesquisar_funcionario)
tela_pesquisar_funcionario.pushButton_7.clicked.connect(voltar_tela_pesquisar_funcionario)
tela_pesquisar_funcionario.pushButton_4.clicked.connect(pesquisar_funcionario)
sistema_geral.pushButton_4.clicked.connect(abrir_tela_emprestimo)
tela_emprestimo.pushButton_7.clicked.connect(voltar_tela_emprestimo)
tela_emprestimo.pushButton_2.clicked.connect(abrir_tela_opc)
tela_opc.pushButton.clicked.connect(voltar_tela_opc)
tela_opc.pushButton_1.clicked.connect(abrir_tela_listar_emprestimo)
tela_listar_emprestimo.pushButton.clicked.connect(voltar_tela_listar_emprestimo)


#IconesDeLogin
login_entrar.setWindowIcon(QtGui.QIcon('icone.png'))
sistema_geral.setWindowIcon(QtGui.QIcon('icone.png'))
tela_cadastro.setWindowIcon(QtGui.QIcon('icone.png'))
alunos_a.setWindowIcon(QtGui.QIcon('icone.png'))
listar_alunos.setWindowIcon(QtGui.QIcon('icone.png'))
tela_editar_aluno.setWindowIcon(QtGui.QIcon('icone.png'))
tela_cadastrar_aluno.setWindowIcon(QtGui.QIcon('icone.png'))
tela_excluir_aluno.setWindowIcon(QtGui.QIcon('icone.png'))
tela_pesquisar_aluno.setWindowIcon(QtGui.QIcon('icone.png'))
tela_livros.setWindowIcon(QtGui.QIcon('icone.png'))
adm_cadastro.setWindowIcon(QtGui.QIcon('icone.png'))
tela_listar_livros.setWindowIcon(QtGui.QIcon('icone.png'))
tela_editar_livro.setWindowIcon(QtGui.QIcon('icone.png'))
tela_cadastrar_livro.setWindowIcon(QtGui.QIcon('icone.png'))
tela_excluir_livro.setWindowIcon(QtGui.QIcon('icone.png'))
tela_pesquisar_livro.setWindowIcon(QtGui.QIcon('icone.png'))
tela_funcionarios.setWindowIcon(QtGui.QIcon('icone.png'))
tela_listar_funcionarios.setWindowIcon(QtGui.QIcon('icone.png'))
tela_editar_funcionario.setWindowIcon(QtGui.QIcon('icone.png'))
tela_cadastrar_funcionario.setWindowIcon(QtGui.QIcon('icone.png'))
tela_excluir_funcionario.setWindowIcon(QtGui.QIcon('icone.png'))
tela_pesquisar_funcionario.setWindowIcon(QtGui.QIcon('icone.png'))
tela_emprestimo.setWindowIcon(QtGui.QIcon('icone.png'))
tela_opc.setWindowIcon(QtGui.QIcon('icone.png'))

#Start

login_entrar.show()
app.exec()

