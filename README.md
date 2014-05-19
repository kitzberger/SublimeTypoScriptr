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
```
page.10.template = TEMPLATE (crlt+enter)
->
page.10.template = TEMPLATE
