SublimeTypoScriptr
==================

This plugin provides a tiny helper when editing TypoScript files

Installation
------------
* Clone this repository into your local packages folder. Find out which folder that is via `Preferences -> Browse Packages ...`
* Add a key binding to call typoscriptr, do so in `Preferences ->  Key Bindings - User`, for example:
```
[
	{ "keys": ["ctrl+enter"], "command": "typoscriptr" }
]
```

What does it do?
----------------
It simply duplicates the current line of code, so TypoScript can be written a little faster.

### Example 1

```
page.10.template = TEMPLATE(cursor)

->

page.10.template = TEMPLATE
page.10.template(cursor)
```

### Example 2

```
page.10.template = TEMPLATE
page.10.template(cursor)

->

page.10.template = TEMPLATE
page.10.template {
	(cursor)
}
```

### Example 3

```
page.10.subparts.FOOTER = COA
page.10.subparts.FOOTER.10 = TEXT
page.10.subparts.FOOTER.10.value = Blub(cursor)

->

page.10.subparts.FOOTER = COA
page.10.subparts.FOOTER.10 = TEXT
page.10.subparts.FOOTER.10.value = Blub
page.10.subparts.FOOTER.10(cursor)
```

### Example 4 (with text right to the cursor)

```
lib.customText = TEXT(cursor)Blub

->

lib.customText = TEXT
lib.customText(cursor)Blub
```

### Example 5 (with text right to the cursor)

```
lib.customText = TEXT
lib.customText(cursor)Blub

->

lib.customText = TEXT
lib.customText {
	(cursor)Blub
}
```
