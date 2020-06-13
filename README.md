# LEADGen

Nesse projeto foi desenvolvido um sistema de predição de *leads business-to-business* (B2B). Após o desenvolvimento a aplicação teve seu *deploy* realizado
na plataforma Heroku.

O link para acesso está [aqui](https://lead--gen.herokuapp.com/).

## Dados utilizados

Os dados utilizados foram fornecidos pela Codenatio em sua aceleração para *data science*. Esse dados são referentes a mais de 400 mil empresas situadas na região
norte do pais. 

Diferentes *features* estão presentes no conjunto de dados, dentre elas pode-se citar o setor de atuação da empresa, saúde tributária, quantidade de sócios e etc.

Além do banco de dados de empresas o sistema precisa de um arquivo *.csv* contendo os identificadores de todos os clientes da empresa que deseja realizar a predição de *leads*.

## Criação do projeto

O projeto foi divido em três partes:

- Análise exploratória de dados;
- Processamento de dados;
- Criação do modelo.

Para desevolvimento dos experimentos *notebooks* foram utilizados, sendo todos os códigos desenvolvidos em *scripts .py*. 

### Análise exploratória de dados

Nessa etapa foi realizada uma análise inicial do conjunto de dados. Foi verificada a existência de valores duplicados, quantidade de valores nulos e relação entre diferentes *features*. 

Além disso, *features* com mais de 40% de seus valores nulos foram removidas.

### Processamento dos dados

Na etapa de processamento de dados os dados faltantes foram preenchidos. Foi desenvolvida uma *pipeline* para preenchimento desses valores. 

Os valores faltantes foram preenchidos da seguinte forma:

- Valores faltantes booleanos: Preenchidos com **False**;
- Valores faltantes numéricos: Preenchidos com **0**;
- Valores faltantes categóricos: Preenchidos com **OUTROS** ou com  **SEM INFORMAÇÃO**.

Após o preenchimento dos valores faltantes outra *pipeline* foi desenvolvida para processamento dos dados. Essa *pipeline* teve três etapas:

- Substituição dos valores booleanos por **0** ou **1**;
- Aplicação do *LabelEncoder* nos dados categóricos;
- Aplicação de uma padronização nos dados numéricos por meio do *StandardScaler*.

### Criação do modelo

A última etapa foi referente a criação do modelo. Inicialmente foi selecionado um conjunto de *features* com alto poder descritivo e após isso foi criado o modelo.

O modelo desenvolvido consiste em duas parte, a primeira parte realiza uma clusterização de clientes e determina o centro de cada *cluster*. A segunda parte calula a similaridade de cada empresa presente no conjunto de dados com cada centro determinado na primeira etapa. Empresas com alta similaridade têm altas chances de ser um futuro cliente.

## Criação da *dashboard*

Para criação da *dashboard* a biblioteca [streamlit](streamlit.io) foi utilizada. Essa biblioteca permite o desenvolvimento de aplicações visuais de maneira rápida e tem total integração com a biblioteca pandas para análise dos dados e [plotly](https://plotly.com/python/) para análises gráficas.

A *dashboard* desenvolvida conta com três páginas:

- Predição de clientes: aqui é onde é importado o banco de dados para determinação dos *clusters* e predição de possíveis novos clientes. Além disso essa etapa permite a a visualização gráfica e a realização do *download* das predições obtidas;
- Análise de resultados: nessa parte pode-se verificar os resultados de maneira detalhada, selecionando os níveis de similaridade desejados.
- Análise de clientes: nessa parte, por meio do identificador da empresa pode-se obter informações detalhadas acerca da mesma.

### Predição de clientes

A figura abaixo aprensenta a interface dessa seção. Por meio da técnica de decomposicação em componentes principais foi possível gerar uma visualização para os dados e seus *clusters*.

![Tela 1](/images/tela_1.png)

### Análise de resultados

A figura abaixo aprensenta a interface dessa seção.

![Tela 1](/images/tela_2.png)

### Análise de clientes

A figura abaixo aprensenta a interface dessa seção.

![Tela 1](/images/tela_3.png)

## Como usar

### *Requirements*

- numpy===1.18.0
- yellowbrick==1.1
- seaborn==0.10.1
- plotly==4.8.1
- matplotlib==3.2.1
- pandas==1.0.4
- streamlit==0.57.3
- scikit_learn==0.23.1

Para instalar todos os requerimentos o seguinte comando pode ser utilizado:

```
pip install -r requirements.txt
```

### Geração do *dashboard*

Para gerar o *dashboard* o seguinte comando deverá ser utilizado:

```
streamlit run dashboard.py
```

## Descrição dos arquivos do projeto

### dashboard

Aqui ficam os códigos responsáveis pela criação da *dashboard*.

### scripts

Aqui ficam os códigos responsáveis pela processamento dos dados, criação do modelo e etc.

### notebooks

Aqui ficam os *notebooks* utilizados para realização dos experimentos.

## Dockerfile

Para garantir o funcionamento do projeto é recomendável a criação de um *container* utilzando o arquivo **Dockerfile**.


