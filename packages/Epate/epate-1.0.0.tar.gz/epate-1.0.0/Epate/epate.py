import requests

class epate:
    def login(username:str,password:str,print:str='no'):
        session = requests.Session()
        login_data = {'pid': '65edCTyg',
                'identity': username,
                'password': password}
        result = session.post('https://api.codemao.cn/tiger/v3/web/accounts/login', json=login_data)

        def get():
            return(result.text())

        if result.status_code == 201:
            if print == 'yes':
                print("Login Successful[201]")
            else:
                return('201')
        else:
            if print == 'yes':
                print("Login Failed["+str(result.status_code)+"]")
            else:
                return(str(result.status_code))
               
    def logout(print:str='no'):
        session = requests.Session()
        result = session.post('https://api.codemao.cn/tiger/v3/web/accounts/loginout')

        def get():
            return(result.text())

        if result.status_code == 200:
            if print == 'yes':
                print("Logout Successful[204]")
            else:
                return('204')
        else:
            if print == 'yes':
                print("Logout Failed["+str(result.status_code)+"]")
            else:
                return(str(result.status_code))
            
    def usrinfo(kind:str,inputstr:str,inputint:int,print:str='no'):
        if kind == 'nick':
            session = requests.Session()
            change = {'nickname':inputstr}
            result = session.patch("/tiger/v3/web/accounts/info",data=change)
        
        if kind == 'full':
            session = requests.Session()
            change = {'fullname':inputstr}
            result = session.patch("/tiger/v3/web/accounts/info",data=change)

        if kind == 'desc':
            session = requests.Session()
            change = {'description':inputstr}
            result = session.patch("/tiger/v3/web/accounts/info",data=change)

        if kind == 'sex':
            session = requests.Session()
            change = {'sex':inputint}
            result = session.patch("/tiger/v3/web/accounts/info",data=change)

        if kind == 'birth':
            session = requests.Session()
            change = {'birthday	':inputint}
            result = session.patch("/tiger/v3/web/accounts/info",data=change)

        if kind == 'avat':
            session = requests.Session()
            change = {'avatar_url':inputstr}
            result = session.patch("/tiger/v3/web/accounts/info",data=change)

        def get():
                return(result.text())    
            
        if result.status_code == 204:
            if print == 'yes':
                print("Change Info Successful[204]")
            else:
                return('204')
        else:
            if print == 'yes':
                print("Change Info Failed["+str(result.status_code)+"]")
            else:
                return(str(result.status_code))
                
    def psc(old_password:str,new_password:str,print:str='no'):
        session = requests.Session()
        change = {'old_password':old_password,'password':new_password,'confirm_password':new_password}
        result = session.patch("/tiger/v3/web/accounts/info",data=change)
        def get():
                return(result.text())    
            
        if result.status_code == 204:
            if print == 'yes':
                print("Change Password Successful[204]")
            else:
                return('204')
        else:
            if print == 'yes':
                print("Change Password Failed["+str(result.status_code)+"]")
            else:
                return(str(result.status_code))

    def like(workid:str,print:str='no'):
        session = requests.Session()
        result = session.post("https://api.codemao.cn/nemo/v2/works/" + workid +"/like")

        def get():
            return(result.text())

        if result.status_code == 201:
            if print == 'yes':
                print("Like Successful[201]")
            else:
                return('201')
        else:
            if print == 'yes':
                print("Like Failed["+str(result.status_code)+"]")
            else:
                return(str(result.status_code))

    def coll(workid:str,print:str='no'):
        session = requests.Session()
        result = session.post("https://api.codemao.cn/nemo/v2/works/" + workid +"/collection")
        
        def get():
            return(result.text())
        
        if result.status_code == 201:
            if print == 'yes':
                print("Collection Successful[201]")
            else:
                return('201')
        else:
            if print == 'yes':
                print("Collection Failed["+str(result.status_code)+"]")
            else:
                return(str(result.status_code))
            
    def fork(workid:str,print:str='no'):
        session = requests.Session()
        result = session.post("https://api.codemao.cn/nemo/v2/works/" + workid +"/fork")

        def get():
            return(result.text())

        if result.status_code == 201:
            if print == 'yes':
                print("Fork Successful[201]")
            else:
                return('201')
        else:
            if print == 'yes':
                print("Fork Failed["+str(result.status_code)+"]")
            else:
                return(str(result.status_code))