import plotly.graph_objects as go

# Define labels for the nodes
labels = ["Source A", "Source B", "Source C", "Target X", "Target Y", "Target Z"]

# Define the source and target indices for the links
source = [0, 0, 0, 1, 1, 1, 1]
target = [3, 3, 4, 4, 5, 5, 5]
values = [8, 2, 4, 8, 4, 2, 3]

# Define colors for the nodes
node_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors  # Set custom colors for nodes
    ),
    link=dict(
        source=source,
        target=target,
        value=values,
        color=['rgba(31, 119, 180, 0.8)', 'rgba(255, 127, 14, 0.8)', 'rgba(44, 160, 44, 0.8)',
               'rgba(214, 39, 40, 0.8)', 'rgba(148, 103, 189, 0.8)', 'rgba(140, 86, 75, 0.8)',
               'rgba(31, 119, 180, 0.5)']  # Set custom colors for links
    )
)])

# Update layout with title and annotations
fig.update_layout(
    title_text="Advanced Sankey Diagram",
    font_size=10,
    annotations=[
        dict(
            x=0.5,
            y=1.1,
            xref="paper",
            yref="paper",
            text="Flow of Resources",
            showarrow=False,
            font=dict(size=16)
        )
    ]
)

# Show the figure
fig.show()
