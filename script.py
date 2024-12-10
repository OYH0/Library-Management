# Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"'{self.titulo}' por {self.autor} (Publicado em {self.ano_publicacao}) [{status}]"

# Classe Usuario
class Usuario:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            return True
        return False

    def __str__(self):
        livros = ", ".join(livro.titulo for livro in self.livros_emprestados) or "nenhum livro emprestado"
        return f"{self.nome} (Matrícula: {self.matricula}, Idade: {self.idade}) - Livros emprestados: {livros}"

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, titulo, autor, ano_publicacao):
        novo_livro = Livro(titulo, autor, ano_publicacao)
        self.livros.append(novo_livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    def cadastrar_usuario(self, nome, idade, matricula):
        novo_usuario = Usuario(nome, idade, matricula)
        self.usuarios.append(novo_usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso!")

    def emprestar_livro(self, matricula, titulo_livro):
        usuario = next((u for u in self.usuarios if u.matricula == matricula), None)
        livro = next((l for l in self.livros if l.titulo == titulo_livro), None)
        if usuario and livro:
            if usuario.emprestar_livro(livro):
                return f"Livro '{titulo_livro}' emprestado para {usuario.nome}. Aproveite a leitura!"
            else:
                return f"Desculpe, o livro '{titulo_livro}' não está disponível no momento."
        return "Usuário ou livro não encontrado. Verifique as informações fornecidas."

    def devolver_livro(self, matricula, titulo_livro):
        usuario = next((u for u in self.usuarios if u.matricula == matricula), None)
        livro = next((l for l in self.livros if l.titulo == titulo_livro), None)
        if usuario and livro:
            if usuario.devolver_livro(livro):
                return f"Obrigado, {usuario.nome}! O livro '{titulo_livro}' foi devolvido com sucesso."
            else:
                return f"O livro '{titulo_livro}' não estava registrado como emprestado para {usuario.nome}."
        return "Usuário ou livro não encontrado. Verifique as informações fornecidas."

    def livros_disponiveis(self):
        return [livro for livro in self.livros if livro.disponivel]

    def usuarios_com_livros(self):
        return [usuario for usuario in self.usuarios if usuario.livros_emprestados]

    def exibir_relatorio_livros_disponiveis(self):
        disponiveis = self.livros_disponiveis()
        if disponiveis:
            return "\n".join(str(livro) for livro in disponiveis)
        return "Nenhum livro disponível no momento."

    def exibir_relatorio_usuarios_com_livros(self):
        usuarios = self.usuarios_com_livros()
        if usuarios:
            relatorio = []
            for usuario in usuarios:
                livros = ", ".join(livro.titulo for livro in usuario.livros_emprestados)
                relatorio.append(f"{usuario.nome} tem emprestado: {livros}")
            return "\n".join(relatorio)
        return "Nenhum usuário possui livros emprestados no momento."

# Exemplo de uso do sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Cadastrando livros
    biblioteca.cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    biblioteca.cadastrar_livro("1984", "George Orwell", 1949)

    # Cadastrando usuários
    biblioteca.cadastrar_usuario("Alice", 30, 1)
    biblioteca.cadastrar_usuario("Bob", 25, 2)

    # Empréstimos
    print(biblioteca.emprestar_livro(1, "1984"))
    print(biblioteca.emprestar_livro(2, "O Senhor dos Anéis"))
    print(biblioteca.emprestar_livro(1, "O Senhor dos Anéis"))

    # Relatórios
    print("\nLivros disponíveis:")
    print(biblioteca.exibir_relatorio_livros_disponiveis())

    print("\nUsuários com livros emprestados:")
    print(biblioteca.exibir_relatorio_usuarios_com_livros())

    # Devolução
    print(biblioteca.devolver_livro(2, "O Senhor dos Anéis"))

    # Relatório final
    print("\nLivros disponíveis:")
    print(biblioteca.exibir_relatorio_livros_disponiveis())
    print("\nUsuários com livros emprestados:")
    print(biblioteca.exibir_relatorio_usuarios_com_livros())
