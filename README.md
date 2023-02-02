# calculation-average-numbers
calculation-average-numbers

Requirements
------------

Este projeto requer:

    * Python 3.8 or earlier
    * poetry for local development

Installation
------------

1. Instalar dependencias e criar maquina virtual

         poetry install
    

2. Para executar a aplicação: 

         flask run


Get / Post
------------
Recomendado a utilização do postman para testes.

Caso não tenha instalado: https://www.postman.com/downloads/

1. O endpoint sera apresentado no momento que iniciar o flask: 

![image](https://user-images.githubusercontent.com/62955161/216433016-4eaf4cee-318e-49b1-a31a-e71781bebd31.png)

2. Inserir o endpoint no postman, da seguinte forma: 

![image](https://user-images.githubusercontent.com/62955161/216433398-b58db3b1-c765-4016-b996-0480a906d1ec.png)

3. Ao executar sera apresentada a lista de dados e a mediana dos numeros. 

![image](https://user-images.githubusercontent.com/62955161/216433611-a14235ed-202d-4605-950b-5cb14337b0db.png)

4. Para inserir um novo numero, devera mudar o metodo para "POST", e inserir o seguinte payload: 

         {
             "new_number": <valor_desejado>
         }

5. Apos executar sera apresentado na tela o novo valor. 

![image](https://user-images.githubusercontent.com/62955161/216434219-1e0c4cfd-362f-4406-a35e-0bfcba20e0f7.png)
