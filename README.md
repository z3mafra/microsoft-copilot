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
> Os arquivos de imagens foram gerados nos testes, respectivamente, nas etapas:  
>   - 4.1.3. Prompts de imagens; e,   
>   - 4.1.4. Prompts para código.  
>

-------

## 4. Criar um arquivo readme.md, incluir Prints e descrição do processo, Insights e Possibilidades aprendidas  

-------
## 4.1. Explore generative AI with Microsoft Copilot
In this exercise you will explore generative AI with Microsoft Copilot.

### Sign into Microsoft Copilot
Open Microsoft Copilot at https://copilot.microsoft.com and sign in with your personal Microsoft account.

Microsoft Copilot uses generative AI to enhance Bing search results. What this means is that unlike search alone, which returns existing content, Microsoft Copilot can put together new responses based on natural language modeling and the web’s information.

Towards the bottom of the screen, you will see a window Ask me anything. As you enter prompts into the window, Copilot uses the entire conversation thread to return responses. For example, let’s try asking a series of questions about traveling.

### 4.1.1. Use prompts to generate responses
Type in a prompt: What are 3 pros and cons of traveling in the winter?. You will see a Searching for:… and Generating… appear before the response. The model uses the searched for responses as grounding information to generate original responses. Notice that the end of the response contains links to its sources.
A screenshot of Copilot's response to a traveling prompt with three bullets for pros and three bullets for cons.

Note: If you do not see a *Generating… message or a bullet list response, you have not gotten to see Copilot in action yet. You need to return to the sign-in menu and connect the current account you are using with a personal account.

Type in a prompt: Find me 3 more pros. What you mean with this prompt is that you would like to see 3 more positive reasons for traveling in the winter that have not already been listed. Notice that with this prompt, you are asking Copilot to do two things that search alone does not do: use the previous chat response to exclude what’s returned in the new response, and use the previous chat’s topic without explicitly stating it.

Type in a prompt: Where are 3 places I can go to find fewer crowds?.

Note: Notice that while Copilot is able to give a related response, it can drop earlier “memories” of the conversation thread as it continues. As a result, the responses you get may not be directly related to traveling in the winter. This is largely to do with token input limitations. When chat “remembers” earlier parts of a conversation, it is because it has saved a certain amount of tokens from the conversation. As new tokens are introduced via your new prompts and responses, chat will let go of older tokens.

The New Topic button next to the chat window is useful. Clicking it clears the previous conversation thread so your new topic responses are not based on the previous topic. Use the New Topic icon next to the chat window to clear your message history.

### 4.1.2. Try image generation
Now let’s see an example of image generation. Type in a prompt: Create an image of an elephant eating a hamburger. Notice that a message I’ll try to create that… appears before Copilot returns a response.

A screenshot of elephants eating hamgburgers.

Note: Your images may not be identical to the ones shown here.

In the response, there is text at the bottom that reads “Powered by DALL-E”. DALL-E is a large language model that generates images from natural language input.

### 4.1.3. Try code generation
Now’s let’s see an example of code generation and translation. Type in a prompt: Use Python to create a list.

Type in the prompt: Translate that into C#. Notice how you did not need to specify what “that” is as Copilot knows to refer to the conversation history.

### 4.1.4. Bonus task
Type in a prompt: What are 3 examples of generative AI helping people?. You can use this as a way to brainstorm your own copilot ideas!

====
## 4.2. Explore Azure OpenAI
Azure OpenAI Service brings the generative AI models developed by OpenAI to the Azure platform, enabling you to develop powerful AI solutions that benefit from the security, scalability, and integration of services provided by the Azure cloud platform.

In this exercise, you’ll explore Azure OpenAI Service and use it to deploy and experiment with generative AI models.

This exercise will take approximately 25 minutes.

### Before you start
You will need an Azure subscription that has been approved for access to the Azure OpenAI service for both text and code models, and DALL-E image generation models.

To sign up for a free Azure subscription, visit https://azure.microsoft.com/free.
To request access to the Azure OpenAI service, visit https://aka.ms/oaiapply.

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
Antes de finalizar o desafio, é importate limpar (Clean up) os recrusos na sua assinatura do Azure, deletando para não gerar custos desnecessários.

### **Clean up** 
Neste laboratório a documentção não recomenda excluir todos os recursos que não serão mais utilizados. Porém, é importante fazer isso para evita acumular custos desnecessários. Foram criados três grupos de recusos: Azure AI Search, Azure AI services e Storage account.
‑
#### Deletando o Azure AI Search
>    1. Abri o portal do Azure (<https://portal.azure.com/>) e selecionei o grupo de recursos _LabCogSearch_.  
>    2. Clicar no recurso e selecionar _Excluir_ e depois _Sim_ para confirmar. O recurso foi excluído.
>
#### Deletando o Azure AI services
>    1. De volta ao portal do Azure (<https://portal.azure.com/>), selecionei o grupo de recursos _CogLabSearch_.  
>    2. Clicar no recurso e selecionar _Excluir_ e depois _Sim_ para confirmar. O recurso foi excluído.
>
>
#### Deletando o Storage account
>    1. Voltando ao portal do Azure (<https://portal.azure.com/>), selecionei o grupo de recursos _cogsrchstg_.  
>    2. Selecionei o recurso e depois _Excluir_ e _Sim_ para confirmar. O recurso foi excluído.
>
>
>>  - **Observação:** Com todos os três recursos excluídos, a plataforma informou que houve consumo de recursos na ordem de R$ 0,55, restando ainda um crédito de R$ 987,63, na assinatura gratuita.
>
> 
Após completar o Desafio, fiz a atualização no repositório local com o comando git pull.  

>- No repositório local;  
>  Clica no botão direito do mouse; e
>- Opção: "Open Git Bash here"
> No terminal digita o comando Git Pull <endereço do repositório remoto>

~~~bash
$ git pull https://github.com/z3mafra/cognitive-search.git
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
