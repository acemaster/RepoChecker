import subprocess

# path="/home/acemaster/KeepMeSafeDjango"
path_file=open('paths.txt')
repo_paths=path_file.read()
repos=repo_paths.split('\n')
no_of_repos=len(repos)
repos_to_pull=[]
repos_notuptodate=0
# print txt
for path in repos:
	proc = subprocess.Popen(["git status", ""], stdout=subprocess.PIPE, shell=True, cwd=path)
	(out, err) = proc.communicate()
	if "Your branch is up-to-date" not in out:
		repos_notuptodate=repos_notuptodate+1
		repos_to_pull.append(path)

print str(repos_notuptodate)+" out of "+str(no_of_repos)+" need to be pulled"
if len(repos_to_pull) != 0:
	for repo in repos_to_pull:
		print repo


