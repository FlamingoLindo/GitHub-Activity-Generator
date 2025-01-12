# GitHub-Activity-Generator

![image](/image.png)

*Essa screenshoot foi tirada no dia em que eu decide fazer esse projeto.

Este projeto foi criado como uma forma divertida de explorar a ideia de que a quantidade de contribuições no GitHub pode influenciar o interesse dos recrutadores durante o processo de seleção. A motivação principal foi testar a teoria de que uma alta atividade no GitHub pode ser um fator decisivo para contratação. Independentemente da validade dessa ideia, o projeto foi uma ótima oportunidade para praticar automação e programação.

## Descrição do Projeto

Este repositório contém um script Python que automatiza a geração de commits no GitHub, criando um arquivo de texto com dados aleatórios e realizando commits em intervalos regulares. Ele também utiliza a biblioteca `schedule` para agendar atividades diárias de commits.

### Funcionalidades Principais
1. **Geração de arquivo**: O script cria um arquivo chamado `activity.txt` contendo uma sequência de caracteres aleatórios.
2. **Automação de commits**: O script adiciona, comita e realiza o push dessas alterações para o repositório remoto.
3. **Agendamento**: Um agendador executa a rotina diariamente em um horário pré-determinado, com múltiplos commits em cada execução.

## Estrutura do Projeto

- `main.py`: Arquivo principal que coordena todas as funções.
- `write_file.py`: Gera o arquivo `activity.txt` com conteúdo aleatório.
- `git_push.py`: Adiciona, realiza o commit e faz o push das alterações para o repositório remoto.
- `activity.txt`: Arquivo gerado contendo dados aleatórios, usado para simular atividades no repositório.
- `README.md`: Este arquivo.

## Observação Importante

Este projeto foi desenvolvido para fins educacionais e de diversão. Embora ele automatize a geração de contribuições, a autenticidade e qualidade das contribuições são mais importantes do que a quantidade. Considere usá-lo com responsabilidade e não se esqueça de criar projetos significativos no GitHub que demonstrem suas habilidades reais.

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias para este projeto.

