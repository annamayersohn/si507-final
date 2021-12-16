import json
import plotly.graph_objects as go
import plotly.express as px
from class_constructor import Node, Name

with open('tree_json.json', 'r') as filepath:
    tree_json = json.load(filepath)

nodes = []
for key in tree_json.keys():
    vals = tree_json[key]
    if vals['type'] == 'name':
        node = Name(vals['type'], vals['text'], vals['href'], vals['usage'], vals['html_class'], vals['number'], vals['note'], vals['gender'], vals['rating'], vals['children'])
    else:
        node = Node(vals['type'], vals['text'], vals['href'], vals['usage'], vals['html_class'], vals['number'], vals['note'], vals['children'])
    nodes.append(node)

for node in nodes:
    if node.children:
        for i in range(len(node.children)):
            child = node.children[i]
            child_node = nodes[int(child)]
            node.children[i] = child_node
    else:
        pass


print("Hello! Today we're going to learn about names descended from the Classical Hebrew word 'chanan', which means 'to be gracious.' The source of this data is BehindTheName.com.\n")


options = {'1': 168, '2': 17, '3': 136, '4': 66, '5': 199, '6': 263, '7': 50}
question = 'Enter the number next to the name whose evolution you wish to see. Then press enter.\n1. Nettie (English)\n2. Ancuța (Romanian)\n3. Nainsí (Irish)\n4. Antje (Frisian)\n5. Neli (Bulgarian)\n6. Hendel (Yiddish)\n7. Annick (French)\n'
choice = input(question)
keep_going = True



while keep_going == True:
    if choice in options.keys():
        leaf_index = options[choice]
        leaf = nodes[leaf_index]
        print(f'\nOpening table for {leaf.make_string()} in browser\n')
        ancestry = leaf.find_ancestry(nodes)
        fig = go.Figure(data=[go.Table(header=dict(values=['Name or word', 'Usage', 'Gender', 'User Rating']), cells=dict(values=[ancestry[0], ancestry[1], ancestry[2], ancestry[3]]))])
        fig.show()
        next_q = '\nTo see the evolution of another name, press 1. To move on to the next set of options, press 2.\n'
        next_choice = False
        answer = input(next_q)
        while next_choice == False:
            if answer == '1':
                choice = input(question)
                next_choice = True
            elif answer == '2':
                next_choice = True
                keep_going = False
            else:
                print('\nNot a valid input\n')
                answer = input(next_q)
    else:
        print('\nNot a valid input\n')
        choice = input(question)

print("\nNow let's look at some subsections of the family tree.\n")
current = nodes[3]
names, parents, ratings = current.treemap_descendants(current, [], [], [])
keep_going = True
while keep_going == True:
    while len(names) > 30:
        question = f'\nSelect a child of the name {current.txt} ({current.lang}).\n'
        number = 1
        options = []
        for child in current.children:
            child_children, child_parents, child_ratings = child.treemap_descendants(child, [child.make_string()], [''], [f'{child.rating}% of users like this name.'])
            if child.children and len(child_children) > 2:
                options.append(child)
                question += str(number) + '. ' + child.make_string() + '\n'
                number += 1
            else:
                pass
        choice = input(question)
        try:
            choice = int(choice)
            if choice in range(1, (len(options) + 1)):
                current = options[choice - 1]
                names, parents, ratings = current.treemap_descendants(current, [current.make_string()], [''], [f'{current.rating}% of users like this name.'])
            else:
                print('\nNot a valid input\n')
        except:
            print('\nNot a valid input\n')
    print(f'\nOpening treemap for {current.make_string()} in browser\n')
    fig = px.treemap(
        names = names,
            parents = parents,
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_traces(text=ratings, selector=dict(type='treemap'))
    fig.update_traces(textinfo='label + text', selector=dict(type='treemap'))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig.show()
    next_q = '\nTo select another subsection of the family tree, press 1. To end the program, press 2.\n'
    next_choice = False
    answer = input(next_q)
    while next_choice == False:
        if answer == '1':
            current = nodes[3]
            names, parents, ratings = current.treemap_descendants(current, [], [], [])
            next_choice = True
        elif answer == '2':
            print('\nGoodbye! Thank you!')
            next_choice = True
            keep_going = False
        else:
            print('\nNot a valid input\n')
            answer = input(next_q)


