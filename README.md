# Desafio: Explorando os Recursos de IA Generativa com Copilot e OpenAI
## Repositório: microsoft-copilot  

> 1. Criar um novo repositório no github com um nome a sua preferência  
> 2. Crie uma pasta chamada 'inputs' e salve as imagens que você utilizou
> 3. Crie uma pasta chamado 'output' e salve os resultados de reconhecimento de texto nessas imagens
> 4. Crie um arquivo chamado readme.md, deixe alguns prints descreva o processo, alguns insights e possibilidades que você aprendeu durante o conteúdo.
>> 4.1. Explore generative AI with Microsoft Copilot  
>>> 4.1.1. Use prompts to generate responses  
>>> 4.1.2. Try image generation  
>>> 4.1.3. Try code generation  
>>> 4.1.4. Bonus task  
>> 
>> 4.2. Explore Azure OpenAI  
>> 4.3. Explore content filters in Azure OpenAI  
> 5. Fnalizar e Compartilhar o link do repositório  
>>  
--------
-------

## 1. Criar um novo repositório no github com um nome a sua preferência  

Na maquina local foi crido o diretório 'microsoft-copilot'  

~~~bash
$ mkdir microsoft-copilot
~~~  

Depois, iniciei o diretório como um repositório no Git.

~~~bash
$ git init
~~~

No GitHub foi criado o repositório microsoft-copilot

> Comandos/configurações:  
> 
> - "Novo repositório".  
> - Nome para o repositório: "microsoft-copilot".  
> - Descrição: "Explorando a IA generativa com o Microsoft Copilot".  
> - Visibilidade: "pública".  
> - Opção: LEIAME.  
> - Cliquei em "Criar repositório".  
> 

-------

## 2. Criar uma pasta chamada 'inputs' e salve as imagens que você utilizou  

Na maquina local, na raiz do repositório 'microsoft-copilot', foi crido o diretório 'inputs'  

~~~bash
$ mkdir inputs
~~~  

No GitHub foi criado o diretório 'inputs' no repositório recog-txt-img

> Comandos/configurações:  
> 
> - Botão: "Add File".  
> - Opção: + Create new file.  
> - Preenchi: inputs/prompts.md  
> - Opção: Commit changes.  
> - Dentro do diretório 'inputs': "Add File".  
> - Opção: Upload files 
> - Cliquei em "Choose your files".  
> - Carregou o conjunto de imagens.  
>

Foram salvas os textos utilizadas como prompts, conforme as instruções sugeridos na documentação, em quatro grupos: Sobre o prompt;  Prompt para projeto de pesquisadores; Prompts de Imagens; e, Prompts para código.  


-------

## 3. Criar uma pasta chamado 'output' e salve os resultados de reconhecimento de texto nessas imagens  

Na maquina local, na raiz do repositório 'microsoft-copilot', foi crido o diretório 'output'  

~~~bash
$ mkdir output
~~~  

No GitHub foi criado o diretório 'output' no repositório 'microsoft-copilot'

> Comandos/configurações:  
> 
> - Botão: "Add File".  
> - Opção: + Create new file.  
> - Preenchi: output/Imagens.md  
> - Opção: Commit changes.  
> - Dentro do diretório 'inputs': "Add File".  
> - Opção: Upload files 
> - Cliquei em "Choose your files".  
> - Carregou o conjunto de imagens.
>

Foram salvas as imagens e códigos, observando a codificação dos nomes para manter a ordem em que foram testadas, em dois grupos: para imagnes, quatro Blocos, com quatro imagnes cada; e para os códigos, dois arquivos python.  

>[!NOTE]
>
> Os arquivos de imagens e códigos foram gerados nos testes, respectivamente, nas etapas:  
>   - 4.1.3. Prompts de imagens; e,   
>   - 4.1.4. Prompts para código.  
>

-------

## 4. Criar um arquivo readme.md, incluir Prints e descrição do processo, Insights e Possibilidades aprendidas  

-------
## 4.1. Explore IA generativa com Microsoft Copilot
Exercício para explorar a IA generativa com o Microsoft Copilot.

### Sign no Microsoft Copilot
Abrir o Microsoft Copilot no link: https://copilot.microsoft.com e entrar com a conta pessoal da  Microsoft.

O Microsoft Copilot usa IA generativa para aprimorar os resultados de pesquisa do Bing. O que isto significa é que, diferentemente da pesquisa apenas, que retorna conteúdo existente, o Microsoft Copilot pode reunir novas respostas com base na modelagem de linguagem natural e nas informações da web.

Na parte inferior da tela, você verá uma janela Pergunte-me qualquer coisa. À medida que você insere prompts na janela, o Copilot usa todo o thread da conversa para retornar respostas. Por exemplo, vamos tentar fazer uma série de perguntas sobre viagens.

### 4.1.1. Explorando prompts

Prompt:
Qual a melhor maneira de estruturar um prompt?

Resposta:
Prompt é o termo usado para se referir aos comandos que são dados às ferramentas de inteligência artificial generativa. É a forma de pedir para que a IA crie algo que você precisa de maneira mais efetiva. Vamos entender como estruturar prompts de forma prática e eficiente:
>>    1. Clareza: Para criar prompts que realmente despertem a criatividade, tenha clareza e use palavras simples e diretas, como se estivesse explicando algo a um amigo. Frases curtas e bem definidas guiam a IA diretamente ao ponto, sem rodeios. Pense em eficiência: quanto mais direto, melhor o resultado.
>>    2. Especificidade: Contextualize seu pedido, adicionando detalhes do que você deseja. Por exemplo, ao invés de digitar “crie um conteúdo sobre marketing”, seja mais específico: “crie um guia passo a passo sobre estratégias de marketing para pequenas empresas no setor de tecnologia”. Quanto mais claros e detalhados forem os prompts, mais precisas e alinhadas com suas expectativas serão as respostas da IA.
>>    3. Divisão em subtarefas: Se a tarefa for complexa, divida-a em subtarefas menores. Isso ajuda a guiar a IA de forma mais eficiente e a obter respostas relevantes.
Lembre-se: a engenharia de prompt é o processo de criação e refinamento do prompt usado pelo modelo. Ao estruturar prompts de maneira adequada, você está basicamente dando à IA um roteiro para seguir, assim como quando pedimos direções a alguém em um local desconhecido. Quanto mais claro e detalhado for o prompt, mais alinhadas com suas necessidades serão as respostas geradas pela IA.

Referências:  
>> [1. O que é prompt? Como estruturar na prática?](https://hotmart.com/pt-br/blog/o-que-e-prompt).  
>> [2. melhor maneira de estruturar um prompt.](https://www.bing.com/search?q=melhor+maneira+de+estruturar+um+prompt&FORM=bngcht&toWww=1&redig=E050BDCA48E14B41866C5F4296FD25C4)  
>> [3. O que é Engenharia de Prompt e quais as suas principais técnicas? Aprenda a escrever um bom comando para IA.](https://www.alura.com.br/artigos/engenharia-prompt)  
>> [4. Engenharia de Prompt para não-técnicos: um guia prático.](https://www.startse.com/artigos/engenharia-de-prompt-para-nao-tecnicos-um-guia-pratico/)  


Prompt:
Você pode me dar um exemplo prático de prompt eficiente?

Copilot
Gerando respostas para você…
>>   Claro! Vamos criar um exemplo de prompt eficiente para gerar um poema sobre a beleza das estações do ano. Aqui está um prompt bem estruturado:
>>   "Escreva um poema curto que celebre a beleza das quatro estações do ano: primavera, verão, outono e inverno. Destaque as características únicas de cada estação, como as cores, os aromas e as sensações que elas evocam. Seja poético e envolvente."
>>   Com esse prompt, a IA terá uma direção clara e específica para criar um poema que atenda às suas expectativas. Lembre-se de adaptar o prompt conforme a tarefa desejada, adicionando detalhes relevantes para obter resultados ainda mais precisos e criativos .


Prompt:  
Escreva um poema curto que celebre a beleza das quatro estações do ano: primavera, verão, outono e inverno. Destaque as características únicas de cada estação, como as cores, os aromas e as sensações que elas evocam. Seja poético e envolvente.


Copilot  
>>   Gerando respostas para você…
>>   Certamente! Aqui está um poema que celebra as quatro estações do ano:

**Primavera**  

>>   Nas asas da primavera, o mundo desperta,
>>   Cores vibrantes dançam na brisa suave.
>>   Os campos se enchem de flores em festa,
>>   E o sol beija a terra com ternura e amor.

**Verão**  

>>   O verão chega com ardor e paixão,
>>   O céu se veste de azul profundo.
>>   As praias convidam para um mergulho,
>>   E o calor nos abraça como um velho amigo.

**Outono**  

>>   Folhas douradas caem em cânticos suaves,
>>   O vento sussurra segredos entre os galhos.
>>   O aroma de maçãs e canela preenche o ar,
>>   E o crepúsculo pinta o céu de tons alaranjados.
  
**Inverno**  
  
>>   A neve cobre o mundo em um manto branco,
>>   As noites são longas, estreladas e frias.
>>   Nas lareiras, histórias são contadas,
>>   E o aconchego dos cobertores nos envolve.  
  
>>   Quatro estações, quatro encantos distintos,
>>   Cada uma com sua magia, sua melodia.
>>   Que possamos celebrar a dança do tempo,
>>   Enquanto a Terra gira, e a vida floresce.


### 4.1.2. Prompt para projeto de pesquisadores

Prompt:
Quais três recomendações para começar um projeto de pesquisa? Ter uma boa ideia para trabalhar?

Copilot 
Claro! Começar um projeto de pesquisa pode parecer desafiador, mas com as orientações certas, Prompt: estará no caminho certo. Aqui estão três recomendações essenciais para iniciar seu projeto de pesquisa:
>>   1. Escolha de Tema e Formulação da Pergunta de Pesquisa:
>>      ◦ Tema Específico: Selecione um tema específico que desperte seu interesse. Evite temas muito amplos, pois podem dificultar a abordagem detalhada. 
>>      ◦ Pergunta Clara: Formule uma pergunta de pesquisa clara e concisa. Ela deve ser o ponto central do seu projeto e direcionar sua investigação. 
>>   2. Definição dos Objetivos:
>>      ◦ Objetivo Geral: Determine o objetivo geral do seu projeto. O que você deseja alcançar com sua pesquisa? 
>>      ◦ Objetivos Específicos: Estabeleça objetivos específicos que direcionem sua investigação em detalhes. Eles ajudarão a delinear o escopo do trabalho. 
>>   3. Justificativa e Importância do Estudo:
>>      ◦ Justificativa: Explique por que sua pesquisa é relevante. Qual é a importância do seu estudo para a área acadêmica ou profissional? 
>>      ◦ Contribuição: Descreva como sua pesquisa contribuirá para o conhecimento existente. Identifique lacunas na literatura que seu projeto pretende preencher. 
>>   Lembre-se de que um projeto de pesquisa bem estruturado é fundamental para o sucesso do seu trabalho acadêmico. Com essas recomendações, você estará preparado para dar os primeiros passos na sua jornada de pesquisa! 🌟12345
  
Referências:  
>> [1. Projeto de Pesquisa.](https://projetodepesquisa.com.br/)  
>> [2. recomendações para começar um projeto de pesquisa.](https://www.bing.com/search?q=recomendações+para+começar+um+projeto+de+pesquisa&toWww=1&redig=467B49F947434422A8255DDAEF8FD575)  
>> [3. Projeto de pesquisa pronto: o que é, como fazer e modelos.](https://viacarreira.com/projeto-de-pesquisa/)  
>> [4. RECOMENDAÇÕES PARA O PROJETO DE PESQUISA.](https://www.unirg.edu.br/anexos/graduacao/Administracao/ESTAGIO/2019/7%20Periodo/Recomendacoes_para_projeto_de_pesquisa.pdf)  
>> [5. Projeto De Pesquisa: Saiba Por Onde Começar.](https://www.univates.br/blog/projeto-de-pesquisa-por-onde-comecar/)  


Prompt:  
Quais seriam três dificuldades enfrentadas por quem vai desenvolver um projeto de pesquisa?

Copilot  
Desenvolver um projeto de pesquisa pode ser desafiador, mas também recompensador. Aqui estão três dificuldades comuns que os pesquisadores enfrentam durante o processo:
>>   1. Estruturação do Projeto:
>>      ◦ Identificação de Fontes Relevantes: Muitos alunos têm dificuldade em encontrar fontes pertinentes ao projeto de pesquisa. Saber onde buscar informações é essencial. 
>>      ◦ Utilização das Fontes: Compreender como usar as informações das fontes no projeto é outro desafio. Isso inclui a elaboração de citações indiretas e a avaliação da qualidade das informações. 
>>      ◦ Relação entre Teoria e Método: Relacionar o material teórico com o método escolhido para a pesquisa pode ser complexo. É importante alinhar a teoria com a prática. 
>>   2. Escolha do Tema e Base Teórica:
>>      ◦ Interesse Pessoal: Escolher um tema pelo qual você realmente se interesse é crucial. Isso manterá sua motivação e facilitará a pesquisa. 
>>      ◦ Leitura Ampliada: Consumir diferentes tipos de conteúdo relacionados ao tema (artigos, livros, dissertações) amplia sua compreensão e embasa sua pesquisa. 
>>      ◦ Diferencial e Adaptações: Procure um diferencial em relação ao que outros pesquisadores estão fazendo. Esteja aberto a fazer adaptações conforme necessário. 
>>   3. Metodologia e Pergunta de Pesquisa:
>>      ◦ Pergunta Bem Definida: A pergunta de pesquisa deve ser clara e nortear todas as decisões do projeto. 
>>      ◦ Escolha da Metodologia: Definir a estratégia de estudo e os procedimentos metodológicos é fundamental. Isso inclui entender como outros pesquisadores abordaram questões semelhantes. 
>>   Lembre-se de que a pesquisa é uma jornada de aprendizado e descoberta. Enfrente os desafios com naturalidade e mantenha-se motivado! 🌟

Referências:  
>> 1. As principais dificuldades no projeto de pesquisa. [link com defeito].  
>> [2. Como Superar os Desafios que Surgem Durante a Pesquisa.](https://www.enago.com.br/academy/como-superar-os-desafios-que-surgem-durante-a-pesquisa/)  
>> [3. GUIA PARA ELABORAÇÃO DE  PROJETOS DE PESQUISA.](https://www.uece.br/posla/wp-content/uploads/sites/28/2021/08/guiaprojeto_pesquisa.pdf)  
>> [4. O que é o Problema do Projeto de Pesquisa? Exemplos.](https://alunoexpert.com.br/problema-no-projeto-de-pesquisa/)
>> [5. Cinco pontos que não podem faltar no seu projeto de pesquisa.](https://www.ifsc.edu.br/web/blog/w/cinco-pontos-que-nao-podem-faltar-no-seu-projeto-de-pesquisa)  
>> [6. Como vencer a dificuldade de escrever um projeto de pesquisa?.](https://vitalknowledge.com.br/como-vencer-dificuldade-escrever-projeto-de-pesquisa/)  


### 4.1.3. Prompts de Imagens

Você
crie uma imagem da terra vista do espaço, como a pupila de um olho!

Bloco 1:  

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco1-01.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco1-02.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco1-03.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco1-04.jpg" width="50%">

Você
crie uma imagem da terra vista do espaço, como sendo a pupila dentro de um olho!

Bloco 2:  

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco2-01.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco2-02.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco2-03.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco2-04.jpg" width="50%">

Você
crie uma imagem da terra vista do espaço, como sendo a pupila dentro de um olho, como parte de um rosto de pele clara !

Bloco 3:  

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco3-01.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco3-02.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco3-03.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco3-04.jpg" width="50%">

Você
crie uma imagem da terra vista do espaço, como sendo a pupila dentro de um olho e iris negra, como parte de um rosto de pele clara !

Bloco 4:  

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco4-01.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco4-02.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco4-03.jpg" width="50%">

<img src="https://github.com/z3mafra/microsoft-copilot/blob/main/output/Bloco4-04.jpg" width="50%">


### 4.1.3. Prompts de código



====
## 4.2. Explore Azure OpenAI
O Azure OpenAI Service traz os modelos generativos de IA desenvolvidos pela OpenAI para a plataforma Azure, permitindo-lhe desenvolver soluções poderosas de IA que beneficiam da segurança, escalabilidade e integração de serviços fornecidos pela plataforma de nuvem Azure.  

Neste exercício, você explorará o serviço Azure OpenAI e o usará para implantar e experimentar modelos de IA generativos.  

Este exercício levará aproximadamente 25 minutos.  

### Antes que você comece
Você precisará de uma assinatura do Azure aprovada para acesso ao serviço Azure OpenAI para modelos de texto e código e modelos de geração de imagens DALL-E.  

Para se inscrever para uma assinatura gratuita do Azure, visite https://azure.microsoft.com/free.  
Para solicitar acesso ao serviço Azure OpenAI, visite https://aka.ms/oaiapply.  

>[!NOTE]
>
> Não foi possível ter acesso aos recursos do Azure OpenAI.  
>
-------

====
## 4.3. Explore content filters in Azure OpenAI  
Azure OpenAI includes default content filters to help ensure that potentially harmful prompts and completions are identified and removed from interactions with the service. Additionally, you can apply for permission to define custom content filters for your specific needs to ensure your model deployments enforce the appropriate responsible AI principals for your generative AI scenario. Content filtering is one element of an effective approach to responsible AI when working with generative AI models.

In this exercise, you’ll explore the affect of the default content filters in Azure OpenAI.

This exercise will take approximately 25 minutes.

### Before you start
You will need an Azure subscription that has been approved for access to the Azure OpenAI service.

To sign up for a free Azure subscription, visit https://azure.microsoft.com/free.
To request access to the Azure OpenAI service, visit https://aka.ms/oaiapply.

====
## 5. Fnalizar e Compartilhar o link do repositório  

Nesta atividade não foi preciso limpar (Clean up) os recrusos na sua assinatura do Azure.
Após completar o Desafio, fiz a atualização no repositório local com o comando git pull.  

>- No repositório local;  
>  Clica no botão direito do mouse; e
>- Opção: "Open Git Bash here"
> No terminal digita o comando Git Pull <endereço do repositório remoto>

~~~bash
$ git pull https://github.com/z3mafra/microsoft-copilot.git
~~~

### **Postar link do repositório**  

Como é solicitado no enunciado do desafio, o link do GitHub deve ser compartilhado na plataforma da DIO. Para isso, segui os seguintes passos:  


>  1. Abra o portal da DIO (<https://www.dio.me/>), com as credenciais e selecione o [Bootcamp Microsoft AZure AI Fundamentals](https://web.dio.me/track/microsoft-azure-ai-fundamentals).  
>  2. Entra na Atividade Desafio de projeto: "Reconhecimento Facial e transformação de imagens em Dados no Azure ML"
>  3. Clica no botão "ENTREGAR PROJETO" 
>  4. Cola o link do projeto na caixa de texto "Repositório do Projeto"; Cola a descrição do repositório; Ler e marcar o Check box "Termos de uso", concordando com os termos o recurso; e,
>  5. Selecione Entregar. O Desafio foi então entregue.
>

--------
--------
