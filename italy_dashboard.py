import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import numpy as np

df = pd.read_excel("Italy.xlsx", header=20, sheet_name=3)

# normalise columns' names
lower_dict = {}

for col in df.columns:
    if type(col) == str:
        lower_dict[col] = col.lower()
    else:
        lower_dict[col] = str(col)
df = df.rename(columns=lower_dict)
df = df.rename(columns={"odname": "country"})

# cleansing the dataset  
df = df[df.areaname != 'World']
df = df.replace({"..": 0})
replace_dict = {
    "United Kingdom of Great Britain and Northern Ireland": "UK",
    "China (including Hong Kong Special Administrative Region)": "China",
    "Democratic People's Republic of Korea": "Korea",
    "Iran (Islamic Republic of)": "Iran",
    "Lao People's Democratic Republic": "Lao's People",
    "The former Yugoslav Republic of Macedonia": "Macedonia",
    "Venezuela (Bolivarian Republic of)": "Venezuela",
}
df["country"] = df["country"].replace(replace_dict)


# defining year list
year_list = [str(i) for i in range(1990, 2014, 1)]

# Create a dash application layout
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # TASK 2.1 Add title to the dashboard
        html.H1(
            "Italian Migration Statistics Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 24},
        ),
        html.Div(
            [
                # TASK 2.2: Add Statistics menu
                html.Label("Select Statistics:"),
                dcc.Dropdown(
                    id="select-statistics",
                    options=[
                        {"label": "Immigrant Statistics", "value": "Immigrants"},
                        {
                            "label": "Emigrant Statistics",
                            "value": "Emigrants",
                        },
                    ],
                    placeholder="Select a report type",
                    value="Select Statistics",
                    style={"padding-left": 35, "font-size": 20, "textAlign": "center"},
                ),
            ]
        ),
        # Add second Year menu
        html.Div(
            dcc.Dropdown(
                id="select-year",
                options=[{"label": i, "value": i} for i in year_list],
                value=None,
                placeholder="Select Year",
            )
        ),

        # add Continent menu
        html.Div(
            dcc.Dropdown(
                id="select-continent",
                options=[{"label": i, "value": i} for i in set(df['areaname'])],
                value=None,
                placeholder="Select Continent",
            )
        ),
        html.Div(
            [
                # TASK 2.3: Add a division for output display
                html.Div(
                    id="output-container",
                    className="chart-grid",
                    style={"display": "flex"},
                ),
            ]
        ),
    ]
)
    

# Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id="output-container", component_property="children"),
    [
        Input(component_id="select-year", component_property="value"),
        Input(component_id="select-statistics", component_property="value"),
        Input(component_id="select-continent", component_property="value")
    ],
)
def update_output_container(input_year, selected_statistics, selected_continent):

    # filter the dataset
    data = df[df["type"] == selected_statistics]
    data = data[data.country != 'Italy']

    ######################################################
    # Plot 1: Fluctuation from 1991 to 2013 
    year_count = data[year_list].sum(axis=0).reset_index()
    # Rename columns
    year_count = year_count.rename(columns={"index": "Year", 0: "Count"})
    fig1 = px.line(
        year_count,
        x="Year",
        y="Count",
        title=f"Count of {selected_statistics} from/to Italy",
    )
    chart_1 = dcc.Graph(figure=fig1)
    ####################################################
    # Plot 2 Proportion of Im/Em by Continent in Year Selected
    if (input_year is not None) and (selected_continent is not None):
        # filter data by continent
        continent = data.loc[data['areaname'] == selected_continent]

        # group by countries in the continent 
        country = continent.groupby('country')[input_year].sum()

        # select top 5 countries 
        country = country.nlargest().reset_index()

        # Rename columns
        country = country.rename(columns={"country": "Country", input_year: "Count"})
        
        fig2 = fig2=px.pie(
                country,
                values="Count",
                names="Country",
                title=f"Proportion of {selected_statistics} from/to Italy by {selected_continent} in {input_year}"
        )
        chart_2 = dcc.Graph(figure=fig2)

    else:
        chart_2 = None

    ###########################################################
    # Plot 3 Top 5 Countries of Im/Em from/to Italy in Year Selected 
    if (input_year is not None):
        countries = data.groupby('country')[input_year].sum().nlargest().reset_index()
        
        fig3 = px.bar(
            countries,
            x="country",
            y=input_year,
            title=f"Top 5 Countries of {selected_statistics} from/to Italy in {input_year}",
        )
        chart_3 = dcc.Graph(figure=fig3)

    else:
        chart_3 = None
        
    #######################################################
    # Plot 4: Im/Em Proportion from/to Italy by Continent from 1991 to 2013 
    if (input_year is not None) and (selected_continent is not None):
    
        # filter dataset by continent
        continent = data.loc[data['areaname'] == selected_continent] 

        # count Im/Em from continent 
        continent = continent[year_list].sum(axis=0)

        # count total Im/Em
        tot = data[year_list].sum(axis=0)

        # calculate proportion of continenr Im/Em 
        continent_proportion = ((continent / tot) *100).reset_index()
        continent_proportion = continent_proportion.rename(columns={"index": "Year", 0: "Percentage"})

        fig4 = px.line(
            continent_proportion,
            x="Year",
            y="Percentage",
            title=f"Proportion of {selected_continent} {selected_statistics} from Italy from 1991 to 2013"
        )
        chart_4 = dcc.Graph(figure=fig4)
    else:
        chart_4 = None
    ########################################################

    html_return = [
        html.Div(
            className="chart-item",
            children=[html.Div(children=chart_1), 
                      html.Div(children=chart_2)
                     ],
        ),
        html.Div(
            className="chart-item",
            children=[html.Div(children=chart_3),
                      html.Div(children=chart_4)
                     ],
        ),
    ]
    
    return html_return
        


# Run the Dash app
if __name__ == "__main__":
    app.run_server(port=6006, debug=True)
