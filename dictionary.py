1))# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# This was harder than I expected...
print (d['k1'][0]['nest_key'][1][0])


2))# This will be hard and annoying!
d1 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

# Phew
print (d1['k1'][2]['k2'][1]['tough'][2][0])
