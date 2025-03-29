# Sankey Diagram

This project demonstrates how to create an advanced Sankey diagram using Plotly in Python. The diagram visualizes the flow of resources between different sources and targets, providing a clear representation of relationships and values.

## Features

- **Interactive Visualization**: Users can hover over links to see the flow values.
- **Custom Colors**: Distinct colors for nodes and links enhance visual clarity.
- **Annotations**: Additional context is provided through annotations.
- **Easy to Customize**: Modify labels, values, and colors to fit your data.

## Installation

To get started, clone this repository and install the required libraries:

## bash
git clone https://github.com/olabodegenius/sankey-diagram.git
cd advanced-sankey-diagram
pip install plotly

## Usage
Run the script to generate the Sankey diagram:
python advanced_sankey_diagram.py

![image](https://github.com/user-attachments/assets/658e128f-6ce5-4ab7-b82a-968797057e04)

## Code Overview
The code creates a Sankey diagram with the following components:
Labels: Defines the names of the nodes (sources and targets).
Source and Target: Lists that define the connections between nodes.
Values: Represents the magnitude of the flow between nodes.
Node Colors: Custom colors for each node to improve visual distinction.
Link Colors: Custom colors for each link to enhance clarity.

## Example
The following example demonstrates the flow of resources from three sources to three targets:

- **Source A contributes to Target X and Target Y.
- **Source B contributes to Target Y and Target Z.
- **Source C contributes to Target X and Target Z.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Plotly - Library for creating interactive visualizations.



