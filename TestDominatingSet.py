
from DominatingSet import minimalDominatingSet


def test_minimalDominatingSet():
    r = minimalDominatingSet(
        ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10", "v11"],
        [
            ("v1", "v2"),
            ("v2", "v3"),
            ("v2", "v4"),
            ("v2", "v8"),
            ("v3", "v4"),
            ("v3", "v5"),
            ("v4", "v5"),
            ("v4", "v6"),
            ("v4", "v8"),
            ("v5", "v6"),
            ("v6", "v7"),
            ("v6", "v8"),
            ("v7", "v8"),
            ("v8", "v9"),
            ("v8", "v10"),
            ("v9", "v10"),
            ("v9", "v11"),
            ("v10", "v11")
        ]
    )

    if sorted(r) != sorted(["v2", "v6", "v9"]):
        return False


    r = minimalDominatingSet(
        ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10", "v11", "v12", "v13", "v14"],
        [
            ("v1", "v2"),
            ("v1", "v4"),
            ("v2", "v3"),
            ("v2", "v5"),
            ("v3", "v5"),
            ("v4", "v5"),
            ("v4", "v7"),
            ("v5", "v6"),
            ("v5", "v7"),
            ("v5", "v8"),
            ("v5", "v11"),
            ("v6", "v8"),
            ("v6", "v11"),
            ("v7", "v9"),
            ("v7", "v10"),
            ("v8", "v10"),
            ("v8", "v11"),
            ("v9", "v10"),
            ("v12", "v14"),
            ("v13", "v14")
        ]
    )

    if sorted(r) != sorted(["v2", "v5", "v7", "v14"]):
        return False


    r = minimalDominatingSet(
        ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9"],
        [
            ("v1", "v2"),
            ("v1", "v4"),
            ("v2", "v3"),
            ("v2", "v4"),
            ("v2", "v5"),
            ("v2", "v8"),
            ("v3", "v5"),
            ("v4", "v5"),
            ("v4", "v6"),
            ("v4", "v7"),
            ("v5", "v6"),
            ("v9", "v5")
        ]
    )

    if sorted(r) != sorted(["v2", "v4", "v5"]):
        return False

    return True


if __name__ == "__main__":
    if not test_minimalDominatingSet():
        print("ERROR in minimalDominatingSet")