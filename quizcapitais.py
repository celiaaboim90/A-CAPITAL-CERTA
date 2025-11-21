import random
from nivelJogo import NIVEIS_DISPONIVEIS
from capitaisjogo import CapitaisJogo
from interface import Interface
from historicojogo import HistoricoJogo

class QuizCapitais:
    def __init__(self):

        self.gestor_capitais = CapitaisJogo.init_pelo_json()
        self.historico_jogo = HistoricoJogo()
        self.interface = Interface()
        self.nivel_atual=None
        self.total_perguntas=0
        self.ajudas_disponiveis=0
        self.historico_respostas=[]
        self.dados_do_jogo={}
        self.pontuacao=0
        self.pontos_por_resposta_correta=100
        self.penalizacao_ajuda=30
        
    def escolher_nivel(self):
        print("ESCOLHA O NÍVEL DE DIFICULDADE:")
        print("1.Fácil - Europa Ocidental".center(70))
        print (f"         {self.gestor_capitais.obter_total_paises('europa_ocidental')} países" 
               f"         {NIVEIS_DISPONIVEIS['1'].num_perguntas} perguntas" 
               f"         {NIVEIS_DISPONIVEIS['1'].num_ajudas} ajudas 50/50")
        print()
        print("2.Intermédio - Europa Oriental".center(70))
        print (f"         {self.gestor_capitais.obter_total_paises('europa_oriental')} países" 
               f"         {NIVEIS_DISPONIVEIS['2'].num_perguntas} perguntas" 
               f"         {NIVEIS_DISPONIVEIS['2'].num_ajudas} ajudas 50/50")
        print() 
        print("3.Difícil - Europa Completa".center(70))
        print (f"         {self.gestor_capitais.obter_total_paises('europa_completa')} países" 
               f"         {NIVEIS_DISPONIVEIS['3'].num_perguntas} perguntas" 
               f"         Sem ajudas 50/50")
        print()

        while True:
            escolha=input("Escolha o nível que quer jogar (1,2,3):")
            if escolha in NIVEIS_DISPONIVEIS:
                self.nivel_atual = NIVEIS_DISPONIVEIS[escolha]
                self.ajudas_disponiveis=self.nivel_atual.num_ajudas
                if self.nivel_atual.regiao_geografica == "europa_ocidental":
                    self.capitais_jogo = self.gestor_capitais.capitais_europa_ocidental
                elif self.nivel_atual.regiao_geografica == "europa_oriental":
                    self.capitais_jogo = self.gestor_capitais.capitais_europa_oriental
                else: 
                    self.capitais_jogo = self.gestor_capitais.capitais_europa_completa
                print(f"Nível {self.nivel_atual.nome} selecionado!")
                return self.nivel_atual
            else:
                print("Erro.Opção inválida!Digite 1,2 ou 3")

    def selecionar_perguntas(self):
        paises_disponiveis=list(self.capitais_jogo)
        num_perguntas=len(paises_disponiveis)
        return random.sample(paises_disponiveis,num_perguntas)
     
    def gerar_opcoes(self,pais_correto):
        capital_certa=self.capitais_jogo[pais_correto]
        outras_capitais=[]
        for pais,capital in self.capitais_jogo.items():
            if pais!= pais_correto:
                outras_capitais.append(capital)

        opcoes_erradas = random.sample(outras_capitais,3)
        opcoes = opcoes_erradas + [capital_certa]
        random.shuffle(opcoes)
        return opcoes
      
    def usar_ajuda_50_50 (self,opcoes,resposta_correta):
        opcoes_erradas=[]
        for opcao in opcoes:
            if opcao!= resposta_correta:
                opcoes_erradas.append(opcao)
    
        opcoes_a_remover=random.sample(opcoes_erradas,2)
        opcoes_finais=[]
        for opcao in opcoes:
            if opcao not in opcoes_a_remover:
                opcoes_finais.append(opcao)
        return opcoes_finais

    def fazer_pergunta(self, numero_pergunta, pais):
        usou_ajuda = False
        opcoes = self.gerar_opcoes(pais)
        opcoes_originais = opcoes.copy() 
        opcoes_ativas = opcoes.copy() 
        resposta_correta = self.capitais_jogo[pais]
        nivel_com_ajuda = self.nivel_atual.tem_ajuda_50_50
        print(f"\n--- Pergunta {numero_pergunta}/{self.total_perguntas} ---")
        print(f"Qual é a capital de {pais}?")

        while True:
       
            print("\nOpções:")
            for i, opcao in enumerate(opcoes_originais, 1):
                if opcao in opcoes_ativas:
                    print(f"{i}. {opcao}")
                else:
                    print(f"{i}. (Eliminada)")
            if nivel_com_ajuda and self.ajudas_disponiveis > 0 and not usou_ajuda:
                print("5. Ajuda 50/50")
        
            resposta = input("Digite o número da resposta: ")

            if resposta == '5':
                if nivel_com_ajuda and self.ajudas_disponiveis > 0 and not usou_ajuda:
                    self.ajudas_disponiveis -= 1
                    usou_ajuda = True
                    print("--- Ajuda 50/50 ! ---")
                    opcoes_ativas = self.usar_ajuda_50_50(opcoes_ativas, resposta_correta)
                    continue

                elif usou_ajuda:
                    print("Já usou a ajuda 50/50 nesta pergunta!" \
                    "Infelizmente,as regras só permitem uma ajuda por pergunta."\
                    "Digite a sua resposta:")
                    continue
                elif nivel_com_ajuda and self.ajudas_disponiveis == 0:
                    print("Ajudas 50/50 esgotadas !")
                    continue
                else:
                    print("Ajuda indisponível !")
                continue
            if resposta.isdigit():
                num = int(resposta)
                if 1 <= num <= len(opcoes_originais): 
                    opcao_escolhida = opcoes_originais[num - 1]
                    if opcao_escolhida in opcoes_ativas: 
                        return opcao_escolhida, usou_ajuda
                    else:
                        print("Essa opção foi eliminada! Responda novamente.")
                else:
                    max_opcao = 5 if (nivel_com_ajuda and self.ajudas_disponiveis > 0 and not usou_ajuda) else 4
                    print(f"Número inválido! Deve escolher entre 1 e {max_opcao}.")
            else:
                if nivel_com_ajuda and self.ajudas_disponiveis > 0 and not usou_ajuda:
                    print("Resposta inválida! Digite apenas o número da opção (1-4, ou 5).")
                else:
                    print("Resposta inválida! Digite apenas o número da opção (1-4).")
                continue  
    
    def verificar_resposta(self, pais, resposta_utilizador):
        resposta_correta = self.capitais_jogo[pais]
        esta_correto = (resposta_utilizador == resposta_correta)
        resposta=(esta_correto,resposta_utilizador)
        return resposta
    
    def calcular_pontos(self, correta, usou_ajuda):
        if not correta:
            return 0
        
        pontos = self.pontos_por_resposta_correta
        if usou_ajuda:
            pontos -= self.penalizacao_ajuda
        return max(pontos, 0)
    
    def mostrar_resultado_final(self): 
        self.interface.limpar_ecra()
        quantidade_respostas_certas = 0
        for resposta in self.historico_respostas:
            if resposta["correto"]:
                quantidade_respostas_certas += 1
        percentagem = (quantidade_respostas_certas / self.total_perguntas )* 100 if self.total_perguntas > 0 else 0
        pontos_maximos = self.total_perguntas * self.pontos_por_resposta_correta
        self.interface.ascii_art_resultado(percentagem)
        print(" RESULTADO FINAL".center(70))
        print(f" Nível: {self.nivel_atual.nome}")
        print(f" Pontuação Total: {self.pontuacao} pts (de {pontos_maximos} possíveis)")
        print(f" Respostas Corretas: {quantidade_respostas_certas}/{self.total_perguntas}")
        print(f" Percentagem de respostas certas: {percentagem:.1f}%")
        
        if self.nivel_atual.tem_ajuda_50_50:
            ajudas_usadas = self.nivel_atual.num_ajudas - self.ajudas_disponiveis
            print(f" Ajudas 50/50 utilizadas: {ajudas_usadas}/{self.nivel_atual.num_ajudas}")
        else:
            print(f" Nível sem ajudas")
        
        self.mostrar_historico_sessao()
        self.guardar_jogo_atual()
    
    def mostrar_historico_sessao(self):
        print(" Histórico de Respostas:")
     
        for i, registo in enumerate(self.historico_respostas, 1):
            status = " CORRETO" if registo["correto"] else " ERRADO"
            pontos = registo.get("pontos", 0)
            borda_status = "="*60
            print(borda_status)
            print(f"{i:2d}. País: {registo['pais']}")
            print("-"*60)
            print(f"Resposta do utilizador : {registo['resposta_utilizador']}")
            print(f"Resultado              :{status}")
            print(f"Pontos                 : {pontos}")
            if not registo["correto"]:
                print(f"Resposta correta       : {registo['resposta_correta']}")
                print(borda_status + "\n")
                print("="*60 + "\n")
            print()

    def guardar_jogo_atual(self):
        quantidade_respostas_certas = 0
        for resposta in self.historico_respostas:
            if resposta["correto"]:
                quantidade_respostas_certas += 1
        ajudas_usadas = self.nivel_atual.num_ajudas - self.ajudas_disponiveis
        
        dados_do_jogo = {
            "nivel": self.nivel_atual.nome,
            "regiao": self.nivel_atual.regiao_geografica,
            "pontuacao": self.pontuacao,
            "quantidade_respostas_certas": quantidade_respostas_certas,
            "total_perguntas": self.total_perguntas,
            "percentagem": round((quantidade_respostas_certas / self.total_perguntas )*100, 1) if self.total_perguntas > 0 else 0,
            "ajudas_usadas": ajudas_usadas if self.nivel_atual.tem_ajuda_50_50 else None,
            "respostas": self.historico_respostas
        }
        
        self.historico_jogo.guardar_jogo_atual(dados_do_jogo)
    
    def iniciar_quiz(self):
        self.interface.limpar_ecra()
        self.interface.exibir_titulo()
        self.escolher_nivel()
        print()
        print(" Sistema de Pontuação:")
        print(f"  • Resposta correta: {self.pontos_por_resposta_correta} pontos")
        
        if self.nivel_atual.tem_ajuda_50_50:
            print(f"  • Penalização por ajuda 50/50: -{self.penalizacao_ajuda} pontos")
            print(f"  • Ajudas disponíveis: {self.ajudas_disponiveis}")
        else:
            print(f"  •  Nível DIFÍCIL: SEM ajudas 50/50!")
        print()
        print(f"Prepare-se para responder a {self.nivel_atual.num_perguntas} perguntas!")
        print()
        input("Pressione Enter para começar")
        
        paises = self.selecionar_perguntas()
        self.total_perguntas = len(paises)
        for i, pais in enumerate(paises, 1):

            self.interface.limpar_ecra()

            resposta_utilizador,usou_ajuda=self.fazer_pergunta(i,pais)

            correto,resposta_correta = self.verificar_resposta(pais, resposta_utilizador)

            pontos = self.calcular_pontos(correto, usou_ajuda)
            
            self.interface.mostrar_feedback(correto, pontos,self.pontuacao)
            
            if correto:
                self.pontuacao += pontos
            else:
                print(f"A capital de {pais} é {resposta_correta}.")
            
            self.historico_respostas.append({
                "pais": pais,
                "resposta_utilizador": resposta_utilizador,
                "resposta_correta": resposta_correta,
                "correto": correto,
                "pontos": pontos,
                "usou_ajuda": usou_ajuda
            })
            print()
            input("Pressione Enter para continuar...")
        
        self.mostrar_resultado_final()
    
    def regressar_zero(self): 
        self.nivel_atual = None
        self.capitais_jogo = {}
        self.pontuacao = 0
        self.total_perguntas = 0
        self.historico_respostas = []
        self.ajudas_disponiveis = 0

    
     