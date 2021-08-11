# This program needed to connect to MongoDB for TravelExperts hosted on Atlas
# It has functions to get the data from different tables/collections
# If the Online DB is not accessible, you need to host it on Atlas.
# Create and Atlas account https://cloud.mongodb.com/ and add a username and open network IP address
# Configure your username and passwork below
# You can get the cluster URL from Atlas. On the cluster check the connection instructions (click connect)

# pip install pymongo dnspython

from pymongo import MongoClient
import pandas as pd
DB_USERNAME = "osama_124"
DB_PASSWORD = "YpDYuGHSvbeeiuIM"
DB_CLUSTER_URL = "cluster0.c0cml.mongodb.net"
# Connect the MongoDB
# ======================
# Making a Connection with MongoClient
client = MongoClient(
    f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@{DB_CLUSTER_URL}")
# database
db = client["myFirstDatabase"]


def getAgentCommissions():
    agentcommissions_table = db["agentcommissions"].find({})
    agentcommissions = pd.DataFrame(agentcommissions_table)
    agentcommissions.set_index("_id", inplace=True)
    return agentcommissions


def getBookings():
    bookings_table = db["bookings"].find({})
    bookings = pd.DataFrame(bookings_table)
    bookings.set_index("_id", inplace=True)
    return bookings

# # bookings_with_details = pd.merge(bookings, bookingdetails, on="BookingId")
# # print(bookings_with_details)


def getAgencies():
    agencies_table = db["agencies"].find({})
    agencies = pd.DataFrame(agencies_table)
    agencies.set_index("_id", inplace=True)
    return agencies


# def getRegions():
#     regions_table = db["regions"].find({})
#     regions = pd.DataFrame(regions_table)
#     regions.set_index("_id", inplace=True)
#     return regions


# def getClasses():
#     classes_table = db["classes"].find({})
#     classes = pd.DataFrame(classes_table)
#     classes.set_index("_id", inplace=True)
#     return classes


# def getProductsSuppliers():
#     products_suppliers_table = db["products_suppliers"].find({})
#     products_suppliers = pd.DataFrame(products_suppliers_table)
#     products_suppliers.set_index("_id", inplace=True)
#     return products_suppliers


# def getSuppliers():
#     suppliers_table = db["suppliers"].find({})
#     suppliers = pd.DataFrame(suppliers_table)
#     suppliers.set_index("_id", inplace=True)
#     return suppliers


# def getProducts():
#     products_table = db["products"].find({})
#     products = pd.DataFrame(products_table)
#     products.set_index("_id", inplace=True)
#     return products


#     # you need to get customers and agents collection and merge by agent Id
# ## Added these new functions

def getAgents():
    agents_table = db["agents"].find({})
    agents = pd.DataFrame(agents_table)
    # agents.set_index("_id", inplace=True)
    return agents


# def getCustomers():
#     customers_table = db["customers"].find({})
#     customers = pd.DataFrame(customers_table)
#     customers.set_index("_id", inplace=True)
#     return customers


def getPackages():
    packages_table = db["packages"].find({})
    packages = pd.DataFrame(packages_table)
    packages.set_index("_id", inplace=True)
    return packages