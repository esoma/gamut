
export DISPLAY=:0
python -m pytest -k "not controller and not mypy" -nauto -vx --timeout=4 --timeout-method=thread
#python -m pytest -k "controller" -v
