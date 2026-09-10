for i in range(0, 5):
    print("iteracion", i)

# range: el 3er valor es el salto: de tanto en tanto salta.
print( list( range(0, 5, 3) ) )
# res = [0, 3]

print( list( range(0, 5, 5) ) )
# res = [0, 5]

print( list( range(0, 5, 0) ) )
# res = [0]

print( list( range(0, 5, 1) ) )
# res = [0 , 1, 2 , 3 , 4 , 5 ]