import json
import os
from datetime import datetime

class HistoricoJogo:
    
    def __init__(self, arquivo_historico="historico_jogos.json"):
       self.arquivo_historico = arquivo_historico
    

    def carregar_historico(self):
        if os.path.exists(self.arquivo_historico):
            try:
                with open(self.arquivo_historico, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def guardar_jogo_atual(self, dados_do_jogo):
        historico = self.carregar_historico()
        
        if "data" not in dados_do_jogo:
            dados_do_jogo["data"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        historico.append(dados_do_jogo)
        
        with open(self.arquivo_historico, 'w', encoding='utf-8') as f:
            json.dump(historico, f, ensure_ascii=False, indent=4)
        
        print("Jogo guardado no histórico!")
    
    def ver_historico(self, limite=10):
        historico = self.carregar_historico()
        if not historico:
            print("Ainda não há jogos no histórico!")
            return
        
        print("HISTÓRICO DE JOGOS".center(70))
        
        
        for i, jogo in enumerate(historico[-limite:], 1):
            print(f"{i}. {jogo.get('data', 'N/A')} | Nível: {jogo.get('nivel', 'N/A')}")
            print(f"   Pontuação: {jogo.get('pontuacao', 0)} pts | ")
            print(f"   Número de respostas certas: {jogo.get('quantidade_respostas_certas', 0)}/{jogo.get('total_perguntas', 0)} ")
            print(f"   {jogo.get('percentagem', 0)}%")
            if jogo.get('ajudas_usadas') is not None:
                print(f"   Ajudas usadas: {jogo.get('ajudas_usadas', 0)}")
            print()

  
        
