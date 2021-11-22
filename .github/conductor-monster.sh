
export DISPLAY=:0
python -m pytest -k "not controller" -nauto -v
python -m pytest -k "controller" -v
