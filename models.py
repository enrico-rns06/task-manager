class Tarefa:

    def __init__(self, nome, importancia, concluida=False):
        self.nome = nome
        self.importancia = importancia
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def editar(self, novo_nome=None, nova_importancia=None):
        if novo_nome is not None:
            self.nome = novo_nome
        if nova_importancia is not None:
            self.importancia = nova_importancia

    def to_dict(self):
        return {
            "Nome": self.nome,
            "Importancia": self.importancia,
            "Concluida": self.concluida
        }

    @staticmethod
    def from_dict(dados):
        return Tarefa(
            nome=dados["Nome"],
            importancia=dados["Importancia"],
            concluida=dados["Concluida"]
        )