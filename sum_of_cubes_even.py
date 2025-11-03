def sum_of_cubes_even(n):
    if n>2000:
        print("warning: n>2000!")
    if n<0 or type(n)!=int:
        return -1
    evenNumbers=range(0,n+1,2)
    total = 0
    for evenNumber in evenNumbers:
        cube = float(evenNumber **3)
        total = total + cube
    return total