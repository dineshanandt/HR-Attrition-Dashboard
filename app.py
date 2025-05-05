import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Load the cleaned data
df = pd.read_csv("attrition_dashboard_data.csv")

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    html.H1("HR Attrition Dashboard", className="text-center mb-4"),

    dbc.Row([
        dbc.Col([
            html.Label("Select Department:"),
            dcc.Dropdown(
                id="dept-filter",
                options=[{"label": d, "value": d} for d in sorted(df["Department"].unique())],
                placeholder="All Departments",
                clearable=True
            )
        ], width=6)
    ], className="mb-4"),

    dbc.Row([dbc.Col(dcc.Graph(id="attrition-by-jobrole"))]),
    dbc.Row([dbc.Col(dcc.Graph(id="revenue-by-department"))]),
    dbc.Row([dbc.Col(dcc.Graph(id="avg-tenure-heatmap"))])
], fluid=True)

# Callback
@app.callback(
    Output("attrition-by-jobrole", "figure"),
    Output("revenue-by-department", "figure"),
    Output("avg-tenure-heatmap", "figure"),
    Input("dept-filter", "value")
)
def update_charts(dept):
    filtered_df = df[df["Department"] == dept] if dept else df

    # Chart 1: Attrition by Job Role
    fig1 = px.histogram(
        filtered_df,
        x="JobRole",
        color="Attrition",
        title="Attrition by Job Role",
        barmode="group",
        template="plotly_white"
    )

    # Chart 2: Revenue Loss by Department (always show all departments)
    rev_loss_df = df.groupby("Department")["RevenueLoss"].sum().reset_index()
    colors = ['lightslategray'] * len(rev_loss_df)

    if dept:
        idx = rev_loss_df[rev_loss_df["Department"] == dept].index[0]
        colors[idx] = 'crimson'

    fig2 = px.bar(
        rev_loss_df,
        x="Department",
        y="RevenueLoss",
        title="Revenue Loss by Department",
        template="plotly_white",
        text_auto='.2s'
    )
    fig2.update_traces(marker_color=colors)
    fig2.update_layout(
        yaxis_title="Revenue Loss",
        xaxis_title="Department",
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )

    # Chart 3: Heatmap of Avg Years at Company by JobRole × Department
    pivot = filtered_df.pivot_table(
        index="JobRole",
        columns="Department",
        values="YearsAtCompany",
        aggfunc="mean"
    )

    fig3 = px.imshow(
        pivot,
        text_auto=True,
        aspect="auto",
        title="Avg Tenure (YearsAtCompany) by Role × Dept",
        color_continuous_scale="Viridis"
    )
    fig3.update_layout(
        xaxis_title="Department",
        yaxis_title="Job Role"
    )

    return fig1, fig2, fig3

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
