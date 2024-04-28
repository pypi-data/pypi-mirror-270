import bashinpy as bash

system = bash.system.call

def git_clone(url):
    system(f"git clone {url}")
