import requests

class ABHA_APIS:
        
    def create_gateway_session_token(clientId:str,clientSecret:str,grantType:str):
        body={
            "clientId":clientId,
            "clientSecret":clientSecret,
            "grantType":grantType
        }
        response = requests.post("https://dev.abdm.gov.in/gateway/v0.5/sessions",json=body)
        print(response.status_code)
        print(response.json())