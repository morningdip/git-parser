# git-parser
A Python tool to convert Git commit logs into CSV format.

## Usage
```shell
git log --pretty=format:"%H,%h,%cn,%cd,%cr,%s" <hash_from>^..<hash_to> | python parser.py
```
## Example
```shell
git log --pretty=format:"%H,%h,%cn,%cd,%cr,%s" b0b4460^..486c1f6 | python parser.py
```
