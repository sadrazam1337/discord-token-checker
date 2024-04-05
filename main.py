import requests

print('sadrazam1337 tarafından yapildi\n')

def token_checkle(token):
    headers = {
        'Authorization': token
    }
    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    
    if response.status_code == 200:
        print('token calisiyor')
        with open('calisiyor.txt', 'a') as f:
            f.write(token + '\n')
    else:
        print('token calismiyor')

def main():
    with open('token.txt', 'r') as f:
        tokens = f.read().splitlines()
    
    for token in tokens:
        token_checkle(token)

if __name__ == "__main__":
    main()
