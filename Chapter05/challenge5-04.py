wow={"身長":"164",
     "水筒":"紫",
     "筆箱":"無印良品"
     }

n=input("何を知りたい、身長、水筒、筆箱の中で:")
if n in wow:
    answer=wow[n]
    print(answer)
else:print("打ち間違った？")

