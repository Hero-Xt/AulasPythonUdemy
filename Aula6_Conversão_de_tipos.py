# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo m outro
# tipos imutãveis e primitivos:
# str, int, float, bool

print(1 + 1)
# print("1" + 1) erro
print("a" + "b") #concatenação

print("1", type("1"), sep=" - ")

#coerção
print(int("1"), type(int("1")), sep=" - ")
print(int('1') + 1)
print(float("1") + 1)
print(str(11)+"b")
