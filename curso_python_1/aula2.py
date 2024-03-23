# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="-")
print(78, 34, sep='-')
print(44, 64, sep='-') 

print(12, 34, 1011, sep="-", end='\r\n' )
print(78, 34, sep='-', end='\n')
print(44, 64, sep='-', end='\n')

print(12, 34, 1011, sep="-", end='##' )
print(78, 34, sep='-', end='\n')
print(44, 64, sep='-', end='\n')