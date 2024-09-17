import snowflake.connector

def connect_to_snowflake(user,password,account,query):
    try:
        conn=snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            )
        print("my snowflake connector is :" , conn)
        if conn!=None:
            print("connection is established")
        cur=conn.cursor()
        
        cur.execute(query)
        result=cur.fetchone()

        cur.close()
        conn.close()
        return result
    except Execption as e:
        return f"An error occured:{e}"

user='SANDEEPL'
password='Sanjaysaahu123'
account='EXZCCOB-DR47913'
query="SELECT CURRENT_VERSION()"

result= connect_to_snowflake(user,password,account,query)
print(result)
