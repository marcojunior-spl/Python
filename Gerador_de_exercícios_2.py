import os

def gerar_conteudo_final():
    # Mantemos o mesmo diretório base para adicionar lá dentro
    base_dir = "Lista_Exercicios_StoryMode"
    
    arquivos = {}

    # =========================================================================
    # UNIDADE 09: MATRIZES (Listas de Listas)
    # =========================================================================
    
    # --- QUESTÃO 1 ---
    path_u9_q1 = f"{base_dir}/Unidade_09/Questao_01_Gerador_Terreno"
    arquivos[f"{path_u9_q1}/README.txt"] = """
================================================================================
                        QUESTÃO 01: O GERADOR DE TERRENO (Minecraft)
================================================================================
CONTEXTO:
Você está criando um jogo estilo Minecraft. O mundo é plano e representado por uma matriz
(uma grade de blocos). Inicialmente, o mundo é todo feito de "Ar" (representado por 0).

Você precisa criar uma função que inicializa esse mundo. O jogo pede um mundo de tamanho
N (linhas) por M (colunas).

ESPECIFICAÇÃO TÉCNICA:
1. Função: `criar_mundo(linhas, colunas)`
2. Entrada: Dois inteiros.
3. Saída: Uma lista de listas (Matriz) preenchida com 0.
   Ex: linhas=2, colunas=3 -> [[0, 0, 0], [0, 0, 0]]
4. Dica: Use laços aninhados ou list comprehension.
"""
    arquivos[f"{path_u9_q1}/resolucao.py"] = "def criar_mundo(linhas, colunas):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u9_q1}/test_resolucao.py"] = """
import pytest
from resolucao import criar_mundo

def test_tamanho_correto():
    matriz = criar_mundo(3, 2)
    # Deve ter 3 linhas
    assert len(matriz) == 3
    # Cada linha deve ter 2 colunas
    assert len(matriz[0]) == 2
    assert matriz == [[0, 0], [0, 0], [0, 0]]

def test_matriz_quadrada():
    matriz = criar_mundo(2, 2)
    assert matriz == [[0, 0], [0, 0]]
"""

    # --- QUESTÃO 2 ---
    path_u9_q2 = f"{base_dir}/Unidade_09/Questao_02_Raio_X"
    arquivos[f"{path_u9_q2}/README.txt"] = """
================================================================================
                        QUESTÃO 02: O RAIO-X DA MALETA
================================================================================
CONTEXTO:
Na segurança do aeroporto, a máquina de Raio-X gera uma matriz de densidades.
Itens de metal possuem densidade maior que 50.
Você precisa varrer a matriz inteira e contar quantos objetos de metal existem na mala.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `contar_metal(matriz)`
2. Entrada: Uma lista de listas de inteiros.
3. Saída: Um inteiro (quantidade de elementos > 50).
4. Lógica: Você precisa iterar por cada linha e, dentro da linha, por cada item.
"""
    arquivos[f"{path_u9_q2}/resolucao.py"] = "def contar_metal(matriz):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u9_q2}/test_resolucao.py"] = """
import pytest
from resolucao import contar_metal

def test_encontrar_metais():
    mala = [
        [10, 55, 10],
        [60, 10, 10],
        [10, 10, 99]
    ]
    # 55, 60 e 99 são metais
    assert contar_metal(mala) == 3

def test_nenhum_metal():
    mala = [[1, 2], [3, 4]]
    assert contar_metal(mala) == 0
"""

    # --- QUESTÃO 3 ---
    path_u9_q3 = f"{base_dir}/Unidade_09/Questao_03_Traco_Principal"
    arquivos[f"{path_u9_q3}/README.txt"] = """
================================================================================
                        QUESTÃO 03: ADIANTANDO O BINGO
================================================================================
CONTEXTO:
Em um jogo de Bingo ou em Álgebra Linear, a "Diagonal Principal" é muito importante.
São os elementos onde o índice da linha é igual ao índice da coluna (0,0), (1,1), (2,2)...

Sua missão é calcular o "Traço" da matriz, que é a SOMA de todos os elementos da diagonal principal.
A matriz será sempre quadrada (N x N).

ESPECIFICAÇÃO TÉCNICA:
1. Função: `soma_diagonal(matriz)`
2. Entrada: Uma matriz quadrada.
3. Saída: A soma dos elementos `matriz[i][i]`.
"""
    arquivos[f"{path_u9_q3}/resolucao.py"] = "def soma_diagonal(matriz):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u9_q3}/test_resolucao.py"] = """
import pytest
from resolucao import soma_diagonal

def test_soma_diag():
    # Diagonal: 1, 5, 9 -> Soma = 15
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert soma_diagonal(m) == 15

def test_matriz_unitaria():
    m = [[10]]
    assert soma_diagonal(m) == 10
"""

    # --- QUESTÃO 4 ---
    path_u9_q4 = f"{base_dir}/Unidade_09/Questao_04_Batalha_Naval"
    arquivos[f"{path_u9_q4}/README.txt"] = """
================================================================================
                        QUESTÃO 04: BATALHA NAVAL (TIRO CERTO)
================================================================================
CONTEXTO:
Você está jogando Batalha Naval. O tabuleiro é uma matriz.
Os navios são marcados com o número 1 e a água com 0.
O jogador informou uma coordenada de tiro (linha, coluna).
Você deve dizer se ele acertou ("Fogo!") ou errou ("Agua").

ESPECIFICAÇÃO TÉCNICA:
1. Função: `verificar_tiro(tabuleiro, linha, coluna)`
2. Entrada: Matriz, int (linha), int (coluna).
3. Saída: String "Fogo!" se tabuleiro[linha][coluna] for 1, senão "Agua".
4. Cuidado: Se a coordenada for inválida (fora da matriz), levante um erro ou retorne "Erro".
   (Para este exercício, assuma coordenadas válidas, mas é bom saber).
"""
    arquivos[f"{path_u9_q4}/resolucao.py"] = "def verificar_tiro(tabuleiro, linha, coluna):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u9_q4}/test_resolucao.py"] = """
import pytest
from resolucao import verificar_tiro

def test_acerto():
    tab = [
        [0, 0, 0],
        [0, 1, 0]
    ]
    # O navio está na linha 1, coluna 1
    assert verificar_tiro(tab, 1, 1) == "Fogo!"

def test_agua():
    tab = [[1, 0]]
    assert verificar_tiro(tab, 0, 1) == "Agua"
"""

    # --- QUESTÃO 5 ---
    path_u9_q5 = f"{base_dir}/Unidade_09/Questao_05_Transposta"
    arquivos[f"{path_u9_q5}/README.txt"] = """
================================================================================
                        QUESTÃO 05: ESPELHANDO A IMAGEM (Transposta)
================================================================================
CONTEXTO:
Você está fazendo um editor de fotos. Uma operação comum é "transpor" a imagem:
o que é linha vira coluna, e o que é coluna vira linha.

Exemplo: 
[[1, 2],       vira      [[1, 3],
 [3, 4]]                  [2, 4]]

ESPECIFICAÇÃO TÉCNICA:
1. Função: `transpor_matriz(matriz)`
2. Entrada: Uma matriz N x M.
3. Saída: Uma NOVA matriz M x N transposta.
"""
    arquivos[f"{path_u9_q5}/resolucao.py"] = "def transpor_matriz(matriz):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u9_q5}/test_resolucao.py"] = """
import pytest
from resolucao import transpor_matriz

def test_transposta_quadrada():
    m = [[1, 2], [3, 4]]
    res = transpor_matriz(m)
    assert res == [[1, 3], [2, 4]]

def test_transposta_retangular():
    # 2 linhas, 3 colunas -> vira 3 linhas, 2 colunas
    m = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    esperado = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    assert transpor_matriz(m) == esperado
"""

    # =========================================================================
    # UNIDADE 10: MAPAS / DICIONÁRIOS
    # =========================================================================

    # --- QUESTÃO 1 ---
    path_u10_q1 = f"{base_dir}/Unidade_10/Questao_01_Agenda_Telefonica"
    arquivos[f"{path_u10_q1}/README.txt"] = """
================================================================================
                        QUESTÃO 01: A AGENDA TELEFÔNICA
================================================================================
CONTEXTO:
Bem-vindo ao mundo dos dicionários! Em vez de índices numéricos [0], usamos chaves ["nome"].
Você precisa criar uma agenda simples.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `buscar_telefone(agenda, nome)`
2. Entrada: `agenda` (dicionário {nome: telefone}), `nome` (string).
3. Saída: O telefone da pessoa se ela existir, ou a string "Não encontrado" se não existir.
"""
    arquivos[f"{path_u10_q1}/resolucao.py"] = "def buscar_telefone(agenda, nome):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u10_q1}/test_resolucao.py"] = """
import pytest
from resolucao import buscar_telefone

def test_busca_sucesso():
    agenda = {"Ana": "1234-5678", "Beto": "9999-0000"}
    assert buscar_telefone(agenda, "Ana") == "1234-5678"

def test_busca_falha():
    agenda = {"Ana": "1234"}
    assert buscar_telefone(agenda, "Carlos") == "Não encontrado"
"""

    # --- QUESTÃO 2 ---
    path_u10_q2 = f"{base_dir}/Unidade_10/Questao_02_Contador_Votos"
    arquivos[f"{path_u10_q2}/README.txt"] = """
================================================================================
                        QUESTÃO 02: A URNA ELETRÔNICA
================================================================================
CONTEXTO:
Você recebeu uma lista enorme de votos em papel: `["Ana", "Beto", "Ana", "Carlos", "Ana"]`.
Você precisa contar quantos votos cada candidato recebeu.

Dicionários são perfeitos para isso: a chave é o nome, o valor é a contagem.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `contar_votos(lista_votos)`
2. Entrada: Lista de strings.
3. Saída: Um dicionário onde chave=candidato e valor=quantidade.
"""
    arquivos[f"{path_u10_q2}/resolucao.py"] = "def contar_votos(lista_votos):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u10_q2}/test_resolucao.py"] = """
import pytest
from resolucao import contar_votos

def test_contagem():
    votos = ["A", "B", "A", "C", "A", "B"]
    resultado = contar_votos(votos)
    # A=3, B=2, C=1
    assert resultado == {"A": 3, "B": 2, "C": 1}

def test_vazia():
    assert contar_votos([]) == {}
"""

    # --- QUESTÃO 3 ---
    path_u10_q3 = f"{base_dir}/Unidade_10/Questao_03_Tradutor_Simples"
    arquivos[f"{path_u10_q3}/README.txt"] = """
================================================================================
                        QUESTÃO 03: O TRADUTOR DE GÍRIAS
================================================================================
CONTEXTO:
Você quer criar um tradutor que substitui gírias por português formal.
Você tem um dicionário: `{"vc": "você", "tmb": "também"}`.
Receba uma frase e substitua as palavras que estiverem no dicionário. As que não estiverem, mantenha igual.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `traduzir_frase(frase, dicionario)`
2. Entrada: String (frase), Dict (mapa de tradução).
3. Saída: String traduzida.
   Dica: Use `frase.split()` para separar as palavras, verifique cada uma no dict, e depois `join`.
"""
    arquivos[f"{path_u10_q3}/resolucao.py"] = "def traduzir_frase(frase, dicionario):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u10_q3}/test_resolucao.py"] = """
import pytest
from resolucao import traduzir_frase

def test_traducao():
    dicio = {"vc": "você", "kd": "cadê"}
    frase = "oi vc sabe kd o chave?"
    
    # "oi" não está no dict -> mantem "oi"
    # "vc" está -> vira "você"
    # "sabe" não está -> mantem
    # "kd" está -> vira "cadê"
    
    esperado = "oi você sabe cadê o chave?"
    assert traduzir_frase(frase, dicio) == esperado
"""

    # --- QUESTÃO 4 ---
    path_u10_q4 = f"{base_dir}/Unidade_10/Questao_04_Estoque_Loja"
    arquivos[f"{path_u10_q4}/README.txt"] = """
================================================================================
                        QUESTÃO 04: GERENTE DE ESTOQUE
================================================================================
CONTEXTO:
Em uma loja, o estoque é um dicionário: `{"maçã": 10, "uva": 5}`.
Chegou um caminhão com novos produtos. A nota fiscal é outro dicionário: `{"maçã": 5, "banana": 20}`.

Você precisa atualizar o estoque principal.
- Se o produto já existe (maçã), some a quantidade.
- Se é novo (banana), crie a entrada no dicionário.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `atualizar_estoque(estoque_atual, novos_produtos)`
2. Entrada: Dois dicionários.
3. Ação: Modifique o `estoque_atual` IN-PLACE. Não retorne nada.
"""
    arquivos[f"{path_u10_q4}/resolucao.py"] = "def atualizar_estoque(estoque_atual, novos_produtos):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u10_q4}/test_resolucao.py"] = """
import pytest
from resolucao import atualizar_estoque

def test_atualizacao_mista():
    estoque = {"tv": 10, "som": 2}
    chegada = {"tv": 5, "pc": 1}
    
    atualizar_estoque(estoque, chegada)
    
    # tv: 10 + 5 = 15
    # som: 2 (não mudou)
    # pc: 1 (novo)
    assert estoque == {"tv": 15, "som": 2, "pc": 1}
"""

    # --- QUESTÃO 5 ---
    path_u10_q5 = f"{base_dir}/Unidade_10/Questao_05_Matriz_Esparsa"
    arquivos[f"{path_u10_q5}/README.txt"] = """
================================================================================
                        QUESTÃO 05: A MATRIZ ESPARSA (Dicionários + Tuplas)
================================================================================
CONTEXTO:
Imagine uma planilha gigante (1 milhão x 1 milhão) onde quase tudo é zero, exceto alguns valores.
Guardar isso numa matriz `lista de listas` gastaria toda a memória do PC.

Solução: Usar um dicionário onde a CHAVE é uma tupla `(linha, coluna)` e o VALOR é o número.
Ex: `{(0, 5): 10}` significa que na linha 0, coluna 5, tem o valor 10. O resto é zero.

Sua função deve simular o acesso a essa matriz. Se a coordenada existir no dict, retorne o valor.
Se não existir, retorne 0.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `obter_valor(matriz_esparsa, linha, coluna)`
2. Entrada: Dicionário, int, int.
3. Saída: O valor naquela coordenada ou 0.
"""
    arquivos[f"{path_u10_q5}/resolucao.py"] = "def obter_valor(matriz_esparsa, linha, coluna):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u10_q5}/test_resolucao.py"] = """
import pytest
from resolucao import obter_valor

def test_esparsa():
    # Apenas a posição (500, 100) tem valor 99
    dados = {(500, 100): 99}
    
    # Teste 1: Acessar onde tem dado
    assert obter_valor(dados, 500, 100) == 99
    
    # Teste 2: Acessar o vazio (deve ser zero)
    assert obter_valor(dados, 0, 0) == 0
"""

    # Gerar os arquivos
    print(" Expandindo o universo... Criando Unidades 9 e 10...")
    for caminho, conteudo in arquivos.items():
        diretorio = os.path.dirname(caminho)
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo.strip())
        print(f" Criado: {caminho}")

    print("\n ATUALIZAÇÃO CONCLUÍDA! Confira as novas pastas na Unidade 9 e 10.")

if __name__ == "__main__":
    gerar_conteudo_final()
