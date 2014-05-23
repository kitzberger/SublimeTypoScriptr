import sublime, sublime_plugin, re

class TyposcriptrCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				# Beginning and end of this line, e.g.: (0, 30)
				line = self.view.line(region)
				posLineBegin = line.a
				posLineEnd = line.b
				string = self.view.substr(line)
				#print ("TypoScriptr processing this string: '" + string + "'")

				# Text after cursor
				posCursor = self.view.sel()[0].begin()
				range = sublime.Region(posCursor, line.b)
				textAfterCursor = self.view.substr(range).strip()

				# Split at operator (only once -> third param!)
				stringSplitted = re.split(r'(=|<|=<|>)', string, 1)
				lengthOfTextInfrontOfCursor = len(stringSplitted[0])
				posOperator = posLineBegin + lengthOfTextInfrontOfCursor
				#print ("Splitted string: " + str(stringSplitted))
				#print ("posLineBegin: " + str(posLineBegin) + ', posCursor: ' + str(posCursor) + ', lengthOfTextBeforeCursor: ' + str(lengthOfTextInfrontOfCursor) + ', posOperator: ' + str(posOperator))

				# Was cursor set behind operator?
				if (posCursor > posOperator):
					#print ("Cursor is after operator")

					# Example: "page.10.template.value = hello world"
					newLine = re.split(r'(=|<|=<|>)', string)
					newLine = '\n' + newLine[0].rstrip()

					# Insert: "page.10.template.value"
					self.view.insert(edit, posCursor, newLine)
				else:
					#print ("Cursor was before operator a.k.a. no operator detected!")
					matchObj = re.match(r'(\s*)(\w*).*$', string, re.M)
					whitespaces = matchObj.group(1)
					#print ("Leading whitespaces found: '" + whitespaces + "'")
					newLines = ' {\n'+whitespaces+'\t\n'+whitespaces+'}'

					# Append: " {LINEBREAK TABS TAB LINEBREAK TABS}"
					self.view.insert(edit, line.end(), newLines)

					# Cursor re-positioning after second LINEBREAK
					pos = self.view.sel()[0].begin()
					pos = pos - len(whitespaces) - 2
					self.view.sel().clear()
					self.view.sel().add(pos)
