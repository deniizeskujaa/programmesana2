def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8") # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()
    return

# ierakstit("Mani sauc D")
    
def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()
    return

# pierakstit_klat("Es esmu programmēšanā")
    
def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

# print(nolasit_visu())

def dabut_rindinas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()
    
    for i in range(len(rindas)):
        rindas[i] = rindas[i].strip()

    return rindas


# saraksts = dabut_rindinas()
# print(saraksts)

# ierakstit("Anna, https://static.twentytwowords.com/wp-content/uploads/10model2-685x685.jpg")
# pierakstit_klat("Katls, https://arkolat.lv/storage/uploads/global/product_images/image/000/055/684/large/ef387b5ad94e9169c7f220dda11f92da.jpg")
# pierakstit_klat("Kartupelis, https://img.medicine.lv/articles/open/1/5/media/users/article/galleries/150/455/15045536.jpg_15045536_600x400.jpg")