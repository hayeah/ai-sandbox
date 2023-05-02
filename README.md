# ai-sandbox

```
alias gac='function _gac(){ git add --all && git commit -m "${1:-changes}"; };_gac'
```

install dependencies

```
pipenv install --dev
pipenv shell
```

set CONFIG_JSON. either from CLI or env

```
CONFIG_JSON=`cat .config.json` python foo.py
```
