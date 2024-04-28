from Flare import APIv2, Helper

helper = Helper()
hwid = helper.get_hwid()

api = APIv2(
    apilink="server api link",  
    private_key="private key from identifiers.txt", 
    public_key="public key from identifiers.txt"
)
api.setprivate()
api.setpublic()

api.auth(
    uniqueidentifier=hwid,
    activation_key="ABCD-1234-ABCD-1234",
    login=' ', 
    password=' '
)

response = api.validate()
if not response.text == 'VALID':
    exit()
else:
    print("Hello, World!")

