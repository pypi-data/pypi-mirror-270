TODO
- Make sure Sphinx generates docs from all files
- generate html instead of md ???
- add general introduction and usage guide on the docs

Build
`hatch build` or `python -m hatch build`
`hatch publish` or `python -m hatch publish` with username `__token__`. Make sure the [keyrings backend](https://github.com/jaraco/keyrings.alt) is installed. 
On arch `pacman -S python-hatch python-keyrings-alt`, publish with `username:__token__`
