from django.http import HttpRequest, HttpResponse
from dataclasses import dataclass
from django.shortcuts import render

@dataclass
class User:
  name: str
  age: int

def test_endpoint(request: HttpRequest, name: str, age: int) -> HttpResponse:
  USERBASE = [
    ("Francesco", 21),
    ("Chris", 21),
    ("Tacc", 50)
  ]
  ctx = {
    'title': 'Test Endpoint',
    'userbase': [User(name, age) for name, age in USERBASE],
    'client': User(name, age)
  }
  
  return render(request, template_name='test.html', context=ctx)