from django.shortcuts import render
import mysql.connector as sql

fn=''
ln=''
s=''
e=''
pwd=''
def signupaction(request):
    global fn,ln,s,e,pwd

    if request.method=='POST':

        m=sql.connect(host='localhost',user='root',password='root',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='first_name':
                fn=value
            if key=='last_name':
                ln=value

            if key=='sex':
                s=value

            if key=='email':
                e=value

            if key=='password':
                pwd=value
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,e,pwd)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')    




