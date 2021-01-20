###############################################
# ZORUNLU ODEV 3: List Comprehension Applications
###############################################

###############################################
# Görev 1: car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
###############################################

# Veri setini baştan okutarak aşağıdaki çıktıyı elde etmeye çalışınız.

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notlar:
# Numerik olmayanların da isimleri büyümeli.
# Tek bir list comp yapısı ile yapılmalı.

############################GENEL KOD YAPISI #########################
import seaborn as sns #genel kütüphanlerimi import ettim
import numpy as np
df = sns.load_dataset("car_crashes") #veri setini yükledim
df.head() # ilk değerleri çağırdım

for col in df.columns: #veri setindeki kolonları for döngüsünde gezerek
    print(col.upper()) #istenilen koşul olan harfleri büyütme işlemi yaptım

A = [] #boş bir liste oluşturudum

for col in df.columns:   #değerleri gezdim
    A.append(col.upper()) #append metotu ile A listesine değerlerimi attım
df.columns = A #A listesindeli değerleri df.columns a attım

###############################################
# Görev 1 Çözüm
###############################################
colnames_numerics_only = df.select_dtypes(include=np.number).columns.tolist()
last_wanted = ["NUM_" + col if col in colnames_numerics_only else col for col in df.columns]
print(last_wanted)
#Yukarıdaki koşulumda numerik olan değişkenlerin başına NUM_ getirip,olmayanların
#başına bir şey getirmedim.Bu işlemi gerçekleştirmek için öncelikle verilerimden
#tipi numeric olanları colnames_numerics_only değişkenine attım
#bi aşağısındada koşulu gerçekleştirip yazdırdım.



###############################################
# Görev 2: İsminde "no" BARINDIRMAYAN değişkenlerin isimlerininin SONUNA "FLAG" yazınız.
###############################################
###############################################
# Görev 2 Çözüm
###############################################
df.columns = [ col+"" if "NO" in col else col + "_FLAG" for col in df.columns]
df.columns

###############################################
# Görev 3: Aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçerek yeni bir df oluşturunuz.
###############################################

###############################################
# Görev 3 Çözüm
###############################################
#list değerlerinden istenilen değerleri! og_liste koydum
og_list = ["abbrev", "no_previous"]
#yeni bir oluşum gerçekleştirdim içinde hem for hem if olan
#amacım ise yukarıda og_list te var olan verileri almayayıp yerine yeni
#veri seti oluşturmak!
new_cols=[col for col in df.columns if col not in og_list]
new_df=df[new_cols]
new_df.head() # Yeni oluşturduğum veri setini çağırdım
