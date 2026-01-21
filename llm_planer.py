def make_plan(req, tools):

    want_dupes = any(k in req.text.lower() for k in ("dup","duplicate","dedupe"))

    steps = [{"tool":"dedupe","args":{"path":req.path,"method":"hash","dry_run":req.dry_run}}] if want_dupes else []

    steps += [{"tool":"organize","args":{"path":req.path,"dry_run":req.dry_run}}]

    return {"steps": steps}
