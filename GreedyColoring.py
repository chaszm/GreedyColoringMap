



#  US map as a graph with adjacent states shown
us_map = {
    'Alabama': ['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
    'Alaska': [],
    'Arizona': ['California', 'Colorado', 'Nevada', 'New Mexico', 'Utah'],
    'Arkansas': ['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
    'California': ['Arizona', 'Nevada', 'Oregon'],
    'Colorado': ['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
    'Connecticut': ['Massachusetts', 'New York', 'Rhode Island'],
    'Delaware': ['Maryland', 'New Jersey', 'Pennsylvania'],
    'Florida': ['Alabama', 'Georgia'],
    'Georgia': ['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
    'Hawaii': [],
    'Idaho': ['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
    'Illinois': ['Indiana', 'Iowa', 'Kentucky', 'Missouri', 'Wisconsin'],
    'Indiana': ['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
    'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
    'Kansas': ['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
    'Kentucky': ['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
    'Louisiana': ['Arkansas', 'Mississippi', 'Texas'],
    'Maine': ['New Hampshire'],
    'Maryland': ['Delaware', 'Pennsylvania', 'Virginia', 'West Virginia'],
    'Massachusetts': ['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
    'Michigan': ['Indiana', 'Ohio', 'Wisconsin'],
    'Minnesota': ['Iowa', 'North Dakota', 'South Dakota', 'Wisconsin'],
    'Mississippi': ['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'],
    'Missouri': ['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
    'Montana': ['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
    'Nebraska': ['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
    'Nevada': ['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
    'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
    'New Jersey': ['Delaware', 'New York', 'Pennsylvania'],
    'New Mexico': ['Arizona', 'Colorado', 'Oklahoma', 'Texas'],
    'New York': ['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Vermont'],
    'North Carolina': ['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
    'North Dakota': ['Minnesota', 'Montana', 'South Dakota'],
    'Ohio': ['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
    'Oklahoma': ['Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
    'Oregon': ['California', 'Idaho', 'Nevada', 'Washington'],
    'Pennsylvania': ['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
    'Rhode Island': ['Connecticut', 'Massachusetts'],
    'South Carolina': ['Georgia', 'North Carolina'],
    'South Dakota': ['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
    'Tennessee': ['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
    'Texas': ['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
    'Utah': ['Arizona', 'Colorado', 'Idaho', 'Nevada', 'Wyoming'],
    'Vermont': ['Massachusetts', 'New Hampshire', 'New York'],
    'Virginia': ['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
    'Washington': ['Idaho', 'Oregon'],
    'West Virginia': ['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
    'Wisconsin': ['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
    'Wyoming': ['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
}



    # greedy algorithm for Graph Coloring Problem
def greedy_state_algorithm(graph, colors):
    color_map = {}  # stores color of each state

    # Sort states by the number of adjacent states
    sorted_states = sorted(graph.keys(), key=lambda state: -len(graph[state]))

    for state in sorted_states:
        
        available_colors = set(colors)


        # Check colors of adjacent states and removes them 
        for adj in graph[state]:
            if adj in color_map:
                if color_map[adj] in available_colors:
                    available_colors.remove(color_map[adj]) #removes



        # Color state with lowest available color
        if available_colors:
            color_map[state] = min(available_colors)
    
    return color_map




colors = ['Red', 'Blue', 'Green', 'Yellow']



coloring = greedy_state_algorithm(us_map, colors) #color in the map

# Create a lookup table with states and their colors
state_table = {state: coloring[state] for state in us_map.keys()}


for state, color in state_table.items():
    print(f"{state}: {color}")
