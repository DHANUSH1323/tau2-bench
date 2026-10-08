import json, importlib, tiktoken
enc = tiktoken.get_encoding("o200k_base")
for d in ["airline", "retail", "telecom"]:
    env = importlib.import_module(f"tau2.domains.{d}.environment").get_environment()
    schemas = [t.openai_schema for t in env.get_tools()]
    print(d, len(schemas), "tools,", len(enc.encode(json.dumps(schemas))), "schema tokens,",
          len(enc.encode(env.get_policy())), "policy tokens")
    print("  ", [s["function"]["name"] for s in schemas])
