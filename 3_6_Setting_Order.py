a = 2
b = 4
c = 8

print('\nDefault Order:\t',a,'x',c,'+',b,'=', a*c+b)
print('Forced Order:\t',a,'x (',c,'+',b,') =', a*(c+b))

print('\nDefault Order:\t',c,'//',b,'-',a,'=',c//b - a)
print('Forced Order:\t',c,'//(',b,'-',a,') =',c//(b - a))

print('\nDefault Order:\t',c,'Remainder of ',a,'+',b,'=',c%a+b)
print('Forced Order:\t',c,'Remainder of (',a,'+',b,') =',c%(a+b))

print('\nDefault Order:\t',c,'Exponent of ',a,'+',b,'=',c**a+b)
print('Forced Order:\t',c,'Exponent of (',a,'+',b,') =',c**(a+b))