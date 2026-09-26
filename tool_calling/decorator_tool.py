from langchain_core.tools import tool

@tool
def get_item_price(item_name: str) -> str:
    """
    Retrieve the current price of an item from the internal database.
    Use this when the user asks for the cost of specific product.
    """
    prices = { "apple": "$1.50", "laptop": "$999.00"}
    return prices.get(item_name.lower(), "Item not found")

print(f"Name: {get_item_price.name}")
print(f"Description: {get_item_price.description}")
print(f"Args: {get_item_price.args}")

print(get_item_price.invoke("laptop"))