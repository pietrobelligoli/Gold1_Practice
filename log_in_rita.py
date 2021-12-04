def log_in(username, password):
    
    
    for name in df["username"]:
        if name == username:
            line = list(df["username"]).index(name)
            digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if df["password"][line] == digest_password:
                print("Access allowed")
                break
                
            else:
                print("Please check password")
                break
                
                
        elif name != username and list(df["username"]).index(name) == len(df["username"])-1:
            print("No correspondence")
            
                
        else: 
            continue
            
            
log_in("Marco Visentin", "MV123456")