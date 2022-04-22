def pushToGit():
    import os
    cmd = 'git add . \ngit commit -m "web page updated!"\ngit push'
    os.system(cmd)