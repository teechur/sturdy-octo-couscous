def myfunc( mystring, myotherstring ):
    print "First: " + myotherstring + ", Second: " + mystring
myfunc( "rainbow" , "unicorn" )

def mycat( thing1, thing2 ):
  output = "you sent " + thing1 + " and also " + thing2
  return output
  
the_output = mycat( "rainbow", "unicorn" )
print the_output
