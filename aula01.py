# BootCamp Klabin Python

print("First Program Python")

# Tipos de Dados

nome = "seu nome"         # str
idade = 23                # int
moeda = "R$"              # str (moeda é texto)
valor = 2333 + 0j         # complex
mapa = {"chave": "valor"} # dict
colecao = {1, 2, 3}       # set
bolleano = True           # bool
binario = b"texto"        # bytes

print(nome, idade, moeda, valor, mapa, colecao, bolleano, binario)


# Tipos de dados com tipagem forte via type hints

nome: str = "seu nome"
idade: int = 23
moeda: str = "R$"
valor: complex = 2333 + 0j
mapa: dict[str, str] = {"chave": "valor"}
colecao: set[int] = {1, 2, 3}
bolleano: bool = True
binario: bytes = b"texto"

print(nome, idade, moeda, valor, mapa, colecao, bolleano, binario)

