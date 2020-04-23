#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      andela
#
# Created:     23.04.2020
# Copyright:   (c) andela 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

uvozi  matematiku

klasa  Trokut ( objekt ):
    def  __init__ ( samo , a , b , c ):
        ako je ( a > 0  i  b > 0  i  c > 0  i  a + b > c  i  a + c > b  i  b + c > a ):
            sebe . __stranice = [ a , b , c ]
        drugo :
            povisi  ValueError ( 'nema trokuta' )


    def  __str__ ( samo ):
        povratak  "trokut% s% s% s"  % ( samo . __stranice [ 0 ], samo . __stranice [ 1 ], samo . __stranice [ 2 ])

    def  __repr__ ( samo ):
        povratak  "Trokut (% s,% s,% s)"  % ( samo . __stranice [ 0 ], samo . __stranice [ 1 ], samo . __stranice [ 2 ])

    def  opseg ( samo ):
        povratak  sebe . __stranice [ 0 ] + samo . __stranice [ 1 ] + ja . __stranice [ 2 ]

    def  povrsina ( samo ):
        a = ja . __stranice [ 0 ]
        b = ja . __stranice [ 1 ]
        c = ja . __stranice [ 2 ]
        s = ( a + b + c ) / 2

        vratiti  matematiku . sqrt ( s * ( s - a ) * ( s - b ) * ( s - c ))
        # return math.sqrt (((a + b + c) * (- a + b + c) * (a-b + c) * (a + bc)) / 16)


klasa  JednakokracniTrokut ( Trokut ):
    def  __init__ ( samo , a , b ):
        c = b
        super ( JednakokracniTrokut , samo ). __init__ ( a , b , c )



klasa  JednakostranicniTrokut ( Trokut ):
    def  __init__ ( samo , a ):
        b = a
        c = a
        super ( JednakostranicniTrokut , samo ). __init__ ( a , b , c )



ispis ( '*** test 1 ***' )
lista_stranica  = [( 1 , 2 , 3 ), ( 3 , 4 , 5 ), ( 3 , 4 , 4 ), ( 3 , 3 , 3 )]
za  stranice  u  listi_stranica :
    probaj :
        t  =  Trokut ( * stranice )
        ispis ( repr ( t ))
    osim  iznimke  kao  e :
        ispis ( e [ 0 ], stranice )



ispis ( '*** test 2 ***' )
lista_stranica  = [( 3 , 4 , 5 ), ( 3 , 4 , 4 ), ( 3 , 3 , 3 )]
za  stranice  u  listi_stranica :
    t  =  Trokut ( * stranice )
    ispis ( '% r ima opseg% .3f i povrsinu% .3f'  % ( t , t . opseg (), t . povrsina ()))




ispis ( '*** test 3 ***' )
trokuti  = [ Trokut ( 3 , 4 , 5 ), JednakokracniTrokut ( 3 , 4 ), JednakostranicniTrokut ( 5 )]
za  t  u  trokuti :
    ispis ( t )