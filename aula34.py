"""
https://docs.python.org/3/library/stdtypes.html
TIpos built in (que ja vem)
Imutáveis (vistos até agora): str, int, float, bool
"""
string = "daniel Carvalho"
string_2 = f"{string[:3]}ABC{string[4:]}"
# string[3] = 'ABC' # Não pode, é imutável
print(string_2)
print(string_2.capitalize())