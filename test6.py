import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components import Br
from dash.dependencies import Input, Output
import plotly.express as px
import dash_table
from readDB import ReadMongoData as db

# df = pd.read_csv("Urban_Park_Ranger_Animal_Condition_Response.csv")
#bookingdetails = db.getBookingDetails()
bookings = db.getBookings()
agents = db.getAgents()
# customers = db.getCustomers()
# agents = db.getAgents()
bookings[["totalPrice"]] = bookings[["totalPrice"]].astype(str).astype(float)

bookings_agents = pd.merge(bookings, agents, on="AgentId")
bookings_agents
bookings_agents.rename(columns={'title': 'Destination', 'totalPrice': 'Total Price'}, inplace=True)


# agents_customers = pd.merge(customers, agents, on="AgentId")
# agents_customers

# bookings_with_details_agents_customers = pd.merge(bookings_with_details, agents_customers, on="CustomerId")
# bookings_with_details_agents_customers


# bookings_with_details_agents_customers[["totalPrice", "AgencyCommission"]] = bookings_with_details_agents_customers[["totalPrice", "AgencyCommission"]].astype(str).astype(float)
# # bookings_with_details_agents_customers[["totalPrice", "AgencyCommission"]] = bookings_with_details_agents_customers[["totalPrice", "AgencyCommission"]].astype(str).astype(float)

# # you need to include __name__ in your Dash constructor if
# # you plan to use a custom CSS or JavaScript in your Dash apps

# # Grouping by:
bookings_agents.rename(columns={'title': 'Destination', 'totalPrice': 'Total Price', 'AgtLastName': 'Agent Last Name'}, inplace=True)
df_group_destination = bookings_agents.groupby(["Destination"]).sum()[["Total Price"]]

#[["totalPrice"]]
# [["totalPrice","customerId"]]

df_group_agent_sales = bookings_agents.groupby(["Agent Last Name"]).sum()[["Total Price"]]


# df_group_destination = bookings_with_details_agents_customers.groupby(["Destination"]).sum()[
#     ["totalPrice", "AgencyCommission"]]

# df_group_comission = bookings_with_details_agents_customers.groupby(["Destination"]).sum()[
#     ["AgencyCommission"]]
# df_group_comission_mean = bookings_with_details_agents_customers.groupby(["Destination"]).mean()

# df_group_agent_commission = bookings_with_details_agents_customers.groupby(["AgtLastName"]).sum()[
#     ["AgencyCommission"]]


# df_group_customer_sales = bookings_with_details_agents_customers.groupby(["CustLastName"]).sum()[
#     ["totalPrice"]]

# # df_group_packages = packages.groupby(["PkgName"]).sum()[
#     # ["PkgtotalPrice", "PkgAgencyCommission"]]


# # ====================Figures:======================
 
fig = px.bar(df_group_destination,
              x=df_group_destination.index, y="Total Price", color = "Total Price")
fig.update_layout(
    title={
        'text': "Total Sales",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})


# 2nd Figure

fig2 = px.bar(df_group_agent_sales,
              x=df_group_agent_sales.index, y="Total Price", color = "Total Price")
fig2.update_layout(
    title={
        'text': "Sales Per Agent",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

# # 3rd Figure

# fig3 = px.bar(df_group_comission,
#               x=df_group_comission.index, y="AgencyCommission", color = "AgencyCommission")
# fig3.update_layout(
#     title={
#         'text': "Total Agency Commission",
#         'y':0.95,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'})

# # 4th Figure

# fig4 = px.bar(df_group_comission_mean,
#               x=df_group_comission_mean.index, y="AgencyCommission", color = "AgencyCommission")
# fig4.update_layout(
#     title={
#         'text': "Average Agency Commission",
#         'y':0.95,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'})

# # 5th Figure

# fig5 = px.bar(df_group_agent_commission,
#               x=df_group_agent_commission.index, y="AgencyCommission", color = "AgencyCommission")
# fig5.update_layout(
#     title={
#         'text': "Commission Per Agent",
#         'y':0.95,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'})

# # 6th Figure

# fig6 = px.bar(df_group_customer_sales,
#               x=df_group_customer_sales.index, y="totalPrice", color = "totalPrice")
# fig6.update_layout(
#     title={
#         'text': "Sales Per Customer",
#         'y':0.95,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'})

# # 7th Figure

# # fig7 = px.bar(df_group_packages,
#             #   x=df_group_packages.index, y="PkgtotalPrice", color = "PkgtotalPrice")
# # fig7.update_layout(
#     # title={
#         # 'text': "Sales Per Package",
#         # 'y':0.95,
#         # 'x':0.5,
#         # 'xanchor': 'center',
#         # 'yanchor': 'top'})




app = dash.Dash(__name__)

# #---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.H1(['Travel Experts Data Analytics']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                    {'label': 'Destination', 'value': 'Destination'},
                    {'label': 'Agent Last Name', 'value': 'Agent Last Name'},
                    {'label': 'Traveler Count', 'value': 'travellerCount'},
                    # {'label': 'Customer Last Name', 'value': 'CustLastName'},
                    #  {'label': 'Species', 'value': 'Animal Class'},
                    #  {'label': 'Species Status', 'value': 'Species Status'}
            ],
            value='Destination',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    html.Div([
        dcc.Graph(id='the_graph')
    ]),
        #=================Graphs=================
        #dcc.Graph(figure=fig)
        dcc.Graph(id='f1', figure=fig),
        html.Br(),
        html.Br(),
        dcc.Graph(id='f2', figure=fig2),
        html.Br(),
        html.Br(),
        # dcc.Graph(id='f3', figure=fig3),
        # html.Br(),
        # html.Br(),
        # dcc.Graph(id='f4', figure=fig4),
        # html.Br(),
        # html.Br(),
        # dcc.Graph(id='f5', figure=fig5),
        # html.Br(),
        # html.Br(),
        # dcc.Graph(id='f6', figure=fig6),
        # html.Br(),
        # html.Br(),
        # dcc.Graph(id='f7', figure=fig7),
    ]),

])

# #---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = bookings_agents

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True, port=8600)