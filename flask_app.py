import itertools
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/fpvecalculator')
def fpvecalculator():
    return render_template('index.html')

@app.route('/uolfp')
def uolfp():
    return str(floyd(graph))

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node,end_node\
        in itertools.product\
            (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node] )
        #Any value that have sys.maxsize has no path
    return distance

# Recursion of Graph
def graph_recursion(rv,OV,graph,MAX_LENGTH,NO_PATH):
    if (rv>0):
        results = rv + graph_recursion(rv-1,OV,graph,MAX_LENGTH,NO_PATH)
        #print(" ")
        #print("Graph Recursion #" + str(rv) + " of " + str(OV) + ":")
        #print("------------------------")
        if (rv>1):
            data.append('\n')
        data.append('Graph Recursion #' + str(rv) + " of " + str(OV) + ":")
        data.append('\n------------------------------------')
        data.append('\n')
        
        floyd_Warshall(graph,MAX_LENGTH,NO_PATH)
    else:
        results = 0
    return results

# Solves the shortest path using Floyd Warshall Algorithm
# G = graph matrix variables
def floyd_Warshall(G,MAX_LENGTH,NO_PATH):
    distance = list(map(lambda p: list(map(lambda q: q, p)), G))

    # Adding vertices individually
    for r in range(MAX_LENGTH):
        for p in range(MAX_LENGTH):
            for q in range(MAX_LENGTH):
                distance[p][q] = min(distance[p][q], distance[p][r] + distance[r][q])
    print_Solution(distance,MAX_LENGTH,NO_PATH)


# Printing the output
def print_Solution(distance,MAX_LENGTH,NO_PATH):
    for p in range(MAX_LENGTH):
        for q in range(MAX_LENGTH):
            if(distance[p][q] == NO_PATH):
                #print("NO_PATH", end=" ")
                data.append("NP  ")
            else:
                #print(distance[p][q], end="  ")
                if(len(str(distance[p][q])) == 1):
                   data.append("0" + str(distance[p][q]) + "   ")
                else:
                    data.append(str(distance[p][q]) + "  ")
        data.append( "\n")
        print(" ")

global data 
data = []
@app.route('/print_graph',methods=['POST'])
def print_graph():
        values = request.json[0]
        #print(values)
     # Define infinity as the large enough value. This value
        # will be used for vertices not connected to each other
        NO_PATH = sys.maxsize

        # recursion value
        rv = int(values["spin1"])

        # Original Value of recursion constant
        OV = rv

        # GET GRAPH LINE 1 VARIABLES
        if (values["textbox11"] == "NO_PATH"  or values["textbox11"] == "" or values["textbox11"] == "NP"):
            m11 = NO_PATH
        else:
            m11 = int(values["textbox11"])
        if (values["textbox12"] == "NO_PATH" or values["textbox12"] == "" or values["textbox12"] == "NP"):
            m12 = NO_PATH
        else:
            m12 = int(values["textbox12"])
        if (values["textbox13"] == "NO_PATH" or values["textbox13"] == "" or values["textbox13"] == "NP"):
            m13 = NO_PATH
        else:
            m13 = int(values["textbox13"])
        if (values["textbox14"] == "NO_PATH" or values["textbox14"] == "" or values["textbox14"] == "NP"):
            m14 = NO_PATH
        else:
            m14 = int(values["textbox14"])

        # GET GRAPH LINE 2 VARIABLES
        if (values["textbox21"] == "NO_PATH" or values["textbox21"] == "" or values["textbox21"] == "NP"):
            m21 = NO_PATH
        else:
            m21 = int(values["textbox21"])
        if (values["textbox22"] == "NO_PATH" or values["textbox22"] == "" or values["textbox22"] == "NP"):
            m22 = NO_PATH
        else:
            m22 = int(values["textbox22"])
        if (values["textbox23"] == "NO_PATH" or values["textbox23"] == "" or values["textbox23"] == "NP"):
            m23 = NO_PATH
        else:
            m23 = int(values["textbox23"])
        if (values["textbox24"] == "NO_PATH" or values["textbox24"] == "" or values["textbox24"] == "NP"):
            m24 = NO_PATH
        else:
            m24 = int(values["textbox24"])

        # GET GRAPH LINE 3 VARIABLES
        if (values["textbox31"] == "NO_PATH" or values["textbox31"] == "" or values["textbox31"] == "NP"):
            m31 = NO_PATH
        else:
            m31 = int(values["textbox31"])
        if (values["textbox32"] == "NO_PATH" or values["textbox32"] == "" or values["textbox32"] == "NP"):
            m32 = NO_PATH
        else:
            m32 = int(values["textbox32"])
        if (values["textbox33"] == "NO_PATH" or values["textbox33"] == "" or values["textbox33"] == "NP"):
            m33 = NO_PATH
        else:
            m33 = int(values["textbox33"])
        if (values["textbox34"] == "NO_PATH" or values["textbox34"] == "" or values["textbox34"] == "NP"):
            m34 = NO_PATH
        else:
            m34 = int(values["textbox34"])

        # GET GRAPH LINE 4 VARIABLES
        if (values["textbox41"] == "NO_PATH" or values["textbox41"] == "" or values["textbox41"] == "NP"):
            m41 = NO_PATH
        else:
            m41 = int(values["textbox41"])
        if (values["textbox42"] == "NO_PATH" or values["textbox42"] == "" or values["textbox42"] == "NP"):
            m42 = NO_PATH
        else:
            m42 = int(values["textbox42"])
        if (values["textbox43"] == "NO_PATH" or values["textbox43"] == "" or values["textbox43"] == "NP"):
            m43 = NO_PATH
        else:
            m43 = int(values["textbox43"])
        if (values["textbox44"] == "NO_PATH" or values["textbox44"] == "" or values["textbox44"] == "NP"):
            m44 = NO_PATH
        else:
            m44 = int(values["textbox44"])

        # Graph Variables from Input Text
        graph = [[m11, m12, m13, m14],
                 [m21, m22, m23, m24],
                 [m31, m32, m33, m34],
                 [m41, m42, m43, m44]]

        # Number of vertices in the graph constant
        MAX_LENGTH = len(graph[0])
        data.append('The following matrices show the shortest distance between every pair of vertices. Number of vertices = ' + str(MAX_LENGTH) + '\n' + '\n')
        graph_recursion(rv,OV,graph,MAX_LENGTH,NO_PATH)
        res = data.copy()
        data.clear()
        return {'res' : "".join(res)}