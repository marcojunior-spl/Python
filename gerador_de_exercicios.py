import os

# Função auxiliar para criar a estrutura
def gerar_conteudo():
    base_dir = "Lista_Exercicios_StoryMode"
    
    # Dicionário gigante com toda a estrutura
    # Chave = Caminho do arquivo
    # Valor = Conteúdo do arquivo
    arquivos = {}

    # =========================================================================
    # UNIDADE 06: EFEITOS COLATERAIS (O MUNDO REAL)
    # =========================================================================
    
    # --- QUESTÃO 1 ---
    path_u6_q1 = f"{base_dir}/Unidade_06/Questao_01_Robo_Logistico"
    arquivos[f"{path_u6_q1}/README.txt"] = """
================================================================================
                        QUESTÃO 01: O COLAPSO DO ROBÔ XP-2000
================================================================================

CONTEXTO:
Você é o Engenheiro Chefe de Software da Amazonia Logistics. Ontem à noite, uma tempestade 
elétrica fritou os sensores do nosso principal robô de triagem, o XP-2000.

O robô começou a alucinar e está registrando caixas que não existem, marcando-as com 
códigos negativos (ex: -542) ou códigos nulos (0) no banco de dados de remessas.

O problema é crítico: o sistema central que controla o robô é um mainframe legado dos anos 90 
com pouquíssima memória RAM. Se tentarmos criar uma nova lista filtrada copiando os dados, 
o sistema vai estourar a memória (Memory Overflow) e a fábrica vai parar.

SUA MISSÃO:
Você precisa limpar a lista de remessas atual DIRETAMENTE na memória onde ela já reside.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `limpar_estoque(codigos)`
2. Entrada: Uma lista de inteiros (ex: `[102, -50, 0, 200]`).
3. Comportamento: Remover todos os valores menores ou iguais a zero.
4. RESTRIÇÃO OBRIGATÓRIA: A alteração deve ser IN-PLACE (na própria lista). 
   A função NÃO deve retornar nada (None).
"""
    arquivos[f"{path_u6_q1}/resolucao.py"] = "def limpar_estoque(codigos):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u6_q1}/test_resolucao.py"] = """
import pytest
from resolucao import limpar_estoque

def test_remocao_basica():
    lista = [100, -50, 200, 0, 300]
    limpar_estoque(lista)
    assert lista == [100, 200, 300], "O robô não limpou os dados corretamente."

def test_memoria_in_place():
    lista = [10, -10]
    memoria_antes = id(lista)
    retorno = limpar_estoque(lista)
    memoria_depois = id(lista)
    
    assert retorno is None, "A função não deve retornar nada (deve ser void)."
    assert memoria_antes == memoria_depois, "Você criou uma nova lista! O Mainframe vai explodir."

def test_bug_dos_indices_consecutivos():
    # Teste para ver se o aluno sabe lidar com o deslocamento de índices
    lista = [10, -1, -2, -3, 20]
    limpar_estoque(lista)
    assert lista == [10, 20], "Falha ao remover sequências de erros (-1, -2, -3)."
"""

    # --- QUESTÃO 2 ---
    path_u6_q2 = f"{base_dir}/Unidade_06/Questao_02_Sindicato"
    arquivos[f"{path_u6_q2}/README.txt"] = """
================================================================================
                        QUESTÃO 02: A VITÓRIA DO SINDICATO
================================================================================

CONTEXTO:
Após semanas de greve, o Sindicato dos Desenvolvedores e Afins conseguiu uma vitória histórica.
Ficou acordado que a desigualdade salarial na empresa deve diminuir.

A regra estipulada no contrato coletivo é clara: 
"Todo funcionário cujo salário base seja estritamente inferior a R$ 2.000,00 deverá receber 
um reajuste imediato de 10% sobre o valor atual."

O RH precisa processar isso hoje antes do fechamento bancário. Eles te enviaram a lista bruta 
dos salários. Como a lista é usada por outros departamentos em tempo real, você deve atualizar 
os valores na própria lista compartilhada.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `aplicar_aumento(salarios)`
2. Entrada: Lista de floats.
3. Lógica: Para cada salário < 2000.0, multiplique por 1.10.
4. RESTRIÇÃO: Modificação IN-PLACE.
"""
    arquivos[f"{path_u6_q2}/resolucao.py"] = "def aplicar_aumento(salarios):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u6_q2}/test_resolucao.py"] = """
import pytest
from resolucao import aplicar_aumento

def test_calculo_aumento():
    folha = [1500.0, 3000.0, 1000.0]
    aplicar_aumento(folha)
    # 1500 * 1.1 = 1650 | 3000 mantem | 1000 * 1.1 = 1100
    assert folha == pytest.approx([1650.0, 3000.0, 1100.0]), "Erro matemático no reajuste."

def test_limite_exato():
    folha = [2000.0, 1999.0]
    aplicar_aumento(folha)
    # 2000 não ganha (é estritamente menor). 1999 ganha.
    assert folha[0] == 2000.0, "Quem ganha 2000 não deveria receber aumento."
    assert folha[1] > 1999.0, "Quem ganha 1999 deveria receber aumento."
"""

    # --- QUESTÃO 3 ---
    path_u6_q3 = f"{base_dir}/Unidade_06/Questao_03_Estagiario_RH"
    arquivos[f"{path_u6_q3}/README.txt"] = """
================================================================================
                        QUESTÃO 03: O ESTAGIÁRIO E OS CRACHÁS
================================================================================

CONTEXTO:
Contratamos um estagiário para digitar os nomes dos novos funcionários no sistema de crachás.
Infelizmente, a tecla 'Shift' do teclado dele estava quebrada (ou ele estava com preguiça).

O banco de dados está uma bagunça:
- "ana maria"
- "JOAO SILVA"
- "pEdRo hEnRiQuE"

O CEO vai visitar a empresa amanhã e os crachás precisam ser impressos com formatação profissional.
Cada nome na lista deve ter apenas a primeira letra maiúscula e o restante minúscula (Capitalize).

ESPECIFICAÇÃO TÉCNICA:
1. Função: `corrigir_nomes(nomes)`
2. Entrada: Lista de strings.
3. Comportamento: Transformar cada string da lista usando lógica de capitalização.
4. RESTRIÇÃO: Modificação IN-PLACE.
"""
    arquivos[f"{path_u6_q3}/resolucao.py"] = "def corrigir_nomes(nomes):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u6_q3}/test_resolucao.py"] = """
import pytest
from resolucao import corrigir_nomes

def test_normalizacao_mista():
    lista = ["ana", "CARLOS", "bEaTrIz"]
    corrigir_nomes(lista)
    esperado = ["Ana", "Carlos", "Beatriz"]
    assert lista == esperado, f"Formatação incorreta. Esperado {esperado}, obteve {lista}"
"""

    # --- QUESTÃO 4 ---
    path_u6_q4 = f"{base_dir}/Unidade_06/Questao_04_Censura_Chat"
    arquivos[f"{path_u6_q4}/README.txt"] = """
================================================================================
                        QUESTÃO 04: O GUARDIÃO DO CHAT
================================================================================

CONTEXTO:
Você trabalha para uma empresa de jogos online voltada para o público infantil.
Recentemente, pais reclamaram que palavras inadequadas estão aparecendo no chat global.

Você precisa implementar um filtro de censura em tempo real. O servidor recebe um lote de mensagens
e uma "blacklist" de palavras proibidas. Como o chat é muito rápido, não podemos criar cópias
das mensagens. A censura deve ocorrer substituindo a palavra ofensiva diretamente na lista de mensagens
por quatro asteriscos "****".

ESPECIFICAÇÃO TÉCNICA:
1. Função: `censurar_chat(mensagens, termos_proibidos)`
2. Entrada: `mensagens` (lista de strings), `termos_proibidos` (lista de strings).
3. Comportamento: Se uma mensagem for EXATAMENTE igual a um termo proibido, substitua-a por "****".
4. RESTRIÇÃO: Modificação IN-PLACE na lista `mensagens`.
"""
    arquivos[f"{path_u6_q4}/resolucao.py"] = "def censurar_chat(mensagens, termos_proibidos):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u6_q4}/test_resolucao.py"] = """
import pytest
from resolucao import censurar_chat

def test_censura_ativa():
    msgs = ["bom dia", "feio", "legal", "bobo"]
    proibidas = ["feio", "bobo", "chato"]
    
    censurar_chat(msgs, proibidas)
    
    assert msgs == ["bom dia", "****", "legal", "****"], "A censura falhou em ocultar palavras."

def test_censura_parcial():
    # Verifica se ele censura apenas a palavra exata (requisito simples)
    msgs = ["feio demais"]
    proibidas = ["feio"]
    censurar_chat(msgs, proibidas)
    # Como a string é "feio demais" e a proibida é "feio", e o enunciado diz "igual a", não deve mudar.
    # (Se o enunciado pedisse 'contém', seria diferente).
    assert msgs == ["feio demais"], "Censurou string que continha a palavra mas não era igual."
"""

    # --- QUESTÃO 5 ---
    path_u6_q5 = f"{base_dir}/Unidade_06/Questao_05_Sistema_Legado"
    arquivos[f"{path_u6_q5}/README.txt"] = """
================================================================================
                        QUESTÃO 05: A VOLTA DOS INTEIROS
================================================================================

CONTEXTO:
O sistema de boletins da escola foi migrado para um banco de dados SQL muito antigo que não
suporta números decimais (ponto flutuante) na coluna de notas finais. Se tentarmos salvar "7.8",
o banco trava.

O diretor decidiu: "Vamos arredondar tudo para o inteiro mais próximo antes de salvar".
Você tem a lista de notas finais em memória e precisa convertê-las para inteiros (`int`) usando
a regra de arredondamento padrão da matemática (round).

ESPECIFICAÇÃO TÉCNICA:
1. Função: `arredondar_notas(notas)`
2. Entrada: Lista de floats.
3. Comportamento: Substituir cada float pelo seu arredondamento inteiro (`round()`).
   Ex: 7.2 -> 7, 7.8 -> 8.
4. RESTRIÇÃO: Modificação IN-PLACE. A lista deve passar a conter inteiros, não floats.
"""
    arquivos[f"{path_u6_q5}/resolucao.py"] = "def arredondar_notas(notas):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u6_q5}/test_resolucao.py"] = """
import pytest
from resolucao import arredondar_notas

def test_arredondamento_tipos():
    notas = [7.1, 7.9, 5.5]
    arredondar_notas(notas)
    
    assert notas == [7, 8, 6], f"Valores incorretos: {notas}"
    assert all(isinstance(x, int) for x in notas), "Os elementos da lista devem ser do tipo int, não float."
"""

    # =========================================================================
    # UNIDADE 07: FUNÇÕES PURAS (SEGURANÇA DE DADOS)
    # =========================================================================
    
    # --- QUESTÃO 1 ---
    path_u7_q1 = f"{base_dir}/Unidade_07/Questao_01_Black_Friday"
    arquivos[f"{path_u7_q1}/README.txt"] = """
================================================================================
                        QUESTÃO 01: O FILTRO DA BLACK FRIDAY
================================================================================

CONTEXTO:
É Black Friday! Milhares de usuários estão acessando seu e-commerce. 
O usuário João configurou um filtro: "Quero ver apenas produtos até R$ 100,00".

Temos a lista mestre de preços de todos os produtos da loja. Você precisa entregar para o João
uma lista personalizada.
PORÉM, CUIDADO! Se você alterar a lista mestre (removendo os itens caros), os outros usuários
vão parar de ver os produtos caros também. Isso seria um prejuízo milionário.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `filtrar_ofertas(precos, teto)`
2. Entrada: Lista de preços (floats) e valor máximo (float).
3. Saída: Uma NOVA lista contendo apenas os preços <= teto.
4. RESTRIÇÃO: Função PURA. A lista `precos` original deve permanecer INTACTA.
"""
    arquivos[f"{path_u7_q1}/resolucao.py"] = "def filtrar_ofertas(precos, teto):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u7_q1}/test_resolucao.py"] = """
import pytest
from resolucao import filtrar_ofertas

def test_pureza_da_funcao():
    precos = [10.0, 50.0, 90.0, 200.0]
    copia_seguranca = precos[:]
    
    resultado = filtrar_ofertas(precos, 80.0)
    
    assert resultado == [10.0, 50.0], "O filtro não funcionou."
    assert precos == copia_seguranca, "CRÍTICO: Você alterou a lista original de preços da loja!"
"""

    # --- QUESTÃO 2 ---
    path_u7_q2 = f"{base_dir}/Unidade_07/Questao_02_Cambio_Dolar"
    arquivos[f"{path_u7_q2}/README.txt"] = """
================================================================================
                        QUESTÃO 02: EXPANSÃO INTERNACIONAL
================================================================================

CONTEXTO:
Sua startup brasileira acaba de abrir vendas para os Estados Unidos.
O banco de dados armazena tudo em Reais (BRL). Para exibir no site americano, precisamos
converter os preços para Dólares (USD) em tempo de execução.

Você receberá a tabela de preços em reais e a taxa de câmbio do dia.
Sua função deve gerar a tabela de preços para o site gringo. Obviamente, não podemos converter
a lista original, senão os clientes brasileiros vão começar a ver preços em dólares e pagar errado.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `converter_tabela(precos_brl, taxa_cambio)`
2. Entrada: Lista de floats e a taxa (float).
3. Saída: NOVA lista onde cada elemento é `preco / taxa`.
4. RESTRIÇÃO: Função Pura.
"""
    arquivos[f"{path_u7_q2}/resolucao.py"] = "def converter_tabela(precos_brl, taxa_cambio):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u7_q2}/test_resolucao.py"] = """
import pytest
from resolucao import converter_tabela

def test_conversao():
    reais = [50.0, 100.0]
    taxa = 5.0
    dolares = converter_tabela(reais, taxa)
    
    assert dolares == [10.0, 20.0], "Cálculo de conversão incorreto."
    assert reais == [50.0, 100.0], "Erro: Lista original foi modificada."
"""

    # --- QUESTÃO 3 ---
    path_u7_q3 = f"{base_dir}/Unidade_07/Questao_03_Lead_Marketing"
    arquivos[f"{path_u7_q3}/README.txt"] = """
================================================================================
                        QUESTÃO 03: INTELIGÊNCIA DE MARKETING
================================================================================

CONTEXTO:
O time de marketing coletou e-mails de milhares de participantes em um evento tech.
A lista está assim: `["joao@google.com", "maria@amazon.com", "pedro@startup.io"]`.

Eles querem fazer uma análise de mercado para saber quais EMPRESAS estavam presentes.
Para isso, precisam que você extraia apenas o domínio de cada e-mail (a parte depois do '@').
Eles precisam dessa lista de domínios separada para gerar gráficos.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `extrair_dominios(emails)`
2. Entrada: Lista de strings (emails).
3. Saída: NOVA lista contendo apenas os domínios.
   Ex: "ana@uol.com.br" -> "uol.com.br"
4. RESTRIÇÃO: Função Pura. Use manipulação de strings (split).
"""
    arquivos[f"{path_u7_q3}/resolucao.py"] = "def extrair_dominios(emails):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u7_q3}/test_resolucao.py"] = """
import pytest
from resolucao import extrair_dominios

def test_extract():
    emails = ["user@gmail.com", "dev@python.org"]
    dominios = extrair_dominios(emails)
    
    assert dominios == ["gmail.com", "python.org"], "Erro ao extrair domínio."
    assert len(dominios) == len(emails)
"""

    # --- QUESTÃO 4 ---
    path_u7_q4 = f"{base_dir}/Unidade_07/Questao_04_Analise_Logs"
    arquivos[f"{path_u7_q4}/README.txt"] = """
================================================================================
                        QUESTÃO 04: O CAÇADOR DE FALHAS
================================================================================

CONTEXTO:
O servidor caiu às 3 da manhã. O arquivo de log tem 1 milhão de linhas misturadas:
- "INFO: Usuário logou"
- "WARNING: Uso de memória alto"
- "ERRO: Falha na conexão DB"
- "INFO: Backup realizado"

O time de SRE (Site Reliability Engineering) precisa de uma ferramenta que receba essa lista bruta
e retorne uma lista contendo APENAS as linhas que começam com "ERRO". Isso vai acelerar o diagnóstico.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `filtrar_erros(logs)`
2. Entrada: Lista de strings.
3. Saída: NOVA lista filtrada (apenas strings que iniciam com "ERRO").
4. RESTRIÇÃO: Função Pura.
"""
    arquivos[f"{path_u7_q4}/resolucao.py"] = "def filtrar_erros(logs):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u7_q4}/test_resolucao.py"] = """
import pytest
from resolucao import filtrar_erros

def test_filtro_log():
    logs = ["INFO: A", "ERRO: DB Crash", "WARNING: B", "ERRO: Timeout"]
    erros = filtrar_erros(logs)
    
    assert erros == ["ERRO: DB Crash", "ERRO: Timeout"], "Filtro de erros falhou."
    assert len(logs) == 4, "A lista original de logs não deve ser tocada."
"""

    # --- QUESTÃO 5 ---
    path_u7_q5 = f"{base_dir}/Unidade_07/Questao_05_Imobiliaria"
    arquivos[f"{path_u7_q5}/README.txt"] = """
================================================================================
                        QUESTÃO 05: A CALCULADORA DE LOTES
================================================================================

CONTEXTO:
Uma imobiliária está vendendo um loteamento onde todos os terrenos são perfeitamente quadrados.
O corretor tem uma lista apenas com a medida do lado de cada terreno (em metros).

Para colocar no catálogo, ele precisa da ÁREA (metros quadrados) de cada um.
Como ele não sabe fazer conta, pediu para você criar um script que recebe a lista de lados
e devolve a lista de áreas calculadas.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `calcular_areas(lados)`
2. Entrada: Lista de números (lados).
3. Saída: NOVA lista com as áreas (lado * lado).
4. RESTRIÇÃO: Função Pura.
"""
    arquivos[f"{path_u7_q5}/resolucao.py"] = "def calcular_areas(lados):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u7_q5}/test_resolucao.py"] = """
import pytest
from resolucao import calcular_areas

def test_area_quadrada():
    lados = [2, 5, 10]
    areas = calcular_areas(lados)
    assert areas == [4, 25, 100], "Cálculo de área incorreto."
"""

    # =========================================================================
    # UNIDADE 08: ALGORITMOS E ARRAYS (A CIÊNCIA DA COMPUTAÇÃO)
    # =========================================================================
    
    # --- QUESTÃO 1 ---
    path_u8_q1 = f"{base_dir}/Unidade_08/Questao_01_Bubble_Sort"
    arquivos[f"{path_u8_q1}/README.txt"] = """
================================================================================
                        QUESTÃO 01: A MESA DO BIBLIOTECÁRIO
================================================================================

CONTEXTO:
Imagine que você é um bibliotecário organizando uma pilha de livros pesados sobre uma mesa.
A mesa está cheia, não há espaço livre para espalhar os livros.
Para ordenar os livros (por código numérico), a única coisa que você consegue fazer fisicamente
é pegar DOIS livros vizinhos (um do lado do outro), comparar seus códigos, e trocá-los de lugar
se estiverem na ordem errada.

Você deve repetir esse processo, percorrendo a mesa várias vezes, até que nenhum livro precise
mais ser trocado. Esse é o algoritmo "Bubble Sort".

ESPECIFICAÇÃO TÉCNICA:
1. Função: `organizar_livros(codigos)`
2. Entrada: Lista de inteiros.
3. Comportamento: Ordenar a lista de forma CRESCENTE usando apenas trocas de elementos adjacentes.
   (Lógica de laços aninhados).
4. RESTRIÇÃO: In-place. Não use `lista.sort()`.
"""
    arquivos[f"{path_u8_q1}/resolucao.py"] = "def organizar_livros(codigos):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u8_q1}/test_resolucao.py"] = """
import pytest
from resolucao import organizar_livros

def test_bubble_sort_basico():
    lista = [5, 1, 4, 2, 8]
    organizar_livros(lista)
    assert lista == [1, 2, 4, 5, 8], "A lista não foi ordenada corretamente."

def test_pior_caso():
    lista = [3, 2, 1]
    organizar_livros(lista)
    assert lista == [1, 2, 3], "Falhou na lista invertida."
"""

    # --- QUESTÃO 2 ---
    path_u8_q2 = f"{base_dir}/Unidade_08/Questao_02_Selection_Parcial"
    arquivos[f"{path_u8_q2}/README.txt"] = """
================================================================================
                        QUESTÃO 02: O CAMPEÃO DA OLIMPÍADA
================================================================================

CONTEXTO:
Na premiação da Olimpíada de Matemática, o diretor quer chamar o aluno com a MAIOR nota para
subir no pódio (posição 0 da fila). O resto da fila não importa agora, ele só quer garantir
que o melhor aluno esteja na frente.

Seu algoritmo deve varrer a lista, encontrar quem tem a nota mais alta, e trocar essa pessoa
de lugar com quem estiver ocupando a primeira posição (índice 0).

ESPECIFICAÇÃO TÉCNICA:
1. Função: `destacar_melhor(notas)`
2. Entrada: Lista de floats.
3. Comportamento: Encontre o valor máximo e faça o swap (troca) com o índice 0.
4. RESTRIÇÃO: In-place. Apenas o índice 0 precisa estar garantido como o maior.
"""
    arquivos[f"{path_u8_q2}/resolucao.py"] = "def destacar_melhor(notas):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u8_q2}/test_resolucao.py"] = """
import pytest
from resolucao import destacar_melhor

def test_selection_top():
    notas = [5.0, 9.5, 2.0, 8.0]
    destacar_melhor(notas)
    assert notas[0] == 9.5, "A maior nota não foi para o índice 0."
    assert len(notas) == 4, "Elementos sumiram da lista."
    assert 5.0 in notas, "A nota que estava em 0 foi sobrescrita em vez de trocada."
"""

    # --- QUESTÃO 3 ---
    path_u8_q3 = f"{base_dir}/Unidade_08/Questao_03_Insertion_Logic"
    arquivos[f"{path_u8_q3}/README.txt"] = """
================================================================================
                        QUESTÃO 03: ORGANIZANDO O BARALHO
================================================================================

CONTEXTO:
Você está jogando cartas. Sua mão já está perfeitamente ordenada: `[2, 4, 7, 10]`.
Você compra uma nova carta do monte: um `5`.

Para não bagunçar sua mão, você não joga o 5 no final e reordena tudo. Você procura visualmente
a posição exata entre o 4 e o 7 e "insere" o 5 ali.
Você deve replicar essa lógica. Dada uma lista JÁ ORDENADA e um novo número, insira-o na posição correta.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `insere_ordenado(lista, numero)`
2. Entrada: Lista de inteiros (ordenada) e um inteiro novo.
3. Comportamento: Inserir o elemento na posição que mantém a ordem.
   Dica: Use `lista.insert(indice, valor)`.
4. RESTRIÇÃO: Modificar a lista original.
"""
    arquivos[f"{path_u8_q3}/resolucao.py"] = "def insere_ordenado(lista, numero):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u8_q3}/test_resolucao.py"] = """
import pytest
from resolucao import insere_ordenado

def test_insercao_meio():
    mao = [2, 4, 7, 10]
    insere_ordenado(mao, 5)
    assert mao == [2, 4, 5, 7, 10], "Inserção na posição errada."

def test_insercao_inicio():
    mao = [10, 20]
    insere_ordenado(mao, 5)
    assert mao == [5, 10, 20], "Falhou ao inserir no início."
"""

    # --- QUESTÃO 4 ---
    path_u8_q4 = f"{base_dir}/Unidade_08/Questao_04_Inversao_Manual"
    arquivos[f"{path_u8_q4}/README.txt"] = """
================================================================================
                        QUESTÃO 04: A INVERSÃO DA ESTANTE
================================================================================

CONTEXTO:
O cliente da livraria é excêntrico. Ele viu a estante ordenada de A a Z e odiou.
"Quero de Z a A!", gritou ele.

Você precisa inverter a ordem dos livros na prateleira.
Mas atenção: a prateleira é apertada. Você não pode tirar todos os livros e colocar em outra mesa.
Você tem que inverter ali mesmo, trocando o primeiro com o último, o segundo com o penúltimo, etc.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `inverter_estante(livros)`
2. Entrada: Lista de qualquer coisa.
3. Comportamento: Inverter a ordem dos elementos.
4. RESTRIÇÃO: In-place. PROIBIDO usar `livros.reverse()` ou `livros[::-1]`.
   Use laço `while` ou `for` manipulando índices opostos (início e fim).
"""
    arquivos[f"{path_u8_q4}/resolucao.py"] = "def inverter_estante(livros):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u8_q4}/test_resolucao.py"] = """
import pytest
from resolucao import inverter_estante

def test_inversao_manual():
    l = ["A", "B", "C", "D"]
    id_original = id(l)
    inverter_estante(l)
    
    assert l == ["D", "C", "B", "A"], "A lista não foi invertida."
    assert id(l) == id_original, "Você criou uma nova lista em vez de inverter in-place."

def test_inversao_impar():
    l = [1, 2, 3]
    inverter_estante(l)
    assert l == [3, 2, 1], "Erro com lista de tamanho ímpar."
"""

    # --- QUESTÃO 5 ---
    path_u8_q5 = f"{base_dir}/Unidade_08/Questao_05_Merge_Filas"
    arquivos[f"{path_u8_q5}/README.txt"] = """
================================================================================
                        QUESTÃO 05: A FUSÃO DE FILAS (MERGE)
================================================================================

CONTEXTO:
No banco, existem duas filas para o caixa: a fila A e a fila B.
Ambas as filas já estão ordenadas por prioridade (senha 1, senha 3, senha 5...).
De repente, um caixa fecha e as duas filas precisam virar uma só, mantendo a ordem de prioridade.

Você deve pegar as duas filas e "fundi-las" (Merge) em uma nova fila única.
Você olha para o primeiro da fila A e o primeiro da fila B. Quem tem a senha menor entra na nova fila.
Repete-se até acabar as filas.

ESPECIFICAÇÃO TÉCNICA:
1. Função: `fundir_filas(fila_a, fila_b)`
2. Entrada: Duas listas de inteiros JÁ ORDENADAS.
3. Saída: Uma NOVA lista contendo a união ordenada.
4. RESTRIÇÃO: Não vale apenas somar as listas e dar sort (`(a+b).sort()`). Isso é ineficiente.
   Use a lógica de comparação de cabeças de lista (algoritmo Merge).
"""
    arquivos[f"{path_u8_q5}/resolucao.py"] = "def fundir_filas(fila_a, fila_b):\n    # Escreva seu código aqui\n    pass"
    arquivos[f"{path_u8_q5}/test_resolucao.py"] = """
import pytest
from resolucao import fundir_filas

def test_merge_classico():
    a = [1, 3, 5]
    b = [2, 4, 6]
    res = fundir_filas(a, b)
    assert res == [1, 2, 3, 4, 5, 6], "Erro na fusão das filas."

def test_tamanhos_diferentes():
    a = [10, 20]
    b = [1, 2, 3, 4, 5]
    res = fundir_filas(a, b)
    assert res == [1, 2, 3, 4, 5, 10, 20], "Erro ao fundir filas de tamanhos diferentes."
"""

    # Gerar os arquivos
    print("🚀 Iniciando a construção do 'Story Mode'...")
    for caminho, conteudo in arquivos.items():
        diretorio = os.path.dirname(caminho)
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo.strip())
        print(f"✅ Criado: {caminho}")

    print("\n✨ CONCLUÍDO! Pasta 'Lista_Exercicios_StoryMode' criada com sucesso.")

if __name__ == "__main__":
    gerar_conteudo()
