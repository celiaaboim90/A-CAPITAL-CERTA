class NivelJogo:

    def __init__(self, nome:str, regiao_geografica:str, num_perguntas:int, tem_ajuda_50_50=True, num_ajudas=3):
        self.nome = nome
        self.regiao_geografica = regiao_geografica
        self.num_perguntas = num_perguntas
        self.tem_ajuda_50_50 = tem_ajuda_50_50
        self.num_ajudas = num_ajudas if tem_ajuda_50_50 else 0
    
    def obter_configuracao(self):
        return {
            "nome": self.nome,
            "regiao_geografica": self.regiao_geografica,
            "num_perguntas": self.num_perguntas,
            "tem_ajuda": self.tem_ajuda_50_50,
            "num_ajudas": self.num_ajudas
        }
    
    def __str__(self):
        info_num_ajudas = f"com {self.num_ajudas} ajudas 50/50" if self.tem_ajuda_50_50 else "sem ajudas"
        return f"{self.nome} - {self.num_perguntas} perguntas ({info_num_ajudas})"



NIVEL_FACIL = NivelJogo(
    nome="Fácil",
    regiao_geografica="europa_ocidental",
    num_perguntas=21,
    tem_ajuda_50_50=True,
    num_ajudas=3
)

NIVEL_INTERMEDIO = NivelJogo(
    nome="Intermédio",
    regiao_geografica="europa_oriental",
    num_perguntas=26,
    tem_ajuda_50_50=True,
    num_ajudas=3
)

NIVEL_DIFICIL = NivelJogo(
    nome="Difícil",
    regiao_geografica="europa_completa",
    num_perguntas=47,
    tem_ajuda_50_50=False,
    num_ajudas=0
)

NIVEIS_DISPONIVEIS = {
    "1": NIVEL_FACIL,
    "2": NIVEL_INTERMEDIO,
    "3": NIVEL_DIFICIL
}