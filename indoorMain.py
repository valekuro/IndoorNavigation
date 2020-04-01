from Libraries import polyskel, qualitativeAlgorithm as Al
from Libraries.euclidNEW import *
import matplotlib.pyplot as plt
import networkx as nx
from Libraries.buffer import Buffer_LineSegment2

if __name__ == "__main__":

    def buffer_from_linesegment(line, buffer_holes=None, dist=0.1, door_size=0.3):
        if buffer_holes is None:
            buffers.append(Buffer_LineSegment2(line))
        else:
            lines = [line]
            for hole in buffer_holes:
                for line in lines:
                    entries = []
                    outies = []
                    if hole.intersect(line):
                        entries.append(LineSegment2(line.p1, hole - line.copy().v.normalize() * door_size))
                        entries.append(LineSegment2(hole + line.copy().v.normalize() * door_size, line.p2))
                        outies.append(line)
                        break
                for outy in outies:
                    # print("outy",outy)
                    lines.remove(outy)
                for entry in entries:
                    # print("entry", entry)
                    lines.append(entry)
            for line in lines:
                bf = Buffer_LineSegment2(line, dist)
                buffers.append(bf)

    def open_room(room,door,door_size=0.3):
        new_walls = []
        ind_old_wall = 0
        for wall in room:
           if door.intersect(wall):
              ind_old_wall = room.index(wall)
              new_walls.append(LineSegment2(wall.p1, door - wall.copy().v.normalize() * door_size))
              new_walls.append(LineSegment2(door + wall.copy().v.normalize() * door_size, wall.p2))
        room.pop(ind_old_wall)
        room.append(new_walls[0])
        room.append(new_walls[1])

    def angle_polygon_tail(rooms, c):
        dict_update = {}
        for room in rooms:
            for poly in room:
                for side_p1, side_p2, next_side_p2 in zip(poly, poly[1:] + poly[:1], poly[2:] + poly[:2]):
                    side = LineSegment2(Point2(side_p1[0], side_p1[1]), Point2(side_p2[0], side_p2[1]))
                    next_side = LineSegment2(Point2(side_p2[0], side_p2[1]), Point2(next_side_p2[0], next_side_p2[1]))
                    na = side.v
                    nb = next_side.v
                    angle = na.angle(nb)
                    if not na.x * nb.y > nb.x * na.y:  # check if is left or right angle
                        if angle + 3.14 > 4.85:
                            dict_update[side_p2, rooms.index(room)] =\
                                [-side.v.normalize() * c + side_p2, next_side.v.normalize() * c + side_p2]
        # print(dict_update)
        outies = []
        for room in rooms:
            for poly in room:
                for key in dict_update.keys():
                    if key[0] in poly and rooms.index(room) == key[1]:
                        j = poly.index(key[0])
                        outies.append(key)
                        poly.pop(j)
                        poly.insert(j, (dict_update[key][0].x, dict_update[key][0].y))
                        poly.insert(j + 1, (dict_update[key][1].x, dict_update[key][1].y))
                for i in outies:
                    dict_update.pop(i)
                outies.clear()


    def noty_coord_polygon_in_rooms(rooms):
        inv_rooms = []
        for room in rooms:
            inv_room = []
            for poly in room:
                inv_poly = []
                for vertices in poly:
                    inv_poly.append((vertices[0], -vertices[1]))
                inv_room.append(inv_poly)
            inv_rooms.append(inv_room)
        return inv_rooms


    def plot_line(pt, next, *args):
        xs = [pt[0], next[0]]
        ys = [-pt[1], -next[1]]
        plt.plot(xs, ys, *args)


    def plot_linesegment2(edge, *args):
        xs = [edge.p1.x, edge.p2.x]
        ys = [-edge.p1.y, -edge.p2.y]
        plt.plot(xs, ys, *args)


    def plot_graph(graph, *args):
        for edge in graph.edges():
            xs = [edge[0].x, edge[1].x]
            ys = [-edge[0].y, -edge[1].y]
            plt.plot(xs, ys, *args)
        for node in graph.nodes():
            plt.plot(node.x, -node.y, "og")


    # function that check the visibilty between two node
    def visibility_check(first_node, second_node, euc_room):
          intsect = False
          for poly in euc_room:
            for wall in poly:
                if wall.intersect(LineSegment2(first_node, second_node)) is not None:
                    intsect = True
          if not intsect:
                to_totalpath.append((first_node, second_node))


    # next function is an evolution of the previous and it's needed to check also boundary of
    # the other room associated to the door_node

    def find_wall(node, euc_room):
        for wall in euc_room:
            if wall.intersect(node):
                return wall

    def main():

        # rooms mapping, first is the room contour, others hole in room like objects
        #room4 è il corridoio
        #room4 = [[(3, 5), (4, 5), (4, 4), (8, 4),(8, 2), (4, 2),(4, 1),(6, 1),(6,0),(3,0)]]
        rooms=Al.inserisciMappa()
        # Execution of tail_angle_function for angle>270

        angle_polygon_tail(rooms, 0.03)

        rooms = noty_coord_polygon_in_rooms(rooms)

        # list instance of the skeleton of rooms
        skeletons = []

        # list instance of the graphed skeleton of rooms that need to be semplified
        networks = []

        # list instance of euclidean rooms ( polygons of the rooms are coverted in
        # for the euclide package as LineSegment2)

        euc_rooms = []

        # plot of rooms
        for room in rooms:
            poly = room[0]
            holes = room[1:] if len(room) > 0 else None
            euc_room = []
            euc_poly = []
            for point, next in zip(poly, poly[1:] + poly[:1]):
                plot_line(point, next, "#333333")
                # create euclidean instances of the rooms and the holes of the rooms to be managed next
                euc_poly.append(LineSegment2(Point2(point[0], point[1]), Point2(next[0], next[1])))
            euc_room.append(euc_poly)
            for hole in holes:
                euc_hole = []
                for point, next in zip(hole, hole[1:] + hole[:1]):
                    euc_hole.append(LineSegment2(Point2(point[0], point[1]), Point2(next[0], next[1])))
                    plot_line(point, next, "#333333")
                euc_room.append(euc_hole)
            euc_rooms.append(euc_room)
            # print(euc_room)


            # Execution of the straight skeleton on a single room
            # print(poly)
            # print(holes)
            #print(polyskel.skeletonize(poly, holes))
            skeletons.append(polyskel.skeletonize(poly, holes))

        # print info about skeleton algo

        # for res in skeletons:
        #     print(res)

        # cycle that returns graph from skeletons
        for ind, skeleton in enumerate(skeletons):
            sg = nx.Graph(room=ind)
            for edge in skeleton:
                source = edge.source
                for sink in edge.sinks:
                    sg.add_edge(source, sink, weight=abs(source - sink))
            leaves = set()
            for node, degree in sg.degree():
                if degree < 2:
                    leaves.add(node)
            sg.remove_nodes_from(leaves)
            networks.append(sg)
            # plot_graph(sg, "b-")

        # construction of adjacency matrix to map doors with rooms

        #doors = [(3, -1), (8, -3)]
        doors = Al.inserisciPorte()
        adj_mat = []
        for door in doors:
            p = Point2(door[0], door[1])
            adj_row = []
            for euc_room in euc_rooms:
                door_in_room = False
                for wall in euc_room[0]:
                    i = wall._intersect_point2(p)
                    if i:
                        door_in_room = True
                adj_row.append(door_in_room)
            adj_mat.append(adj_row)
        #print(adj_mat)

        # find the shortest edges between the doors and the graph of the rooms\
        # that match the adjacency matrix

        door_paths = nx.Graph()
        for ind, door_map, in enumerate(adj_mat):
            for network, door_in_room in zip(networks, door_map):
                if door_in_room:
                    p = Point2(doors[ind][0], doors[ind][1])
                    connected = {}
                    outies = []
                    entries = []
                    for edge in network.edges():
                        if edge[0] == edge[1]:
                            connected[edge[0].connect(p)] = LineSegment2(edge[0], edge[1])
                            outies.append(LineSegment2(edge[0], edge[1]))
                        else:
                            l = LineSegment2(edge[0], edge[1])
                            connected[l.connect(p)] = l
                    con = min(connected.keys(), key=lambda ls: ls.length)
                    # print(connected[con].p1.x,connected[con].p1.y,connected[con].p2.x,connected[con].p2.y)
                    door_paths.add_edge(con.p1, con.p2, weight=abs(con.p1 - con.p2))
                    if connected[con].p1 != con.p1 and connected[con].p1 != con.p2 \
                            and connected[con].p2 != con.p1 and connected[con].p2 != con.p2:
                        if con.p1 != p:
                            outies.append(connected[con])
                            entries.append(LineSegment2(con.p1, connected[con].p1))
                            entries.append(LineSegment2(con.p1, connected[con].p2))
                        elif con.p2 != p:
                            outies.append(connected[con])
                            entries.append(LineSegment2(con.p2, connected[con].p1))
                            entries.append(LineSegment2(con.p2, connected[con].p2))
                    for i in outies:
                        #print(i.p1.x,i.p1.y,i.p2.x,i.p2.y)
                        if network.has_edge(i.p1, i.p2):
                            network.remove_edge(i.p1, i.p2)
                    for j in entries:
                        # print(j.p1.x,j.p1.y,j.p2.x,j.p2.y)
                        network.add_edge(j.p1, j.p2, weight=abs(j.p1 - j.p2))

        # merge all room_graph in a single graph and update node data to
        # know the room where is it
        #VALENTINA
        for network in networks:
             for node in network.nodes():
                 network.add_node(node, room=[network.graph['room']])

        global totalpath

        totalpath = nx.compose_all(networks)
        totalpath = nx.compose(totalpath, door_paths)

        # update doors with rooms intersections to extend node attribute

        ind = 0
        for node_door in door_paths.nodes():
            if (node_door.x, node_door.y) in doors:
                adj_row = adj_mat[ind]
                room_ass = []
                for dni, door_in_room in enumerate(adj_row):
                    if door_in_room:
                        room_ass.append(dni)
                totalpath.add_node(node_door, room=room_ass)
                ind += 1

        nodes_room = nx.get_node_attributes(totalpath, 'room')

        # for node in nodes_room:
        #      print(nodes_room)

        #function to insert two line instead one line where is a door
        #to simulate space visibility

        row_index=0
        for row in adj_mat :
            col_index = 0
            for col in row:
              if col:
                  open_room(euc_rooms[col_index][0],
                    Point2(doors[row_index][0],doors[row_index][1]))
              col_index += 1
            row_index +=1

        # for room in euc_rooms:
        #    for poly in room:
        #     for wall in poly:
        #           plot_linesegment2(wall, "r-")

        # visibilty graph teorically O(n^3)
        # The idea is to check for a node of a generic room if it has

        global to_totalpath
        to_totalpath = []

        room_list_node = nx.get_node_attributes(totalpath, 'room')

        # for node in room_list_node:
        #     print(room_list_node[node],node)

        for node_room in room_list_node:
            for nd_room in room_list_node:
                # it check edge intersection of nodes that stay in the same room
                if len(room_list_node[node_room]) == 1 and len(room_list_node[nd_room]) == 1 and \
                        room_list_node[nd_room][0] == room_list_node[node_room][0]:
                    visibility_check(node_room, nd_room, euc_rooms[room_list_node[node_room][0]])  # same room
                elif len(room_list_node[node_room]) == 2 and len(room_list_node[nd_room]) == 1:  # node_room is a door
                    if room_list_node[node_room][0] == room_list_node[nd_room][0]:
                        visibility_check(node_room, nd_room, euc_rooms[room_list_node[node_room][0]])
                    if room_list_node[node_room][1] == room_list_node[nd_room][0]:
                        visibility_check(node_room, nd_room, euc_rooms[room_list_node[node_room][1]])
                elif len(room_list_node[node_room]) == 2 and len(room_list_node[nd_room]) == 2:
                    if room_list_node[node_room][0] == room_list_node[nd_room][0]:
                        visibility_check(node_room, nd_room, euc_rooms[room_list_node[node_room][0]])
                    if room_list_node[node_room][1] == room_list_node[nd_room][0]:
                        visibility_check(node_room, nd_room, euc_rooms[room_list_node[node_room][1]])
                    if room_list_node[node_room][0] == room_list_node[nd_room][1]:
                        visibility_check(node_room, nd_room, euc_rooms[room_list_node[node_room][0]])
                    if room_list_node[node_room][1] == room_list_node[nd_room][1]:
                        visibility_check(node_room, nd_room, euc_rooms[room_list_node[node_room][1]])

        # now we want to filter the visibility edge that intersect skeleton graph (in this case totalgraph)

        to_remove = []
        for arc in to_totalpath:
            for edge in totalpath.edges():
                intersection = LineSegment2(arc[0], arc[1]).intersect(LineSegment2(edge[0], edge[1]))
                if intersection is not None and intersection != arc[0] \
                        and intersection != arc[1] and intersection != edge[0] and intersection != edge[1]:
                    if arc not in to_remove:
                        to_remove.append(arc)
        for arc in to_remove:
            to_totalpath.remove(arc)

        # plot the visibility graph
        # for edge in to_totalpath:
        #     totalpath.add_edge(edge[0], edge[1])

        tmp=nx.Graph()

        for edge in to_totalpath:
             tmp.add_edge(edge[0], edge[1])


# filter visibility graph throught buffers on euc_rooms

        global buffers
        buffers = []

        for room in euc_rooms:
          for poly in room:
            for wall in poly:
                holes = []
                for door in doors:
                    p = Point2(door[0], door[1])
                    if p.intersect(wall):
                        holes.append(p)
                buffer_from_linesegment(wall, holes)

        # filter total_graph

        ondelete = []

        for buffer in buffers:
            for edge in tmp.edges():
                if buffer._intersect_line2(LineSegment2(edge[0], edge[1])):
                    ondelete.append(edge)
            #plot_linesegment2(buffer.side1, 'm-')
            #plot_linesegment2(buffer.side2, 'm-')

        ondelete = list(dict.fromkeys(ondelete))
        ondelete.sort()
        ondelete.reverse()

        for edge in ondelete:
            # print(ind)
            tmp.remove_edge(edge[0], edge[1])

# delete nodes not achievable,main door is the firsr node to achieve anyother

        outies = set()

        for node in totalpath.nodes():
            try:
                nx.dijkstra_path(totalpath, Point2(doors[0][0], doors[0][1]), node)

            except nx.exception.NetworkXNoPath as ne:
                outies.add(node)
        totalpath.remove_nodes_from(outies)


        tmp=nx.compose(tmp,totalpath)

        plot_graph(tmp, "b-")

        #plt.show()

        plt.savefig('vis.png')
        Al.nodes_room=nodes_room
        Al.totalpath=tmp
        Al.startPoint()

main()
