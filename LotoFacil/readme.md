## Análise da Lotofácil: Frequência e Uniformidade dos Sorteios

### Sobre o Projeto
Este projeto foi criado com o objetivo de reforçar habilidades em análise de dados, incluindo estatísticas descritivas, visualização de dados e testes de hipóteses. Utilizando dados históricos dos sorteios da Lotofácil, explorei a frequência dos números sorteados e avaliei se os sorteios seguem um padrão uniforme. 

O projeto também inclui simulações de sorteios para comparar os resultados reais com distribuições ideais, permitindo espaço para testes adicionais e melhorias.

---

### Estrutura do Projeto
O projeto está organizado da seguinte forma:

- **`analise_lotofacil.ipynb`**: Notebook contendo o código e as análises realizadas.
- **`Lotofacil.xlsx`**: Base de dados utilizada, com o histórico dos sorteios.
- **Gráficos**: Visualizações criadas durante o projeto.
- **README.md**: Este arquivo explicativo.

---

### Objetivos
- Reforçar habilidades em análise e visualização de dados.
- Analisar a frequência dos números sorteados na Lotofácil.
- Realizar um teste estatístico para verificar a uniformidade dos sorteios.
- Simular sorteios para comparação com dados reais.

---

### Ferramentas e Tecnologias Utilizadas
- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas` para manipulação de dados.
  - `numpy` para cálculos numéricos e simulações.
  - `matplotlib` e `seaborn` para visualização de dados.
  - `scipy` para testes estatísticos.

---

### Resultados Principais
- **Frequência dos Números Sorteados**: Análise da frequência de cada número nos sorteios históricos.
- **Teste de Uniformidade (Qui-Quadrado)**: Conclusão de que os sorteios seguem uma distribuição uniforme, dentro do nível de significância adotado.
- **Simulação de Sorteios**: Comparação entre a distribuição dos números sorteados reais e sorteios simulados com distribuição uniforme.

---

### Como Reproduzir o Projeto
1. **Clonar o Repositório**:  
   ```bash
   git clone https://github.com/lucasbomfim10/Analise-lotofacil.git
   cd Analise-lotofacil
   ```
2. **Instalar Dependências**:  
   Certifique-se de ter o Python instalado. Instale as dependências com:  
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```
3. **Executar o Notebook**:  
   Abra o arquivo `analise_lotofacil.ipynb` em seu editor de notebooks favorito (como Jupyter ou VSCode) e execute as células sequencialmente.

---

### Possibilidades de Expansão
- Analisar padrões temporais nos sorteios.
- Implementar outros testes estatísticos para validar os resultados.
- Criar um dashboard interativo para visualização de dados.
- Explorar métodos avançados de simulação com modelos probabilísticos.

---

### Licença
Este projeto foi desenvolvido apenas para fins educacionais e está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.