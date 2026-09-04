import os
import dash
from dash import dcc, html
from dotenv import load_dotenv
from neo4j import GraphDatabase
import pandas as pd
import plotly.express as px

# Load environment variables from a local .env file
load_dotenv()

# Secure Database Configuration with fallbacks
URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "password123")  # Fallback for local testing only

AUTH = (USER, PASSWORD)

def load_data():
    """Fetches cleaned graph payload datasets from Neo4j."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    with driver.session() as session:
        df_engagement = pd.DataFrame(session.run("""
            MATCH (q:Question)
            RETURN q.view_count AS Views, q.answer_count AS Answers, q.title AS Title
        """).data())
        
        df_scores = pd.DataFrame(session.run("""
            MATCH (a:Answer)
            RETURN a.score AS Score, a.is_accepted AS IsAccepted
        """).data())
    driver.close()
    return df_engagement, df_scores

# Load dataset outputs
dfEngagement, dfScores = load_data()

# Calculate Summary Metrics
total_questions = len(dfEngagement)
total_answers = len(dfScores)

# Build Interactive Visualizations
fig_scatter = px.scatter(
    dfEngagement, 
    x="Views", 
    y="Answers", 
    hover_name="Title", 
    title="Question Engagement: Views vs. Popularity", 
    template="plotly_dark",
    color="Answers",
    color_continuous_scale="Viridis",
    labels={"Views": "Total Views", "Answers": "Total Responses"}
)
fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

fig_box = px.box(
    dfScores, 
    x="IsAccepted", 
    y="Score", 
    title="Score Dispersal by Acceptance Status", 
    template="plotly_dark",
    color="IsAccepted",
    labels={"IsAccepted": "Accepted?", "Score": "Vote Weight / Score"}
)
fig_box.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

# Create Clean-Themed Dash App Layout
app = dash.Dash(__name__)

app.layout = html.Div(style={
    'backgroundColor': '#121212', 
    'color': '#E0E0E0', 
    'fontFamily': 'Segoe UI, Helvetica, sans-serif',
    'padding': '30px'
}, children=[
    
    # Dashboard Header Area
    html.Div(style={'textAlign': 'center', 'marginBottom': '40px'}, children=[
        html.H1("Stack Overflow Graph Analytics", style={'fontSize': '32px', 'fontWeight': 'bold', 'color': '#FFFFFF'}),
        html.P("Exploratory system metrics derived from graph relations and node payload schemas.", style={'color': '#888888', 'fontSize': '16px'})
    ]),
    
    # KPI Row (Summary Cards)
    html.Div(style={'display': 'flex', 'justifyContent': 'center', 'gap': '30px', 'marginBottom': '40px'}, children=[
        html.Div(style={
            'backgroundColor': '#1E1E1E', 'padding': '20px 40px', 'borderRadius': '10px', 'textAlign': 'center', 'border': '1px solid #333'
        }, children=[
            html.H3("Questions Analyzed", style={'fontSize': '14px', 'color': '#888888', 'textTransform': 'uppercase'}),
            html.H1(f"{total_questions:,}", style={'fontSize': '36px', 'margin': '5px 0', 'color': '#00ADB5'})
        ]),
        html.Div(style={
            'backgroundColor': '#1E1E1E', 'padding': '20px 40px', 'borderRadius': '10px', 'textAlign': 'center', 'border': '1px solid #333'
        }, children=[
            html.H3("Answers Ingested", style={'fontSize': '14px', 'color': '#888888', 'textTransform': 'uppercase'}),
            html.H1(f"{total_answers:,}", style={'fontSize': '36px', 'margin': '5px 0', 'color': '#393E46'})
        ])
    ]),
    
    # Interactive Graphics Layout
    html.Div(style={'display': 'flex', 'flexDirection': 'column', 'gap': '30px'}, children=[
        # Scatter Card
        html.Div(style={
            'backgroundColor': '#1E1E1E', 'padding': '25px', 'borderRadius': '10px', 'border': '1px solid #333'
        }, children=[
            dcc.Graph(figure=fig_scatter)
        ]),
        
        # Box Card
        html.Div(style={
            'backgroundColor': '#1E1E1E', 'padding': '25px', 'borderRadius': '10px', 'border': '1px solid #333'
        }, children=[
            dcc.Graph(figure=fig_box)
        ])
    ])
])

if __name__ == "__main__":
    app.run(debug=True, port=8050)