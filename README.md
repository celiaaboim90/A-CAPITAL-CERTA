https://github.com/celiaaboim90/A-CAPITAL-CERTA
  
  🌍 A CAPITAL CERTA

**Jogo de quiz interativo sobre as capitais da Europa!**

Teste os seus conhecimentos de geografia europeia através de um quiz divertido com diferentes níveis de dificuldade. Será que consegue acertar todas as capitais?

---

## 📋 Sobre o Projeto

**A Capital Certa** é um jogo educativo desenvolvido em Python que desafia os jogadores a identificarem corretamente as capitais dos países europeus. Com diferentes níveis de dificuldade e um sistema de ajuda, o jogo adapta-se tanto a iniciantes como a especialistas em geografia.

### ✨ Funcionalidades

- 🎯 **Três níveis de dificuldade**: Fácil, Intermédio e Difícil
- 🆘 **Sistema de ajuda 50/50**: Elimina duas respostas incorretas (disponível nos níveis Fácil e Intermédio)
- 📊 **Histórico de jogos**: Acompanhe o seu desempenho ao longo do tempo
- 🎨 **Interface interativa**: Experiência de jogo fluida e intuitiva
- 📈 **Progressão de dificuldade**: Desafie-se progressivamente

---

## 🚀 Como Começar

### Pré-requisitos

- Python 3.7 ou superior instalado no seu sistema
- Bibliotecas Python padrão (json, random, etc.)

### Instalação

1. **Clone o repositório**:
`ash
   git clone https://github.com/celiaaboim90/A-CAPITAL-CERTA.git
   cd A-CAPITAL-CERTA
`

2. **Verifique se tem o Python instalado**:
`ash
   python --version
`

3. **Execute o jogo**:
`ash
   python quizCapitais.py
`

---

## 🎮 Como Jogar

1. **Inicie o jogo** executando o ficheiro `quizCapitais.py`
2. **Escolha o nível de dificuldade**:
   - 🟢 **Fácil**: Perguntas simples com ajuda 50/50 disponível
   - 🟡 **Intermédio**: Desafio moderado com ajuda 50/50
   - 🔴 **Difícil**: Teste os seus conhecimentos sem ajudas!
3. **Responda às perguntas** sobre as capitais europeias
4. **Use a ajuda 50/50** estrategicamente (quando disponível)
5. **Acompanhe o seu progresso** através do histórico de jogos

---

## 📁 Estrutura do Projeto
`
A-CAPITAL-CERTA/
│
├── quizCapitais.py          # Script principal - inicia o jogo
├── capitaisjogo.py          # Gestão das capitais e perguntas
├── historicojogo.py         # Sistema de histórico e pontuação
├── interface.py             # Interface de usuário e interação
├── nivelJogo.py             # Lógica dos níveis de dificuldade
│
├── capitais.json            # Base de dados das capitais europeias
├── historico_jogos.json     # Registo dos jogos anteriores
│
└── README.md                # Este ficheiro
`

### Descrição dos Ficheiros

- **`quizCapitais.py`**: Ponto de entrada do jogo, coordena todos os módulos
- **`capitaisjogo.py`**: Gestão das capitais, carregamento e seleção de perguntas
- **`historicojogo.py`**: Registo e visualização do histórico de desempenho
- **`interface.py`**: Apresentação visual e interação com o jogador
- **`nivelJogo.py`**: Implementação da lógica de diferentes níveis
- **`capitais.json`**: Dados estruturados com países e capitais
- **`historico_jogos.json`**: Armazenamento persistente dos resultados

---

## 🎯 Níveis de Dificuldade

| Nível | Perguntas | Ajuda 50/50 | Dificuldade |
|-------|-----------|-------------|-------------|
| 🟢 Fácil | Capitais mais conhecidas | ✅ Disponível | Baixa |
| 🟡 Intermédio | Mix de capitais | ✅ Disponível | Média |
| 🔴 Difícil | Todas as capitais | ❌ Indisponível | Alta |

---

## 📊 Sistema de Pontuação

- ✅ **Resposta correta**: +10 pontos
- ❌ **Resposta incorreta**: 0 pontos
- 🆘 **Uso da ajuda 50/50**: Penalização de -2 pontos

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal
- **JSON**: Armazenamento de dados
- **Módulos nativos**: json, random, datetime

---



---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Se quiser melhorar o jogo:

1. Faça um **fork** do projeto
2. Crie uma **branch** para a sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Faça **commit** das suas alterações (`git commit -m 'Adicionar nova funcionalidade'`)
4. Faça **push** para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um **Pull Request**

---

## 📝 Licença

Este projeto está sob a licença MIT. Consulte o ficheiro `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

**Célia Aboim**
- GitHub: [@celiaaboim90](https://github.com/celiaaboim90)

---

## 📞 Contacto

Tem dúvidas ou sugestões? Abra uma [issue](https://github.com/celiaaboim90/A-CAPITAL-CERTA/issues) no repositório!

---

**Divirta-se a jogar e aprender sobre as capitais da Europa! 🌍🎉**
