import json
class CapitaisJogo:
    def __init__ (self,capitais_europa_ocidental={},capitais_europa_oriental={},capitais_europa_completa={}):
        self.capitais_europa_ocidental=capitais_europa_ocidental
        self.capitais_europa_oriental=capitais_europa_oriental
        self.capitais_europa_completa=capitais_europa_completa

    @staticmethod
    def deserializar() -> dict:
        try:
            with open ('capitais.json','r',encoding='utf-8') as f:
                dados=json.load(f)
        except FileNotFoundError:
            print("Erro.Ficheiro Json não encontrado.")
            return {}
        return dados
    
    @classmethod
    def init_pelo_json(cls):
        try:
            dados=CapitaisJogo.deserializar()
            capitais_europa_ocidental=dados.get("europa_ocidental",{})
            capitais_europa_oriental=dados.get("europa_oriental",{})
            capitais_europa_completa=dados.get("europa_completa",{})
            return cls(capitais_europa_ocidental,capitais_europa_oriental,capitais_europa_completa)
        
      
        except Exception as e:
            print("Erro ao deserializar capitais:{e}")
        raise
             
    def obter_total_paises(self,regiao_geografica):
        total_de_paises = 0
        if regiao_geografica =="europa_ocidental":
            total_de_paises = len(self.capitais_europa_ocidental)
        elif regiao_geografica =="europa_oriental":
            total_de_paises = len(self.capitais_europa_oriental)
        else:
            total_de_paises = len(self.capitais_europa_completa)
        return total_de_paises 
    







