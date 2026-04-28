import plotly.graph_objects as go

def trend_chart(data, keyword):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data.index,
        y=data[keyword],
        mode='lines',
        name=keyword
    ))

    fig.update_layout(
        template="plotly_dark",
        height=300,
        margin=dict(l=10, r=10, t=30, b=10)
    )

    return fig
