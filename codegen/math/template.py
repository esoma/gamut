
__all__ = ['get_template']

# python
from pathlib import Path
# jinja2
from jinja2 import Environment, FileSystemLoader, Template

env = Environment(
    loader=FileSystemLoader(Path(__file__).resolve().parent / 'templates')
)

def get_template(name: str) -> Template:
    return env.get_template(name)
