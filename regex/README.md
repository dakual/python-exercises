| Method | Description |
| --- | --- |
| `[re.compile('pattern')](https://pynative.com/python-regex-compile/)` | Compile a regular expression pattern provided as a string into a `re.Pattern` object. |
| `[re.search(pattern, str)](https://pynative.com/python-regex-search/)` | Search for occurrences of the regex pattern inside the target string and return only the first match. |
| `[re.match(pattern, str)](https://pynative.com/python-regex-pattern-matching/)` | Try to match the regex pattern at the start of the string. It returns a match only if the pattern is located at the beginning of the string. |
| `[re.fullmatch(pattern, str)](https://pynative.com/python-regex-pattern-matching/#h-re-fullmatch)` | Match the regular expression pattern to the entire string from the first to the last character. |
| `[re.findall(pattern, str)](https://pynative.com/python-regex-findall-finditer/)` | Scans the regex pattern through the entire string and returns all matches. |
| `[re.finditer(pattern, str)](https://pynative.com/python-regex-findall-finditer/#h-finditer-method)` | Scans the regex pattern through the entire string and returns an iterator yielding match objects. |
| `[re.split(pattern, str)](https://pynative.com/python-regex-split/)` | It breaks a string into a list of matches as per the given regular expression pattern. |
| `[re.sub(pattern, replacement, str)](https://pynative.com/python-regex-replace-re-sub/)` | Replace one or more occurrences of a pattern in the string with a `replacement`. |
| `[re.subn(pattern, replacement, str)](https://pynative.com/python-regex-replace-re-sub/#h-re-s-subn-method)` | Same as re.sub(). The difference is it will return a tuple of two elements.  <br>First, a new string after all replacement, and second the number of replacements it has made. |