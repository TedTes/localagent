def validate(plan, tools):
   for s in plan.get("steps", []):
        assert s["tool"] in tools
        for k in tools[s["tool"]].args_schema: assert k in s["args"]
   return plan