


df=pd.read_csv("OnlineRetail.csv",encoding="ISO-8859-1")
df.head()
df.shape
df.isnull().sum()

df.dropna(subset=["CustomerID"],inplace=True)

df.dropna(subset=["Description"],inplace=True)

#Ülkelerin çoktan aza satış miktarı.
df.groupby("Country")["Quantity"].sum().sort_values(ascending=False)
#en çok satış yapan ülke.
df.groupby("CustomerID")["Quantity"].sum().idxmax()
df.groupby("CustomerID")["Quantity"].sum().sort_values(ascending=False).head(1)
df.groupby("CustomerID")["gelir"].sum().sort_values(ascending=False).head(1)

df.info()

df.groupby("Description")["UnitPrice"].max().sort_values(ascending=False).head()


df.describe().T

#Toplam gelir satış adedi*satış fiyatı
df["gelir"]=df["Quantity"]*df["UnitPrice"]
#Ülkelerin gelir kazancına göre sıralama.
df.groupby("Country")["gelir"].sum().sort_values(ascending=False).head()

df.head()
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
df["Year"]=df["InvoiceDate"].dt.year
df["Month"]=df["InvoiceDate"].dt.month
df["Day"] = df["InvoiceDate"].dt.day

df["InvoiceDate"].max()
df["InvoiceDate"].min()



df.groupby("Month")["Quantity"].sum().sort_values(ascending=False)
df.groupby("Year")["Quantity"].sum().sort_values(ascending=False)
df.groupby("Day")["Quantity"].sum().sort_values(ascending=False)
df.groupby("Month")["gelir"].sum().idxmax()
df.groupby("Year")["gelir"].sum().idxmax()

df_a=df.groupby("Month")[["Quantity","gelir"]].sum().reset_index()

df_a["ürün_b_g"]=df_a["gelir"]/df_a["Quantity"]


df_a.sort_values(by="ürün_b_g",ascending=False)

df.head()
df_b=df.groupby("Month").agg({"gelir":"sum","CustomerID":"count"}).reset_index()

df_b["A"]=df_b["gelir"]/df_b["CustomerID"]

df_c=df.groupby("Month").agg({"gelir":"sum","CustomerID":"count","Quantity":"sum"})


#En çok gelir getiren ürün.
df.groupby("Description")["gelir"].sum().sort_values(ascending=False).head()

#Fiyat ile satış adedi arasında ilişki var mı ?
df["UnitPrice"].corr(df["Quantity"])

