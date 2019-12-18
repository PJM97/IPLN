from args import args_Parser

args= args_Parser()
print(args.regex[0].encode("unicode_escape"),args.regex[1],args.regex[2])
#strng = "\w+"

#print(strng)