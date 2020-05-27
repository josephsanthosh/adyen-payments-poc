
merchant_account = ''  #variable initialisation for storing merchant account name
api_key = ''   #variable initialisation for storing api key
origin_key = ''   #variable initialisation for storing origin key
server_name = ''  #variable initialisation for storing server name

def get_all_config():
    global merchant_account,api_key,origin_key,server_name
    
    #Server name for free web host. Uncomment this and comment the localhost server
    #server_name = 'http://josephsanthosh.pythonanywhere.com'  
    server_name = 'http://localhost:8080'
    
    merchant_account = 'SupportRecruitementCOM'
    api_key = 'AQE1hmfxKo3NaxZDw0m/n3Q5qf3Ve55dHZxYTFdTxWq+l3JOk8J4BO7yyZBJ4o0JviXqoc8j9sYQwV1bDb7kfNy1WIxIIkxgBw==-q7XjkkN/Cud0WELZF+AzXpp/PuCB8+XmcdgqHYUWzTA=-Kk9N4dG837tIyjZF'
    
    
    #Origin key for free web host. Uncomment this and comment the localhost server
    #origin_key = 'pub.v2.7814286629520534.aHR0cDovL2pvc2VwaHNhbnRob3NoLnB5dGhvbmFueXdoZXJlLmNvbQ.vKbntfieKPxFs_z4GFJL3otJD-pHp24P3tQPMUS7wqw'
    origin_key = 'pub.v2.7814286629520534.aHR0cDovL2xvY2FsaG9zdDo4MDgw.gKjRMbdysLhnVHPmtYDJ0ufSr7CL-ttXhunsdwc0qjE'