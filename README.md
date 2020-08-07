![logo](./ui-map-parser.png) Library that helps you with storing ui elements in files
======

HOWTO Install:
------
- `pip install ui-map-parser`

HOWTO Use:
------
First you should create a folder where you will store ini files with selectors.
In this folder create common.ini file.
Now you can create elements in this file or create another ini files which will represent pages.

Example of common.ini:
```ini
[DEFAULT]
type=xpath

[SimpleXpathElement]
selector=//div

[SimpleCssElement]
type=css
selector=div#some-id
```

Example of how you can access this elements:
```python
from ui_map_parser import UIMapParser

# common is page by default but you can change it specifying default_page variable during initialization
ui_map_parser = UIMapParser(ini_files_folder)
selector_type, selector = ui_map_parser.parse_element('SimpleXpathElement')  # name of element is case insensitive
# selector_type will be equal to "xpath", selector will be equal to "//div"
```

You can add another page for example login.ini:
```ini
[DEFAULT]
type=xpath

[EmailTextField]
selector=//div[@id="login-panel"]/input[@id="email"]

[PasswordTextField]
selector=//div[@id="login-panel"]/input[@id="password"]
```

and then access it in following way:

```python
selector_type, selector = ui_map_parser.parse_element('Login.EmailTextField')
```

You can replace repeating sections such as "//div[[@id="login-panel"]" by using "parent" property:
```ini
[DEFAULT]
type=xpath

[LoginPanel]
selector=//div[@id="login-panel"]

[EmailTextField]
parent=Login.LoginPanel
selector=/input[@id="email"]

[PasswordTextField]
parent=Login.LoginPanel
selector=/input[@id="password"]
```

`parent=Login.LoginPanel` indicates that we are searching for parent element in login.ini file with name "LoginPanel".
In case if parent element located in "default_page" (common.ini by default) you can skip this and use without specifying page `parent=LoginPanel`.

**Important note: you can use parent only on elements with same type**

To work with more complex elements templates are supported, you can specify template in your selector:
```ini
[RegionButtonTemplate]
type=xpath
selector=//input[@id="region-%%region%%-button"]
```

and then use it like:
```python
selector_type, selector = ui_map_parser.parse_element('Login.RegionButtonTemplate', template={'region': 'na'})
# selector will be equal to "//input[@id="region-na-button"]"
```

Also you can specify selectors for different languages:
```ini
[SomeElement]
type=xpath
selector=//div
en=[@text="some en text"]
es=[@text="some es text"]
```

and then specify language when initializing UIMapParser:
```python
ui_map_parser = UIMapParser(ini_files_folder, language='en')
selector_type, selector = ui_map_parser.parse_element('SomeElement')
# selector will be equal to "//div[@text="some en text"]"
```