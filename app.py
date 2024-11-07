from flask import Flask
from signalwire_swaig.core import SWAIG, SWAIGArgument, SWAIGArgumentItems
import logging, random
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

logging.getLogger('werkzeug').setLevel(logging.WARNING)

if os.environ.get('DEBUG'):
    print("Debug mode is enabled")
    debug_pin = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(100, 999)}"
    os.environ['WERKZEUG_DEBUG_PIN'] = debug_pin
    logging.getLogger('werkzeug').setLevel(logging.DEBUG)
    print(f"Debugger PIN: {debug_pin}")

# Initialize Flask app
app = Flask(__name__)

# Initialize SWAIG with the Flask app and basic authentication
swaig = SWAIG(
    app,
    auth=(os.getenv('HTTP_USERNAME'), os.getenv('HTTP_PASSWORD'))
)

# Mock data for menu items
menu_items = [
    {
        'sku': 'CFT001',
        'name': 'French Toast',
        'description': 'Classic French Toast served with maple syrup and fresh berries.',
        'price': 15.00,
        'category': 'Breakfast'
    },
    {
        'sku': 'AVT002',
        'name': 'Avocado Toast',
        'description': 'Multigrain bread topped with smashed avocado, poached egg, and a sprinkle of chili flakes.',
        'price': 12.00,
        'category': 'Breakfast'
    },
    {
        'sku': 'EGB003',
        'name': 'Egg Benedict',
        'description': 'Poached eggs on English muffins with hollandaise sauce.',
        'price': 14.00,
        'category': 'Breakfast'
    },
    {
        'sku': 'CSR004',
        'name': 'Caesar Salad',
        'description': 'Romaine lettuce with Caesar dressing, croutons, and parmesan.',
        'price': 10.00,
        'category': 'Lunch'
    },
    {
        'sku': 'CSG005',
        'name': 'Chicken Sandwich',
        'description': 'Grilled chicken sandwich with lettuce, tomato, and mayo.',
        'price': 11.00,
        'category': 'Lunch'
    },
    {
        'sku': 'CSS006',
        'name': 'Club Sandwich',
        'description': 'Triple-decker sandwich with turkey, bacon, lettuce, and tomato.',
        'price': 13.00,
        'category': 'Lunch'
    },
    {
        'sku': 'QRB007',
        'name': 'Quinoa Bowl',
        'description': 'Quinoa with roasted vegetables and a lemon tahini dressing.',
        'price': 12.00,
        'category': 'Lunch'
    },
    {
        'sku': 'CLB008',
        'name': 'Cheeseburger',
        'description': 'Beef patty with cheese, lettuce, tomato, and pickles.',
        'price': 14.00,
        'category': 'Dinner'
    },
    {
        'sku': 'GSM009',
        'name': 'Grilled Salmon',
        'description': 'Grilled salmon with a side of vegetables.',
        'price': 18.00,
        'category': 'Dinner'
    },
    {
        'sku': 'RBS010',
        'name': 'Ribeye Steak',
        'description': 'Juicy ribeye steak with mashed potatoes.',
        'price': 25.00,
        'category': 'Dinner'
    },
    {
        'sku': 'PSP011',
        'name': 'Pasta Primavera',
        'description': 'Pasta with seasonal vegetables and a light sauce.',
        'price': 16.00,
        'category': 'Dinner'
    },
    {
        'sku': 'COF012',
        'name': 'Coffee',
        'description': 'Freshly brewed coffee.',
        'price': 3.00,
        'category': 'Beverage'
    },
    {
        'sku': 'TEH013',
        'name': 'Herbal Tea',
        'description': 'A selection of herbal teas.',
        'price': 3.50,
        'category': 'Beverage'
    },
    {
        'sku': 'TEG014',
        'name': 'Green Tea',
        'description': 'Refreshing green tea.',
        'price': 3.50,
        'category': 'Beverage'
    },
    {
        'sku': 'TEB015',
        'name': 'Black Tea',
        'description': 'Classic black tea.',
        'price': 3.50,
        'category': 'Beverage'
    },
    {
        'sku': 'COK016',
        'name': 'Coke',
        'description': 'Chilled Coca-Cola.',
        'price': 2.00,
        'category': 'Beverage'
    },
    {
        'sku': 'PEP017',
        'name': 'Pepsi',
        'description': 'Chilled Pepsi.',
        'price': 2.00,
        'category': 'Beverage'
    },
    {
        'sku': 'DRP018',
        'name': 'Dr Pepper',
        'description': 'Chilled Dr Pepper.',
        'price': 2.00,
        'category': 'Beverage'
    },
    {
        'sku': 'RBR019',
        'name': 'Root Beer',
        'description': 'Chilled root beer.',
        'price': 2.00,
        'category': 'Beverage'
    },
    {
        'sku': 'RBM020',
        'name': 'Red Bull',
        'description': 'Energy drink.',
        'price': 3.00,
        'category': 'Beverage'
    },
    {
        'sku': 'RBM021',
        'name': 'Monster Energy',
        'description': 'Energy drink.',
        'price': 3.00,
        'category': 'Beverage'
    },
    {
        'sku': 'RBW022',
        'name': 'White Wine',
        'description': 'Glass of white wine.',
        'price': 8.00,
        'category': 'Beverage'
    },
    {
        'sku': 'RBW023',
        'name': 'Red Wine',
        'description': 'Glass of red wine.',
        'price': 8.00,
        'category': 'Beverage'
    },
        {
        'sku': 'RBS010-R',
        'name': 'Ribeye Steak - Rare',
        'description': '8 oz. steak cooked rare with mashed potatoes and seasonal vegetables.',
        'price': 30.00,
        'category': 'Dinner'
    },
    {
        'sku': 'RBS010-MR',
        'name': 'Ribeye Steak - Medium Rare',
        'description': '8 oz. steak cooked medium rare with mashed potatoes and seasonal vegetables.',
        'price': 30.00,
        'category': 'Dinner'
    },
    {
        'sku': 'RBS010-M',
        'name': 'Ribeye Steak - Medium',
        'description': '8 oz. steak cooked medium with mashed potatoes and seasonal vegetables.',
        'price': 30.00,
        'category': 'Dinner'
    },
    {
        'sku': 'RBS010-MW',
        'name': 'Ribeye Steak - Medium Well',
        'description': '8 oz. steak cooked medium well with mashed potatoes and seasonal vegetables.',
        'price': 30.00,
        'category': 'Dinner'
    },
    {
        'sku': 'RBS010-WD',
        'name': 'Ribeye Steak - Well Done',
        'description': '8 oz. steak cooked well done with mashed potatoes and seasonal vegetables.',
        'price': 30.00,
        'category': 'Dinner'
    }
]

# Initialize orders dictionary
orders = {}

completed_orders = []

# Helper function to find a menu item by SKU
def find_menu_item(sku: str):
    for item in menu_items:
        if item['sku'] == sku:
            logging.debug(f"Found item: {item}")
            return item
    return None

@swaig.endpoint(
    description="Adds items to the customer's order based on the provided SKUs and associates it with their room number.",
    room=SWAIGArgument(type="string", description="Customer's room number used as the order key.", required=True),
    skus=SWAIGArgument(type="array", description="List of SKU strings to add to the order.", required=True,
        items=SWAIGArgumentItems(
            type="string",
            enum=[item['sku'] for item in menu_items]
        )
    )
)
def add_items(room, skus):
    if room not in orders:
        orders[room] = {'items': [], 'status': 'pending'}
    for sku in skus:
        item = find_menu_item(sku)
        logging.debug(f"Item: {item}")
        if item:
            orders[room]['items'].append(item)
    return f"Items added successfully", {}

@swaig.endpoint(description="Removes items from the customer's order based on the provided SKUs and room number.",
                room=SWAIGArgument(type="string", description="Customer's room number used as the order key.", required=True),
                skus=SWAIGArgument(type="array", description="List of SKU strings to remove from the order.", required=True,
                    items=SWAIGArgumentItems(
                        type="string",
                        enum=[item['sku'] for item in menu_items]
                    )
                )
            )    
def delete_items(room, skus):
    if room in orders:
        orders[room]['items'] = [item for item in orders[room]['items'] if item['sku'] not in skus]
        return f"Items removed successfully", {}
    else:
        return f"Order not found for the given room number, Did you add the items first?", {}

@swaig.endpoint(description="Provides a summary of the customer's order and total price.",
                room=SWAIGArgument(type="string", description="Customer's room number used as the order key.", required=True))
def order_total(room):
    return f"Order total: {sum(item['price'] for item in orders[room]['items']):.2f}", {}

@swaig.endpoint(description="Reviews the customer's order and provides the items and their quantities.",
                room=SWAIGArgument(type="string", description="Customer's room number used as the order key.", required=True))
def review_order(room):
    if room in orders:
        from collections import defaultdict
        order_summary = defaultdict(int)

        for item in orders[room]['items']:
            order_summary[item['sku']] += 1

        summary_table = "SKU | Quantity\n"
        summary_table += "-" * 20 + "\n"
        for sku, quantity in order_summary.items():
            summary_table += f"{sku} | {quantity}\n"

        return summary_table.strip(), {}
    else:
        return f"Order not found for the given room number, Did you add the items first?", {}

@swaig.endpoint(description="Finalizes the customer's order and provides a confirmation.",
                room=SWAIGArgument(type="string", description="Customer's room number used as the order key.", required=True),
                notes=SWAIGArgument(type="string", description="Additional instructions for the order."))
def place_order(room, notes=""):
    if room in orders:
        orders[room]['status'] = 'placed'
        orders[room]['notes'] = notes
        completed_order = orders.pop(room)
        completed_order['room'] = room
        completed_orders.append(completed_order)
        return f"Order placed successfully", {}
    else:
        return f"Order not found for the given room number, Did you add the items first?", {}

@app.route('/swaig', methods=['GET'])
def display_detailed_orders():
    html_content = """
    <html>
    <head>
        <title>Detailed Orders Summary</title>
        <style>
            table {
                width: 80%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Pending Orders Summary</h2>
        <table>
            <tr>
                <th>Room Number</th>
                <th>SKU</th>
                <th>Item Name</th>
                <th>Description</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Total Price</th>
                <th>Status</th>
            </tr>
    """
    for room, order in orders.items():
        item_count = {}
        for item in order['items']:
            if item['sku'] in item_count:
                item_count[item['sku']]['quantity'] += 1
            else:
                item_count[item['sku']] = {
                    'name': item['name'],
                    'description': item['description'],
                    'price': item['price'],
                    'quantity': 1
                }
        
        total_price = 0
        for sku, details in item_count.items():
            item_total = details['price'] * details['quantity']
            total_price += item_total
            html_content += f"""
            <tr>
                <td>{room}</td>
                <td>{sku}</td>
                <td>{details['name']}</td>
                <td>{details['description']}</td>
                <td>${details['price']:.2f}</td>
                <td>{details['quantity']}</td>
                <td>${item_total:.2f}</td>
                <td>{order['status']}</td>
            </tr>
            """
        html_content += f"""
            <tr>
                <td colspan="6" style="text-align:right;"><strong>Total Price for room {room}:</strong></td>
                <td><strong>${total_price:.2f}</strong></td>
                <td></td>
            </tr>
        """
    
    html_content += """
        </table>
        <h2>Completed Orders Summary</h2>
        <table>
            <tr>
                <th>Room Number</th>
                <th>SKU</th>
                <th>Item Name</th>
                <th>Description</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Total Price</th>
                <th>Status</th>
            </tr>
    """
    for order in completed_orders:
        room = order.get('room', 'Unknown')
        item_count = {}
        for item in order['items']:
            if item['sku'] in item_count:
                item_count[item['sku']]['quantity'] += 1
            else:
                item_count[item['sku']] = {
                    'name': item['name'],
                    'description': item['description'],
                    'price': item['price'],
                    'quantity': 1
                }
        
        total_price = 0
        for sku, details in item_count.items():
            item_total = details['price'] * details['quantity']
            total_price += item_total
            html_content += f"""
            <tr>
                <td>{room}</td>
                <td>{sku}</td>
                <td>{details['name']}</td>
                <td>{details['description']}</td>
                <td>${details['price']:.2f}</td>
                <td>{details['quantity']}</td>
                <td>${item_total:.2f}</td>
                <td>{order['status']}</td>
            </tr>
            """
        html_content += f"""
            <tr>
                <td colspan="6" style="text-align:right;"><strong>Total Price for room {room}:</strong></td>
                <td><strong>${total_price:.2f}</strong></td>
                <td></td>
            </tr>
        """
    
    html_content += """
        </table>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) 