# ai-sandbox

```
alias gac='function _gac(){ git add --all && git commit -m "${1:-changes}"; };_gac'
```

```
pipenv install --dev
pipenv shell

CONFIG_JSON=`cat .config.json` python foo.py
```
