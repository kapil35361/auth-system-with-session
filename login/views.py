from django.shortcuts import render,redirect
import mysql.connector as sql


e=''
pwd=''
def loginaction(request):
    
    if 'email' in request.session:
        return redirect(dashboard)

    else:
        global e,pwd

        if request.method=='POST':

            m=sql.connect(host='localhost',user='root',password='root',database='website')
            cursor=m.cursor()
            d=request.POST
            for key,value in d.items():
                    

                if key=='email':
                    e=value

                if key=='password':
                    pwd=value
            c="select * from users where email='{}' and password='{}' ".format(e,pwd)
            cursor.execute(c)
            
            
            t=tuple(cursor.fetchall())
            
           
            if t==():
                return render(request,'error.html')
            else:
                request.session['email']= e 
                return redirect(dashboard)
        return render(request,'login_page.html')  

def dashboard(request):
    if 'email'in request.session:
        return render(request,'welcome.html')
      
      

      
    else:
        return render(request,'login_page.html') 


def logout(request):
    if 'email' in request.session:
        request.session.flush()
        return render (request,'login_page.html')