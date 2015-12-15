from sys import argv

script, user_name, location = argv
prompt = '>'

print "hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions since you live in %s." % location
print "Do you like me %s?" % user_name
like = raw_input(prompt)

print "How old are you %s?" % user_name
age = raw_input(prompt)

print "What is your job title %s?" % user_name
occupation = raw_input(prompt)

print """
Alright, so you said %r about liking me. You're only %r years old and you work as a %r. Not bad."
""" % (like, age, occupation)

