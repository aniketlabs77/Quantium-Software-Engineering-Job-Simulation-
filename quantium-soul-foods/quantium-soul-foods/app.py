import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("data/processed_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = Dash(__name__)

app.layout = html.Div(
    style={"fontFamily": "Segoe UI, sans-serif", "backgroundColor": "#f8f4f0", "minHeight": "100vh", "padding": "20px"},
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            id="header",
            style={
                "textAlign": "center",
                "color": "#c0396b",
                "marginBottom": "5px",
                "fontSize": "2.2rem",
                "fontWeight": "700",
                "letterSpacing": "0.5px"
            }
        ),
        html.P(
            "Soul Foods — Impact of the January 15, 2021 Price Increase",
            style={"textAlign": "center", "color": "#888", "marginTop": "0", "marginBottom": "25px", "fontSize": "1rem"}
        ),

        html.Div(
            style={"textAlign": "center", "marginBottom": "25px"},
            children=[
                html.Label("Filter by Region:", style={"fontWeight": "600", "color": "#444", "marginRight": "12px", "fontSize": "0.95rem"}),
                dcc.RadioItems(
                    id="region-picker",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"display": "inline-block"},
                    inputStyle={"marginRight": "5px", "accentColor": "#c0396b"},
                    labelStyle={"marginRight": "18px", "color": "#333", "fontSize": "0.95rem", "cursor": "pointer"}
                )
            ]
        ),

        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "borderRadius": "12px",
                "boxShadow": "0 2px 12px rgba(0,0,0,0.08)",
                "padding": "20px"
            },
            children=[
                dcc.Graph(id="sales-chart")
            ]
        ),

        html.Div(
            style={"textAlign": "center", "marginTop": "18px", "color": "#aaa", "fontSize": "0.8rem"},
            children=[html.Span("Data provided by Soul Foods · Quantium")]
        )
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-picker", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered = df.copy()
    else:
        filtered = df[df["region"] == selected_region].copy()

    grouped = filtered.groupby("date", as_index=False)["sales"].sum()

    fig = px.line(
        grouped,
        x="date",
        y="sales",
        labels={"date": "Date", "sales": "Total Sales ($)"},
        title=f"Daily Pink Morsel Sales — Region: {selected_region.capitalize()}"
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="#e74c3c",
        annotation_text="Price Increase",
        annotation_position="top right",
        annotation_font_color="#e74c3c"
    )

    fig.update_traces(line_color="#c0396b", line_width=2.5)

    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        font={"family": "Segoe UI, sans-serif", "color": "#333"},
        xaxis={"showgrid": True, "gridcolor": "#f0f0f0"},
        yaxis={"showgrid": True, "gridcolor": "#f0f0f0"},
        title_font_size=16,
        margin={"t": 60, "b": 40, "l": 60, "r": 40},
        hovermode="x unified"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
