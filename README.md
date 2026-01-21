# Automação de Cadastro de Produtos (RPA) 🤖🐍

Este projeto consiste em um robô de automação de processos (RPA) que realiza o login e o cadastro automático de uma lista de produtos em um sistema web de gestão. O objetivo é eliminar o esforço manual de preenchimento, garantindo agilidade e precisão nos dados.

## 📁 Estrutura de Arquivos
* **`main.py`**: Script principal que contém a lógica de navegação, login e o loop de cadastro dos produtos.
* **`posicao_mouse.py`**: Script auxiliar utilizado para capturar as coordenadas (X e Y) da tela, garantindo que o bot clique nos campos corretos independente da resolução do monitor.
* **`produtos.csv`**: Base de dados contendo as informações (código, marca, tipo, categoria, etc.) que o bot deve processar.

## 🛠️ Tecnologias e Bibliotecas
- **Python 3**: Linguagem base.
- **Pandas**: Utilizado para ler e estruturar a base de dados CSV.
- **PyAutoGUI**: Biblioteca para automação de teclado e mouse.
- **Time**: Para gerenciar os intervalos de carregamento das páginas web.

## 🚀 Como o projeto funciona
O script executa uma sequência de passos lógicos:
1. **Configuração de Pausa**: Define um intervalo padrão entre comandos para evitar erros de sincronização.
2. **Navegação**: Abre o navegador Chrome e acessa a URL do sistema.
3. **Login**: Realiza a autenticação automática no portal.
4. **Iteração de Dados**: Percorre cada linha do arquivo CSV e preenche os campos correspondentes (Código, Marca, Tipo, Categoria, Preço, Custo e Observações).
5. **Tratamento de Condicionais**: O código verifica se existem observações antes de preenchê-las, evitando erros de campos vazios (`NaN`).
6. **Finalização**: Envia o formulário e retorna ao topo da página para o próximo cadastro.

## ⚙️ Instruções de Uso
1. Clone este repositório.
2. Instale as dependências necessárias:
   ```bash
   pip install pyautogui pandas
3. Execute o script posicao_mouse.py se precisar ajustar as coordenadas para a sua tela.

4. Execute o script principal:
   ```
   python main.py
