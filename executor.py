def run(plan, tools):
    out = []
    for step in plan["steps"]:
        out.append(tools[step["tool"]].fn(**step["args"]))
    return out