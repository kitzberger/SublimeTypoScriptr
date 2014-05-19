import sublime, sublime_plugin, re

class TyposcriptrCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				# Beginning and end of this line, e.g.: (0, 30)
				line = self.view.line(region)
				string = self.view.substr(line)
				print ("TypoScriptr processing this string: '" + string + "'")

				# Example: "page.10.template.value = hello world"
				matchObj = re.match(r'.*\s*(=|<|=<|>)\s*[^\s]*\s*$', string, re.M)
				if (matchObj):
					newLine = re.split(r'(=|<|=<|>)', string)
					newLine = '\n' + newLine[0].rstrip()

					# Insert: "page.10.template.value"
					self.view.insert(edit, line.end(), newLine)
				else:
					matchObj = re.match(r'(\s*)(\w*).*$', string, re.M)
					whitespaces = matchObj.group(1)
					#print ("Whitespace found: '" + whitespaces + "'")
					newLines = ' {\n'+whitespaces+'\t\n'+whitespaces+'}'

					# Append: " {LINEBREAK TABS TAB LINEBREAK TABS}"
					self.view.insert(edit, line.end(), newLines)

					# Cursor re-positioning after second LINEBREAK
					pos = self.view.sel()[0].begin()
					pos = pos - len(whitespaces) - 2
					self.view.sel().clear()
					self.view.sel().add(pos)