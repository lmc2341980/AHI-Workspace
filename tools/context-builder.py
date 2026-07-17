import json
import os

INDEX = "90_SYSTEM/AHI-INDEX"


def load(name):
    with open(os.path.join(INDEX, name), "r", encoding="utf-8") as f:
        return json.load(f)


artifacts = load("artifact.json")
graph = load("knowledge_graph.json")
search = load("search_index.json")

context = {
    "artifact_count": len(artifacts),
    "graph_nodes": len(graph.get("nodes", [])),
    "graph_edges": len(graph.get("edges", [])),
    "search_items": len(search),
    "artifacts": artifacts,
    "graph": graph,
    "search": search
}

with open(
    os.path.join(INDEX, "context.json"),
    "w",
    encoding="utf-8"
) as f:
    json.dump(context, f, indent=2, ensure_ascii=False)

print("AHI Context Builder Done")
