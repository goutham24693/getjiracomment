from jira import JIRA


issues = ("ABDC-2509",)
username = "username"
password = "passwd"
branch = "hub4_vdsl"

jira = JIRA('https://ccc.abc.ccccccc.net/', basic_auth=(username, password))

for issue in issues:
	i = jira.issue(issue, fields="summary,comment")
	print( str(i) + " " + i.fields.summary)
	for comment in i.fields.comment.comments:
		if "*MERGED*" in comment.body:
			print("\t" + comment.body.replace("Gerrit Code-Review ","").strip())
			print("\n")

