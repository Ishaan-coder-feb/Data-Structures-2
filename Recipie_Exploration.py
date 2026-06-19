print("Recipie Explorer!")
pasta=("Alfredo","Penne","Italian",30,"Medium")
bir=("Biryani","Paneer","Indian",60,"Hard")
print("We are making Pasta! Lets look at the recipie details!The sauce we are using for the pasta is",pasta[0]," and the type of pasta we are using is",
      pasta[1],",the cuisine is", pasta[2],"it takes",pasta[3]," minutes to make and the difficulty level is",pasta[4])
print("We are making ",bir[0],"! Lets look at the recipie details!The type of biryani we are making is",bir[1]," and the cuisine is",
      bir[2]," and it takes",bir[3]," minutes to make and the difficulty level is",bir[4])
menu=("Alfredo","Penne","Italian",30,"Medium",("Biryani","Paneer","Indian",60,"Hard"))
print("Some pasta details are",menu[0:3])
pasta_set={"pasta","cheese","milk","cream","water"}
bir_set={"rice","Panneer","onoin","beans","peas","masala"}
print("There are",len(pasta_set)," ingredients in pasta")
print("There are",len(bir_set)," ingredients in biryani")
bir_set.add("salt")
pasta_set.discard("water")
all_ing=pasta_set.union(bir_set)
common_ing=pasta_set.intersection(bir_set)
only_pasta=pasta_set.difference(bir_set)
shr=pasta_set.symmetric_difference(bir_set)
print("All ingerdients combined are",all_ing)
print("The commond ingredients are ",common_ing)
print("The ingredients that are only present in pasta are",only_pasta)
print("The ingredient that are not shared are",shr)



