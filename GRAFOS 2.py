import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


estados = [
    "Jalisco",
    "Guanajuato",
    "Michoacán",
    "Zacatecas",
    "Aguascalientes",
    "Querétaro",
    "San Luis Potosí"
]

G.add_nodes_from(estados)


conexiones = [
    ("Jalisco", "Guanajuato", 200),
    ("Jalisco", "Michoacán", 150),
    ("Guanajuato", "Michoacán", 100),
    ("Guanajuato", "Zacatecas", 300),
    ("Michoacán", "Aguascalientes", 250),
    ("Aguascalientes", "San Luis Potosí", 150),
    ("Querétaro", "San Luis Potosí", 180),
    ("Querétaro", "Guanajuato", 120),
    ("Zacatecas", "San Luis Potosí", 220),
]


for estado1, estado2, costo in conexiones:
    G.add_edge(estado1, estado2, weight=costo)

recorrido_encontrado = []
costo_total = 0  


def recorrer_nodos(nodo_actual, recorrido, visitados):
    global recorrido_encontrado, costo_total
    
    recorrido.append(nodo_actual)
    visitados.add(nodo_actual)

    if len(recorrido) == len(estados):
        recorrido_encontrado = recorrido.copy()
      
        for i in range(len(recorrido) - 1):
            costo_total += G[recorrido[i]][recorrido[i + 1]]['weight']
        return True  

    for vecino in G[nodo_actual]:
        if vecino not in visitados:
            if recorrer_nodos(vecino, recorrido, visitados):
                return True 

    visitados.remove(nodo_actual)
    recorrido.pop()
    return False  


for estado in estados:
    if recorrer_nodos(estado, [], set()):
        break  


if recorrido_encontrado:
    print(f"Recorrido encontrado recorriendo todos los estados: {' -> '.join(recorrido_encontrado)}")
    print(f"Costo total del recorrido: {costo_total}")
else:
    print("No se encontró un recorrido válido.")

recorrido_encontrado2 = []
costo_total2 = 0  

def recorrer_nodos_y_volver(nodo_actual, recorrido):
    global recorrido_encontrado2, costo_total2
    recorrido.append(nodo_actual)

    if len(recorrido) == len(estados):
        
        if len(recorrido) > 1:
            recorrido.append(recorrido[-2])  
            
            for i in range(len(recorrido) - 1):
                costo_total2 += G[recorrido[i]][recorrido[i + 1]]['weight']
        print(f"Recorrido encontrado: {' -> '.join(recorrido)}")
        print(f"Costo total del recorrido: {costo_total2}")  
        return True  

    for vecino in G[nodo_actual]:
        if vecino not in recorrido: 
            if recorrer_nodos_y_volver(vecino, recorrido):
                return True 

    recorrido.pop()  
    return False  


for estado in estados:
    if recorrer_nodos_y_volver(estado, []):
        break  


if not recorrido_encontrado2:
    print("No se encontró un recorrido válido.")


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')


if recorrido_encontrado:
    edges_recorrido = [(recorrido_encontrado[i], recorrido_encontrado[i + 1]) for i in range(len(recorrido_encontrado) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_recorrido, edge_color='red', width=2)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Grafo de estados de la República Mexicana")
plt.show()


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
if recorrido_encontrado2:
    edges_recorrido2 = [(recorrido_encontrado2[i], recorrido_encontrado2[i + 1]) for i in range(len(recorrido_encontrado2) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_recorrido2, edge_color='red', width=2)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Grafo de estados de la República Mexicana con recorrido único")
plt.show()
sumaf=costo_total+costo_total2

print("la suma de los recorridos es: ",sumaf)