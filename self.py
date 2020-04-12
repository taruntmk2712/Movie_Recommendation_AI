import pandas as pd 
from tkinter import *
from tkinter import font

def show_data():
    movieName = ent.get()


    df = pd.read_csv("C:\\Users\\Tarun M Krishna\\Documents\\6th SEM\\AI\\ratings.csv") 
    df.head() 

    movie_titles = pd.read_csv("C:\\Users\\Tarun M Krishna\\Documents\\6th SEM\\AI\\movies.csv") 
    movie_titles.head() 
    data = pd.merge(df, movie_titles, on='movieId',how='left') 
    data.head() 

    data.groupby('title')['rating'].mean().sort_values(ascending=False).head() 
    ratings = pd.DataFrame(data.groupby('title')['rating'].mean()) 
    ratings['Total Ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 
    ratings.head()

    moviemat = data.pivot_table(index ='userId',columns ='title', values ='rating') 
    moviemat.head() 

    ratings.sort_values('Total Ratings', ascending = False).head(10) 


    movie_user_ratings = moviemat[movieName]
    movie_user_ratings.head() 

    similar_to_userinput = moviemat.corrwith(movie_user_ratings) 

    corr_userinput = pd.DataFrame(similar_to_userinput, columns =['Correlation']) 
    corr_userinput.dropna(inplace = True)

    corr_userinput.head()

    corr_userinput.sort_values('Correlation', ascending = False).head(10) 
    corr_userinput = corr_userinput.join(ratings['Total Ratings'])
    corr_userinput.head()

    
    '''res = corr_userinput[corr_userinput['Total Ratings']>100].sort_values('Correlation', ascending = False).head()
    res = res.merge(movie_titles,on='title',how='left')
    res.head(10)'''
    res=[]
    res.append(corr_userinput[corr_userinput['Total Ratings']>100].sort_values('Correlation', ascending = False).merge(movie_titles,on='title',how='outer').head())
    '''res1=[]
    res1.append(res)
    res2=""'''
    res2=""
    for i in res:
        res2+=str(i)
    txt.delete(0.0,END)
    txt.insert(0.0,res2)


root = Tk()
root.geometry("1600x1200")
root.title("Movie Recommendation System")

lab=Label(root,text="Movie Recommendation System")
lab.place(x=565, y=10, height=50, width=300)


l1 =Label(root,text="Enter Movie:")
l1.place(x=435, y=50, height=90, width=120)
ent = Entry(root)
ent.place(x=535, y=82, height=25, width=350)



btn = Button(root,text="Submit", command = show_data)
btn.place(x=900, y=78, height=30, width=50)

txt = Text(root,width=25,height=10,wrap=WORD)
txt.place(x=100, y=135, height=650, width=1300)


root.mainloop()
