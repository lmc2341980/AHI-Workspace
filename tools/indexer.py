import os
import json


ROOT = "."

IGNORE = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode",
    "AHI-INDEX"
}


INDEX_PATH = "90_SYSTEM/AHI-INDEX"


folders = []
files = []

knowledge_map = {}

artifacts = []

dependencies = []


os.makedirs(
    INDEX_PATH,
    exist_ok=True
)


os.makedirs(
    INDEX_PATH + "/knowledge",
    exist_ok=True
)


def safe_name(path):

    if path == ".":
        return "ROOT"

    return (
        path
        .replace("./", "")
        .replace("/", "__")
        .replace("\\", "__")
        .replace(" ", "_")
    )



def parse_metadata(content):

    if not content.startswith("---"):

        return None


    end = content.find(
        "---",
        3
    )


    if end == -1:

        return None



    block = content[3:end]


    metadata = {}

    current_key = None


    for line in block.splitlines():

        line = line.rstrip()


        if not line.strip():

            continue



        if line.startswith("  - "):

            if current_key:

                metadata[current_key].append(
                    line.replace(
                        "  - ",
                        ""
                    ).strip()
                )

            continue



        if ":" in line:


            key, value = line.split(
                ":",
                1
            )


            key = key.strip()

            value = value.strip()



            if value:

                metadata[key] = value

                current_key = None


            else:

                metadata[key] = []

                current_key = key



    return metadata




for path, dirs, fs in os.walk(ROOT):


    dirs[:] = [
        d for d in dirs
        if d not in IGNORE
    ]


    rel = os.path.relpath(
        path,
        ROOT
    )


    folders.append(rel)



    folder_key = safe_name(rel)


    knowledge_map[folder_key] = []



    manifest = []



    for d in dirs:

        manifest.append(
            f"- 📁 {d}"
        )



    for file in fs:


        if file == "MANIFEST.md":

            continue



        full_path = os.path.join(
            path,
            file
        )


        rel_path = os.path.join(
            rel,
            file
        )


        manifest.append(
            f"- 📄 {file}"
        )


        files.append(
            rel_path
        )



        if file.lower().endswith(".md"):


            try:

                with open(
                    full_path,
                    "r",
                    encoding="utf8"
                ) as f:


                    content = f.read()



                knowledge_map[folder_key].append(
                    {
                        "path": rel_path,
                        "content": content
                    }
                )



                metadata = parse_metadata(
                    content
                )



                if metadata:


                    metadata["path"] = rel_path


                    artifacts.append(
                        metadata
                    )



                    dependencies.append(
                        {
                            "id": metadata.get("id"),

                            "parent": metadata.get(
                                "parent",
                                []
                            ),

                            "dependencies": metadata.get(
                                "dependencies",
                                []
                            ),

                            "tags": metadata.get(
                                "tags",
                                []
                            ),

                            "path": rel_path
                        }
                    )


            except Exception:

                pass




    with open(
        os.path.join(
            path,
            "MANIFEST.md"
        ),
        "w",
        encoding="utf8"
    ) as f:


        f.write(
            "# MANIFEST\n\n"
        )


        f.write(
            f"Folder: `{rel}`\n\n"
        )


        f.write(
            "## Contents\n\n"
        )


        f.write(
            "\n".join(manifest)
        )





with open(
    INDEX_PATH + "/repository.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        {
            "folders": len(folders),
            "files": len(files)
        },
        f,
        indent=2,
        ensure_ascii=False
    )





with open(
    INDEX_PATH + "/tree.txt",
    "w",
    encoding="utf8"
) as f:


    for item in folders:

        f.write(
            item + "\n"
        )


    for item in files:

        f.write(
            item + "\n"
        )





with open(
    INDEX_PATH + "/files.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        files,
        f,
        indent=2,
        ensure_ascii=False
    )





for name, items in knowledge_map.items():


    if not items:

        continue



    with open(
        INDEX_PATH + "/knowledge/" + name + ".jsonl",
        "w",
        encoding="utf8"
    ) as f:


        for item in items:


            f.write(
                json.dumps(
                    item,
                    ensure_ascii=False
                )
            )


            f.write("\n")





with open(
    INDEX_PATH + "/artifact.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        artifacts,
        f,
        indent=2,
        ensure_ascii=False
    )





with open(
    INDEX_PATH + "/dependency.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        dependencies,
        f,
        indent=2,
        ensure_ascii=False
    )





with open(
    INDEX_PATH + "/metadata.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        {
            "artifact_count": len(artifacts),

            "dependency_count": len(dependencies),

            "generated_by": "AHI Repository Indexer V3"

        },
        f,
        indent=2,
        ensure_ascii=False
    )

# Create Knowledge Graph

nodes = []

edges = []


for artifact in artifacts:

    nodes.append(
        {
            "id": artifact.get("id"),
            "name": artifact.get("name"),
            "type": artifact.get("type")
        }
    )


for item in dependencies:

    source = item.get("id")


    for target in item.get("dependencies", []):

        edges.append(
            {
                "from": source,
                "relation": "depends_on",
                "to": target
            }
        )


    for target in item.get("parent", []):

        edges.append(
            {
                "from": source,
                "relation": "inherits",
                "to": target
            }
        )



with open(
    INDEX_PATH + "/knowledge_graph.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        {
            "nodes": nodes,
            "edges": edges
        },
        f,
        indent=2,
        ensure_ascii=False
    )
# Create AI Search Index

search_index = []


for artifact in artifacts:

    keywords = []


    if artifact.get("name"):
        keywords.append(
            artifact.get("name")
        )


    if artifact.get("tags"):

        keywords.extend(
            artifact.get("tags")
        )


    search_index.append(
        {
            "id": artifact.get("id"),

            "type": artifact.get("type"),

            "keywords": keywords,

            "path": artifact.get("path")
        }
    )



with open(
    INDEX_PATH + "/search_index.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        search_index,
        f,
        indent=2,
        ensure_ascii=False
    )
print("AHI Repository Indexer V5 Done")
