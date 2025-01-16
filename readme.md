# README

## Descrição
Este é um web server criado com Python, projetado para receber dados em formato JSON e retornar a tradução correspondente. Ele possui uma rota principal (`/traduzir`) que aceita uma frase e um idioma como parâmetros e retorna a tradução desejada.

### Rota principal
- **Endpoint:** `/traduzir`
- **Método HTTP:** POST
- **Parâmetros JSON:**
  - `frase`: A frase a ser traduzida. (Ex.: "este é um exemplo")
  - `idioma`: O código do idioma para tradução. (Ex.: "en" para inglês)

### Exemplo de Requisição
```json
{
  "frase": "este é um exemplo",
  "idioma": "en"
}
```

### Exemplo de Resposta
```json
{
  "tradução": "this is an example"
}
```

## Instalação e Configuração

1. Certifique-se de que o Python (versão 3.7 ou superior) está instalado.
2. Clone este repositório ou baixe os arquivos necessários.
3. Navegue até o diretório do projeto.
4. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # Para Linux/Mac
   venv\Scripts\activate   # Para Windows
   ```
5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução do Servidor

1. No diretório do projeto, execute o arquivo `main.py`:
   ```bash
   python main.py
   ```
2. O servidor será iniciado e estará acessível em `http://127.0.0.1:8000` por padrão.

## Dependências Necessárias
- FastAPI
- Uvicorn
- Biblioteca de tradução (por exemplo, `googletrans` ou similar)

## Exemplo de Uso com cURL

```bash
curl -X POST "http://127.0.0.1:8000/traduzir" \
-H "Content-Type: application/json" \
-d '{"frase": "este é um exemplo", "idioma": "en"}'
```

## Exemplo de Arquivo `requirements.txt`

```
fastapi
uvicorn
googletrans==4.0.0-rc1
