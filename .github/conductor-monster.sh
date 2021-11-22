
export DISPLAY=:0
python -m pytest -k "not controller" -nauto
python -m pytest -k "controller"
