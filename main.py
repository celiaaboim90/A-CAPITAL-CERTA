from quizcapitais import QuizCapitais

if __name__ == "__main__":
    quiz = QuizCapitais()
    quiz.iniciar_quiz() 
   
    while True:
        quiz.interface.limpar_ecra()
        quiz.interface.exibir_titulo()
        
        opcao = quiz.interface.exibir_menu() 
        
        if opcao == '1':
            quiz.iniciar_quiz() 
            quiz.regressar_zero() 
            
        elif opcao == '2':
            quiz.interface.limpar_ecra()

            quiz.historico_jogo.ver_historico() 
            input("Pressione Enter para regressar ao menu...")
            
        elif opcao == '3':
            print("Obrigado por jogar! Até à próxima.")
            break 
            
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione qualquer tecla para continuar...")