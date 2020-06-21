from puzzles import Node, create_graph, p6

def test_function_works():
    com = Node("COM")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")
    i = Node("I")
    j = Node("J")
    k = Node("K")
    l = Node("L")

    com.add(b)
    b.add(c)
    b.add(g)
    c.add(d)
    d.add(e)
    d.add(i)
    e.add(f)
    e.add(j)
    g.add(h)
    j.add(k)
    k.add(l)
    actual = p6(com)

    assert(actual == 42)

def test_create_graph():
    graph = create_graph('input.txt')
    assert(graph is not None)