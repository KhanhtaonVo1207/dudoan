import tkinter
import customtkinter
attribute_data = data[:,0:2]
label_data = data[:,2]
import pandas as pd
from sklearn import preprocessing
from customtkinter import CTkOptionMenu
#Read data
data_train = pd.read_csv("E:\\BTX\\AI\\webtest\\file\\Dự đoán bóng đá.csv")
#print(data_train)

#Preprocessing main data
data = data_train.values
convert_dataY = preprocessing.LabelEncoder()
convert_dataY.fit(label_data)
Y_train = convert_dataY.transform(label_data)
#print(Y_train)

#Preprocessing other data
#--print(attribute_data)
convert_dataX = preprocessing.OrdinalEncoder()
convert_dataX.fit(attribute_data)
X_train = convert_dataX.transform(attribute_data)
#--print(X_train)

#Using Decision Tree
from sklearn.tree import DecisionTreeClassifier

Dtree_Model = DecisionTreeClassifier()
Dtree_Model.fit(X_train, Y_train)
from matplotlib import pyplot as plt
from sklearn import tree
#tree.plot_tree(Dtree_Model)
#plt.show()
#Command
Arsenal = None
Aston = None
Y_label = None

#System 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
#App
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Dự đoán bóng đá")
#Các hàm
def Team2(option):
    global Aston
    Aston = str(option)
    print(Aston)
def Team1(option):
    global Arsenal
    Arsenal = str(option)
    print(Arsenal)

def hi() :
  
    Team1_input = Arsenal
    Team2_input = Aston
    #Phần quang trọng
    X_test = convert_dataX.transform([(Team1_input,Team2_input)])
    print(X_test)
    Y_test = Dtree_Model.predict(X_test)
    global Y_label
    Y_label = "Thắng"
    if  Y_test[0]==0:Y_label = "Đội Nhà Thắng"
    if  Y_test[0]==1:Y_label = "Đội Nhà Thua"
    if  Y_test[0]==2:Y_label = "Hoà"
    print("Kết quả", Y_test, "-->", Y_label)
    
    K.configure(text = Y_label, width=300, height=80,font=("Arial", 20))
    K.pack()
#Elements
K = customtkinter.CTkLabel(app, width = 100, height = 50, text =Y_label)
title = customtkinter.CTkLabel(app, width = 100, height = 50, text ="Dự đoán giải ngoại hạng Anh",)
title.configure(width=300, height=40,font=("Arial", 30))
title.pack(padx = 10 , pady = 10)
team1 = customtkinter.CTkLabel(app, width = 50, height = 20, text ="Đội Nhà",)
team1.configure(width=100, height=40,font=("Arial", 20))
team1.pack(padx = 5 , pady = 15)
options = ["Arsenal","Aston Villa","Bournemouth","Brentford","Brighton","Burnley","Chelsea","Crystal Palace","Everton","Fulham","Liverpool","Luton","Man City","Man Utd","Newcastle","Forest","Sheffield Utd","Tottenham ","West Ham","Wolves"]
dropdown_1 = CTkOptionMenu(master=app , values=options, command=Team1)
dropdown_2 = CTkOptionMenu(master=app , values=options, command=Team2)
dropdown_1.pack()
team2 = customtkinter.CTkLabel(app, width = 50, height = 20, text ="Đội Khách",)
team2.configure(width=100, height=40,font=("Arial", 20))
team2.pack(padx = 5 , pady = 20)
dropdown_2.pack()
button = customtkinter.CTkButton(app, width = 50, height = 40 , text_color = "white" , text = "Dự Đoán", command =hi)
button.pack(padx = 10 , pady = 50)
#Run
app.mainloop()

