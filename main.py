from request_parser import parse;
from context_policy import Policy,enforce_scope
from tools_registry import TOOLS;
from llm_planer import make_plan;
from plan_validator import validate;
from executor import run;
from report_generator import summarize
from pathlib import Path

req=parse(input("request> "), enforce_scope(Policy(base=Path.home()), input("path> ")))

res = run(validate(make_plan(req, TOOLS), TOOLS), TOOLS); 
print(summarize(res))


if input("apply changes? (y/N) ").lower()=="y":
    req = type(req)(req.text, req.path, False); 
    print(summarize(run(validate(make_plan(req, TOOLS), TOOLS), TOOLS)))