class Cores:
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    AZUL = '\033[94m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    VERDE = '\033[92m'   
    VERMELHO = '\033[91m' 


class Interface:
    
    @staticmethod
    def limpar_ecra():
        print("\n" * 1)
    
    @staticmethod
    def exibir_titulo():
        M = Cores.MAGENTA + Cores.BOLD
        C = Cores.CIANO
        B = Cores.AZUL + Cores.BOLD
        R = Cores.RESET
        
        print(f"{C}╔═══════════════════════════════════════════════════════════════════════════╗{R}")
        print(f"{C}║                                                                           ║{R}")
        print(f"{C}║        {M}█████╗      ██████╗  █████╗ ██████╗ ██╗████████╗ █████╗ ██         {R}{C}║{R}")
        print(f"{C}║       {M}██╔══██╗    ██╔════╝ ██╔══██╗██╔══██╗██║╚══██╔══╝██╔══██╗██║        {R}{C}║{R}")
        print(f"{C}║       {M}███████║    ██║      ███████║██████╔╝██║   ██║   ███████║██║        {R}{C}║{R}")
        print(f"{C}║       {M}██╔══██║    ██║      ██╔══██║██╔═══╝ ██║   ██║   ██╔══██║██║        {R}{C}║{R}")
        print(f"{C}║       {M}██║  ██║    ╚██████╗ ██║  ██║██║     ██║   ██║   ██║  ██║███████╗   {R}{C}║{R}")
        print(f"{C}║       {M}╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   {R}{C}║{R}")
        print(f"{C}║                                                                           ║{R}")
        print(f"{C}║                {M}██████╗███████╗██████╗ ████████╗ █████╗                    {R}{C}║{R}")
        print(f"{C}║               {M}██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗                   {R}{C}║{R}")
        print(f"{C}║               {M}██║     █████╗  ██████╔╝   ██║   ███████║                   {R}{C}║{R}")
        print(f"{C}║               {M}██║     ██╔══╝  ██╔══██╗   ██║   ██╔══██║                   {R}{C}║{R}")
        print(f"{C}║               {M}╚██████╗███████╗██║  ██║   ██║   ██║  ██║                   {R}{C}║{R}")
        print(f"{C}║                {M}╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                   {R}{C}║{R}")
        print(f"{C}║                                                                           ║{R}")
        print(f"{C}║                     {B}🌍  Capitais Europeias  🌍{R}{C}                            ║{R}")
        print(f"{C}║                                                                           ║{R}")
        print(f"{C}╚═══════════════════════════════════════════════════════════════════════════╝{R}")
        print()
    
    @staticmethod
    def exibir_menu():
        print("MENU".center(70))
        print()
        print("1.Jogar Quiz")
        print("2.Ver Histórico de Jogos")
        print("3.Sair")
        print()
        
        return input("Escolha uma opção: ")

    @staticmethod
    def mostrar_feedback(resposta_certa,pontos,pontuacao_total):
        if resposta_certa:
            print(f"\n{Cores.VERDE} CORRETO! Parabéns!{Cores.RESET}")
            print(f"Pontos ganhos: {pontos} pts")
        else:
            print(f"\n{Cores.VERMELHO} ERRADO!{Cores.RESET}")
            print(f"Pontos ganhos: 0 pts")
        print(f"Pontuação acumulada: {pontuacao_total} pts")
    @staticmethod
    def ascii_art_resultado(percentagem):
        
        if percentagem >= 90:
            print("""
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║        🏆  EXCELENTE!  🏆             ║
    ║                                       ║
    ║          É um EXPERT em               ║
    ║        Geografia Europeia!            ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
            """)

        elif percentagem >= 70:
            print("""
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║        ⭐  MUITO BOM!  ⭐             ║
    ║                                       ║
    ║       Conhece bem as capitais         ║
    ║             europeias!                ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
            """)
        
        elif percentagem >= 50:
            print("""
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║        👍  BOM TRABALHO!  👍          ║
    ║                                       ║
    ║          Continue estudando!          ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
            """)

        else:
            print("""
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║        📚  NÃO DESISTA!  📚           ║
    ║                                       ║
    ║         Continue praticando!          ║
    ║       A geografia é desafiante!       ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
            """)