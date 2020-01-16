import pandas as pd
from matplotlib import pyplot as plt
import os,signal

#displaying starting msg function
def first(program_name = 'DENTAL RECORD',programmer_name = 'Sunil Ghimire',student_ID = '1EW14CS138'):
    for i in range(100):
        print("*",end='')

    print(f"\nHello welcome to my Program \"{program_name}\"\n My name is \"{programmer_name}\"\n My student ID is : \"{student_ID}\"" )

    for i in range(100):
        print("*",end='')

#extracting data from csv file and storing
data = pd.read_csv('addresses.csv')
total_childern = len(data.index)
never_lost_tooth = data['Total_teeth_lost'].eq(0).sum()
one_lost_tooth = data['Total_teeth_lost'].eq(1).sum()
all_baby_tooth_lost = data['Total_teeth_lost'].eq(20).sum()
expend = total_childern - one_lost_tooth - never_lost_tooth
teeth = data['Total_teeth_lost'].sum()
tas = data['State'].eq('TAS').sum()
qld = data['State'].eq('QLD').sum()
wa = data['State'].eq('WA').sum()
nsw = data['State'].eq('NSW').sum()
sa = data['State'].eq('SA').sum()
vic = data['State'].eq('VIC').sum()
nt = data['State'].eq('NT').sum()
act = data['State'].eq('ACT').sum()

#this function displays the details of children and their tooth
def statics():
    print(f"Total number of children on list : {total_childern} ")
    print(f"Average number of teeth claims over the years : {teeth / total_childern}")
    print(f"Number of children who have never lost a tooth : {never_lost_tooth} ")
    print(f"Number of children who have lost all their baby teeth : {all_baby_tooth_lost} ")
    print(f"Total expenditure for this year : ${expend * 0.50+one_lost_tooth} ")

#this function backups in file.txt based on user input
def export_childrens():
    file_name = input("Enter new file name : \n")
    with open(f'{file_name}.txt', 'w') as f:
        f.write(f'17 children have been saved in {file_name}.txt ')
        print(f'{never_lost_tooth} children have been saved in {file_name}.txt ')

#ploting the graph using matplotlib
def claims_per_state():
    num_of_children = [tas,qld,wa,nsw,sa,vic,nt,act]
    labels = ['TAS','QLD','WA','NSW','SA','VIC','NT','ACT']
    plt.xticks(range(len(num_of_children)), labels)
    plt.xlabel('States')
    plt.ylabel('Number of Childrens ')
    plt.title('Number of children per State')
    plt.bar(range(len(num_of_children)), num_of_children)
    plt.show()

#this function will get the user input and then compare that and displays the bar graph
def compare():
    d = {}
    e = {}

    #storing value in d dict
    d['tas'] = data.loc[data['State'].eq('TAS'), 'Total_teeth_lost'].sum()
    d['qld'] = data.loc[data['State'].eq('QLD'), 'Total_teeth_lost'].sum()
    d['wa'] = data.loc[data['State'].eq('WA'), 'Total_teeth_lost'].sum()
    d['nsw'] = data.loc[data['State'].eq('NSW'), 'Total_teeth_lost'].sum()
    d['sa'] = data.loc[data['State'].eq('SA'), 'Total_teeth_lost'].sum()
    d['vic'] = data.loc[data['State'].eq('VIC'), 'Total_teeth_lost'].sum()
    d['nt'] = data.loc[data['State'].eq('NT'), 'Total_teeth_lost'].sum()
    d['act'] = data.loc[data['State'].eq('ACT'), 'Total_teeth_lost'].sum()
    f_state = input("Enter first state (TAS/QLD/WA/NSW/SA/VIC/NT) : \n").lower()
    s_state = input("Enter second state (TAS/QLD/WA/NSW/SA/VIC/NT) : \n").lower()

    #storing value in e dict
    e['tas'] = data['State'].eq('TAS').sum()
    e['qld'] = data['State'].eq('QLD').sum()
    e['wa'] = data['State'].eq('WA').sum()
    e['nsw'] = data['State'].eq('NSW').sum()
    e['sa'] = data['State'].eq('SA').sum()
    e['vic'] = data['State'].eq('VIC').sum()
    e['nt'] = data['State'].eq('NT').sum()
    e['act'] = data['State'].eq('ACT').sum()
    x = [f_state.upper(),s_state.upper()]
    y = [d[f_state]/e[f_state],d[s_state]/e[s_state]]
    plt.ylabel('Average Number of Teeth')
    plt.xlabel('States')
    plt.title('Average Number of Teeth Lost across 2 States')
    plt.bar(x, y)
    plt.show()

def exits():
    pid = os.getpid()
    print("Exiting The Program")
    os.kill(pid,signal.SIGTERM)

#this function will helps user to their option
def switch_if():
    print(' 1. Statistics \n 2. Export childerns details who haven\'t lost any teeth \n 3. Display number of claims per State \n 4. Compare 2 States \n 5. Exit \n ')
    option = int(input("Enter you choice : \n"))

    if option == 1:
        statics()

    elif option == 2:
        export_childrens()

    elif option == 3 :
        claims_per_state()

    elif option == 4 :
        compare()

    elif option == 5:
        exits()
    else:
        print("********* Enter the valid number********* \n")
        switch_if()

first()
switch_if()


