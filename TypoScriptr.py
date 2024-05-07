import sublime, sublime_plugin, re

class TyposcriptrCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for counter, region in enumerate(self.view.sel()):
			if region.empty():
				# Beginning and end of this line, e.g.: (0, 30)
				line = self.view.line(region)
				string = self.view.substr(line)
				print ("TypoScriptr processing this string: '" + string + "'")

				# Example: "page.10.template.value = hello world"
				matchObj = re.match(r'.*\s*(=|<|=<|>)\s*.*$', string, re.M)
				if (matchObj):
					if region.end() == line.end():
						print ("* Case 1a: line containing TypoScript operator and cursor at end of it")
					else:
						print ("* Case 1b: line containing TypoScript operator and cursor within line")

					newLine = re.split(r'(=|<|=<|>)', string)
					newLine = '\n' + newLine[0].rstrip()

					# Insert: "page.10.template.value"
					self.view.insert(edit, region.end(), newLine)
				else:
					if region.end() == line.end():
						print ("* Case 2a: line not containing TypoScript operator and cursor at end of it")
					else:
						print ("* Case 2b: line not containing TypoScript operator and cursor within line")

					regionRightToCursor = sublime.Region(region.end(), line.end())
					textRightToCursor = self.view.substr(regionRightToCursor)
					self.view.erase(edit, regionRightToCursor)

					matchObj = re.match(r'(\s*)(\w*).*$', string, re.M)
					whitespaces = matchObj.group(1)
					#print ("Whitespace found: '" + whitespaces + "'")
					newLines = ' {\n'+whitespaces+'\t'+textRightToCursor+'\n'+whitespaces+'}'

					# Append: " {LINEBREAK TABS TAB LINEBREAK TABS}"
					self.view.insert(edit, region.end(), newLines)

					# Refresh region since we just shifted its coordinates with the previous command
					region = self.view.sel()[counter]

					# Cursor re-positioning after second LINEBREAK
					pos = region.begin()
					pos = pos - len(whitespaces) - len(textRightToCursor) - 2
					self.view.sel().subtract(region)
					self.view.sel().add(pos)
