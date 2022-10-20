
from typing import List, Tuple, Dict, Optional
from Graph import Graph, buildGraph

t = 0

def minimalDominatingSet(vertices : List[str], edges : List[Tuple[str]]) -> List[str]:
    def aux(graph : Graph, maximum_stack_length : int):
        global t
        print('  ' * t + "SUBGRAPH ({}):".format(maximum_stack_length), [ v.getName() for v in graph.getVertices() ])

        def aux2(graph : Graph, stack : List[str], result : List[str], explored_roots : Dict[str, bool]):
            global t

            print('  ' * t + "STACK:", stack)

            unmarked_components = graph.getUnmarkedConnectedComponents()
            if len(unmarked_components) > 1:
                r = stack
                print('  ' * t + "COMPONENTS:", [ [ v.getName() for v in g.getVertices() ] for g in unmarked_components ])

                for c in unmarked_components:
                    if len(r) < maximum_stack_length and len(r) < len(result):
                        r += aux(c, min([maximum_stack_length, len(result)]) - len(r))

                if len(r) < maximum_stack_length and len(r) < len(result):
                    result.clear()
                    for v in r:
                        result.append(v)
                    print('  ' * t + "SOLUTION:", result)

                return

            if len(stack) >= maximum_stack_length or len(stack) >= len(result):
                return

            uncovered = len(graph.getVertices())

            for v in graph.getVertices():
                if v.isMarked():
                    uncovered -= 1

            if uncovered <= 0:
                result.clear()
                for v in stack:
                    result.append(v)
                print('  ' * t + "SOLUTION:", result)

            if len(stack) >= maximum_stack_length - 1 or len(stack) >= len(result) - 1:
                return

            remaining = [
                v
                for v in (
                    graph.getDisk([ graph.getVertexByName(name) for name in stack ], 3)
                    if len(stack) > 0
                    else graph.getVertices()
                )
                if v.getName() not in stack
                and v.getCoveringPotential() >= 1
                and not explored_roots[v.getName()]
            ]

            if len(stack) + 1 in [maximum_stack_length - 1, len(result) - 1]:
                remaining = [
                    v
                    for v in remaining
                    if v.getCoveringPotential() >= uncovered
                ]

            remaining.sort(
                key = lambda v: -v.getCoveringPotential()
            )

            for name in [ v.getName() for v in remaining ]:
                vertex = graph.getVertexByName(name)
                modif = vertex.cover()

                t += 1
                aux2(
                    graph,
                    stack + [ vertex.getName() ],
                    result,
                    explored_roots
                )
                t -= 1

                graph.revert(modif)

                if len(stack) == 0:
                    explored_roots[v.getName()] = True

                if len(stack) >= maximum_stack_length - 1 or len(stack) >= len(result) - 1:
                    return


        dominating : List[str] = [ v.getName() for v in graph.getVertices() ]
        t += 1
        aux2(graph, [], dominating, { v.getName(): False for v in graph.getVertices() })
        t -= 1

        return dominating

    graph = buildGraph(vertices, edges)
    return aux(graph, len(graph.getVertices()))
