import json
import sys

print(
    list(
        filter(lambda x: x["packagetype"] == "sdist",
               json.load(sys.stdin)["releases"][sys.argv[1]])
    )[0]["url"]
)
