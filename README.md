# RoomieServe AI: Comprehensive Plan and Specification

## Table of Contents

1. [Introduction](#introduction)
2. [How RoomieServe AI Works](#how-roomieserve-ai-works)
3. [System Architecture](#system-architecture)
4. [Function Specifications](#function-specifications)
   - [add_items](#1-add_items)
   - [delete_items](#2-delete_items)
   - [order_total](#3-order_total)
   - [review_order](#4-review_order)
   - [place_order](#5-place_order)
5. [Data Structures](#data-structures)
   - [Menu Items](#menu-items)
   - [Orders](#orders)
6. [Mocked Python Functions](#mocked-python-functions)
7. [Example Interactions](#example-interactions)
8. [Conclusion](#conclusion)

---

## Introduction

**RoomieServe AI** is an innovative, AI-powered room service management tool designed to revolutionize the hospitality and healthcare industries. By leveraging natural language processing and AI technologies, RoomieServe AI streamlines the room service ordering process, enhancing guest and patient experiences through efficient, accurate, and user-friendly interactions.

This document provides a comprehensive plan and specification for RoomieServe AI, detailing its functionality, system architecture, data structures, mocked-up Python functions using mock data, and example interactions.

---

## How RoomieServe AI Works

RoomieServe AI operates as an AI Agent that interacts with users to handle room service orders through natural language conversations. The system is designed to:

- **Dynamic Menu Integration**: Automatically update menu offerings based on inventory and availability, ensuring guests have access to the most current items.
- **Order Management**: Efficiently add, remove, and modify items in a guest's order, with real-time updates on pricing and availability.
- **User Identification**: Use the guest's phone number as a unique identifier to track and manage their order throughout the interaction.
- **Human-Readable Interactions**: Provide clear, concise, and friendly responses to the user, enhancing the overall experience.
- **Mock Data Utilization**: For demonstration purposes, the system uses mock data and functions without the need for a database connection.

---

## System Architecture

The RoomieServe AI system consists of the following key components:

1. **AI Agent (LLM)**: The conversational interface that interacts with the user, understands their requests, and communicates accordingly.
2. **Functions/Tools**: Backend functions that handle order processing, including adding items, deleting items, calculating totals, and placing orders.
3. **Data Structures**: In-memory data representations of menu items and orders, using mock data for demonstration.
4. **Mocked Python Functions**: Implementations of the backend functions using mock data, simulating the behavior of a real system.

---

## Function Specifications

### 1. `add_items`

- **Description**: Adds items to the customer's order based on the provided SKUs and associates it with their room number.
- **Function Name**: `add_items`
- **Parameters**:

  ```json
  {
    "type": "object",
    "properties": {
      "room": {
        "type": "string",
        "description": "Customer's room number used as the order key."
      },
      "skus": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": [
            "CFT001", "AVT002", "EGB003", "CSR004", "CSG005", "CSS006",
            "QRB007", "CLB008", "GSM009", "RBS010", "PSP011", "COF012",
            "TEH013", "TEG014", "TEB015", "COK016", "PEP017", "DRP018",
            "RBR019", "RBM020", "RBM021", "RBW022", "RBW023"
          ]
        },
        "description": "List of SKU strings to add to the order."
      }
    },
    "required": ["room", "skus"]
  }
  ```

- **Returns**: A human-readable string confirming the items added to the order.

### 2. `delete_items`

- **Description**: Removes items from the customer's order based on the provided SKUs and room number.
- **Function Name**: `delete_items`
- **Parameters**:

  ```json
  {
    "type": "object",
    "properties": {
      "room": {
        "type": "string",
        "description": "Customer's room number used as the order key."
      },
      "skus": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": []  // Populated dynamically based on items in the customer's order
        },
        "description": "List of SKU strings to remove from the order."
      }
    },
    "required": ["room", "skus"]
  }
  ```

- **Returns**: A human-readable string confirming the items removed from the order.

### 3. `order_total`

- **Description**: Provides a summary of the customer's order, including item details and the total price, identified by the customer's room number.
- **Function Name**: `order_total`
- **Parameters**:

  ```json
  {
    "type": "object",
    "properties": {
      "room": {
        "type": "string",
        "description": "Customer's room number used as the order key."
      }
    },
    "required": ["room"]
  }
  ```

- **Returns**: A human-readable string summarizing the order and total price.

### 4. `review_order`

- **Description**: Provides a detailed review of the customer's current order, including item names, quantities, and individual prices, identified by the customer's room number.
- **Function Name**: `review_order`
- **Parameters**:

  ```json
  {
    "type": "object",
    "properties": {
      "room": {
        "type": "string",
        "description": "Customer's room number used as the order key."
      }
    },
    "required": ["room"]
  }
  ```

- **Returns**: A human-readable string detailing the current items in the order, their quantities, and individual prices.

### 5. `place_order`

- **Description**: Finalizes the customer's order, adds any notes, and confirms the order, identified by the customer's room number.
- **Function Name**: `place_order`
- **Parameters**:

  ```json
  {
    "type": "object",
    "properties": {
      "room": {
        "type": "string",
        "description": "Customer's room number used as the order key."
      },
      "notes": {
        "type": "string",
        "description": "Any additional notes or instructions for the order."
      }
    },
    "required": ["room"]
  }
  ```

- **Returns**: A human-readable string confirming that the order has been placed.

---

## Data Structures

### Menu Items

A list of dictionaries representing the menu items, including details such as SKU, name, description, price, and category.

```python
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
    # ... Additional items as per the menu
]
```

### Orders

A dictionary to store orders, using the customer's room number as the key.

```python
orders = {
    # Example:
    '101': {
        'items': {
            'CFT001': {
                'item': menu_items[0],
                'quantity': 1
            }
        },
        'total_price': 15.00,
        'notes': ''
    }
}
```

---

## Mocked Python Functions

Below are the mocked-up Python functions that simulate the backend operations using the mock data.

```python
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
        orders[room] = [item for item in orders[room] if item['sku'] not in skus]
        return f"Items removed successfully", {}
    else:
        return f"Order not found for the given room number", {}

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
        return f"Order not found for the given room number", {}

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
        return f"Order not found for the given room number", {}
```

---

## Example Interactions

### Interaction 1: Adding Items

**User**: "I would like to order French Toast and a Coffee. My room number is 101."

**AI Agent**:

- **Function Call**:

  ```json
  {
    "function": "add_items",
    "arguments": {
      "room": "101",
      "skus": ["CFT001", "COF012"]
    }
  }
  ```

- **Function Response**: "Added to your order: French Toast, Coffee."

- **Assistant Response**: "French Toast and Coffee have been added to your order."

### Interaction 2: Deleting Items

**User**: "Please remove the Coffee from my order."

**AI Agent**:

- **Function Call**:

  ```json
  {
    "function": "delete_items",
    "arguments": {
      "room": "101",
      "skus": ["COF012"]
    }
  }
  ```

- **Function Response**: "Removed from your order: Coffee."

- **Assistant Response**: "Coffee has been removed from your order."

### Interaction 3: Viewing Order Total

**User**: "What is the total for my order?"

**AI Agent**:

- **Function Call**:

  ```json
  {
    "function": "order_total",
    "arguments": {
      "room": "101"
    }
  }
  ```

- **Function Response**: "Your order: 1 x French Toast ($15.00). Total price: $15.00."

- **Assistant Response**: "Your order includes 1 French Toast. The total price is $15.00."

### Interaction 4: Placing an Order

**User**: "I'd like to place the order. Please deliver it to room 101."

**AI Agent**:

- **Function Call**:

  ```json
  {
    "function": "place_order",
    "arguments": {
      "room": "101",
      "notes": "Please deliver to room 101."
    }
  }
  ```

- **Function Response**: "Your order has been placed. Total: $15.00. Please deliver to room 101."

- **Assistant Response**: "Your order has been placed and will be delivered to room 101 shortly. The total is $15.00."

---

## Conclusion

The RoomieServe AI system is designed to enhance the room service experience by providing a seamless, AI-driven ordering process. By utilizing the customer's room number as a unique identifier, the system efficiently manages orders, ensuring accuracy and personalized service.

This comprehensive plan outlines the key components, function specifications, data structures, and example interactions necessary to implement RoomieServe AI using mock data. The mocked-up Python functions demonstrate how the backend operates without the need for a database, making it suitable for demonstrations and initial development phases.

By following this plan, developers and stakeholders can understand the system's architecture and functionality, paving the way for further development and integration into real-world applications.

---

## Château AI-Luxe Deployment

RoomieServe AI has been successfully deployed at Château AI-Luxe, showcasing its capabilities in a real-world hospitality environment. This deployment demonstrates the system's effectiveness in enhancing guest experiences through efficient and personalized room service management.

---

## Key Highlights

- **Dynamic Menu Integration**: Automatic updates to menu offerings based on mock data.
- **Efficient Order Management**: Quick addition and removal of items using SKUs.
- **User-Friendly Interactions**: Clear, human-readable responses enhance user experience.
- **Scalable Architecture**: The system can be adapted to include database integration and expanded functionalities as needed.

---

## Next Steps

- **Database Integration**: Transition from mock data to actual database connections for real-world applications.
- **AI Agent Enhancement**: Improve the natural language understanding capabilities of the AI Agent for more complex interactions.
- **Feature Expansion**: Include additional functionalities such as order tracking, payment processing, and feedback collection.

---

## Contact Information

For further information or inquiries about RoomieServe AI, please contact:

- **Email**: [sales@signalwire.com](mailto:sales@signalwire.com)
- **Phone**: [+16503820000](tel:+16503820000)

---

## Disclaimer

This document is intended for informational purposes to outline the plan and specifications of RoomieServe AI using mock data for demonstration. The functions and data structures provided are for illustrative purposes and may require adjustments for deployment in a production environment.

---

## Appendices

### Full OpenAI Tool Specification

```json
{
  "functions": [
    {
      "name": "add_items",
      "description": "Adds items to the customer's order based on the provided SKUs and associates it with their room number.",
      "parameters": {
        "type": "object",
        "properties": {
          "room": {
            "type": "string",
            "description": "Customer's room number used as the order key."
          },
          "skus": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "CFT001", "AVT002", "EGB003", "CSR004", "CSG005", "CSS006",
                "QRB007", "CLB008", "GSM009", "RBS010", "PSP011", "COF012",
                "TEH013", "TEG014", "TEB015", "COK016", "PEP017", "DRP018",
                "RBR019", "RBM020", "RBM021", "RBW022", "RBW023"
              ]
            },
            "description": "List of SKU strings to add to the order."
          }
        },
        "required": ["room", "skus"]
      }
    },
    {
      "name": "delete_items",
      "description": "Removes items from the customer's order based on the provided SKUs and room number.",
      "parameters": {
        "type": "object",
        "properties": {
          "room": {
            "type": "string",
            "description": "Customer's room number used as the order key."
          },
          "skus": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": []  // To be dynamically populated
            },
            "description": "List of SKU strings to remove from the order."
          }
        },
        "required": ["room", "skus"]
      }
    },
    {
      "name": "order_total",
      "description": "Provides a summary of the customer's order and total price.",
      "parameters": {
        "type": "object",
        "properties": {
          "room": {
            "type": "string",
            "description": "Customer's room number used as the order key."
          }
        },
        "required": ["room"]
      }
    },
    {
      "name": "place_order",
      "description": "Finalizes the customer's order and provides a confirmation.",
      "parameters": {
        "type": "object",
        "properties": {
          "room": {
            "type": "string",
            "description": "Customer's room number used as the order key."
          },
          "notes": {
            "type": "string",
            "description": "Additional instructions for the order."
          }
        },
        "required": ["room"]
      }
    }
  ]
}
```

---
