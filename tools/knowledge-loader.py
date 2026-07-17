import os
import json


INDEX_PATH = "90_SYSTEM/AHI-INDEX"


def load_json(filename):

    path = os.path.join(
        INDEX_PATH,
        filename
    )

    if not os.path.exists(path):

        return None


    with open(
        path,
        "r",
        encoding="utf8"
    ) as f:

        return json.load(f)



def load_knowledge():

    return {

        "repository": load_json(
            "repository.json"
        ),

        "artifacts": load_json(
            "artifact.json"
        ),

        "dependencies": load_json(
            "dependency.json"
        ),

        "graph": load_json(
            "knowledge_graph.json"
        ),

        "search": load_json(
            "search_index.json"
        )

    }



def find_artifact(artifact_id):

    data = load_knowledge()


    artifacts = data.get(
        "artifacts",
        []
    )


    for artifact in artifacts:

        if artifact.get("id") == artifact_id:

            return artifact


    return None



def search(keyword):

    data = load_knowledge()


    results = []


    for item in data.get(
        "search",
        []
    ):


        text = " ".join(
            item.get(
                "keywords",
                []
            )
        )


        if keyword.lower() in text.lower():

            results.append(
                item
            )


    return results




if __name__ == "__main__":


    print(
        "AHI Knowledge Loader V1"
    )


    package = load_knowledge()


    print(
        "Artifacts:",
        len(
            package.get(
                "artifacts",
                []
            )
        )
    )


    print(
        "Knowledge loaded"
    )
