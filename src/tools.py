import random
import json


# Looping tool(s)
# =================================================
LOOPING_TOOLS = [
    {
        "type": "function",
        "name": "done",
        "description": "Call this when the request is fully handled.",
        "parameters": {
            "type": "object",
            "properties": {
                "done": {
                    "type": "boolean",
                    "description": "True if the request has been fully handled; false otherwise.",
                    "default": False,
                }
            },
            "required": ["done"],
        },
    }
]


# Decorator to register tools
# =================================================
tools_available = {}


def tool(func):
    """Decorator to mark a function as a tool.

    Args:
        func: The function to mark as a tool
    """
    tools_available[func.__name__] = func
    return func


# Tools
# =================================================
@tool
def add(a: float, b: float) -> float:
    """A function that adds two numbers

    Args:
        a: The first number to add
        b: The second number to add
    """
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """A function that subtracts two numbers

    Args:
        a: The first number to subtract
        b: The second number to subtract
    """
    return a - b


@tool
def multiply(a: float, b: float) -> float:
    """A function that multiplies two numbers

    Args:
        a: The first number to multiply
        b: The second number to multiply
    """
    return a * b


@tool
def divide(a: float, b: float) -> float:
    """A function that divides two numbers

    Args:
        a: The first number to divide
        b: The second number to divide
    """
    return a / b


@tool
def fetch_office_locations():
    """Fetch a list of available office locations for Webstep"""
    return ["oslo", "bergen", "stavanger", "trondheim", "kristiansand", "haugesund"]


@tool
def fetch_address_and_number_of_employees(office: str) -> tuple[str, int]:
    """Fetch the number of employees at a given office
    Args:
        office: The office to fetch the number_of_employees
    """
    number_of_employees = {
        "bergen": {
            "address": "Damsgårdsveien 14, 5058 Bergen",
            "number_of_employees": 91,
        },
        "oslo": {
            "address": "Universitetsgata 2, 0164 Oslo",
            "number_of_employees": 185,
        },
        "stavanger": {
            "address": "Verksgata 1 A, 4013 Stavanger",
            "number_of_employees": 51,
        },
        "trondheim": {
            "address": "Kongens gate 16, 7011 Trondheim",
            "number_of_employees": 53,
        },
        "kristiansand": {
            "address": "Skippergata 19, 4611 Kristiansand S",
            "number_of_employees": 21,
        },
    }
    if office not in number_of_employees:
        return ("unknown", 0)
    return number_of_employees[office]


@tool
def robber_language_b(word: str) -> str:
    """Convert a word to 'robber language' by inserting 'o' between consonants."""
    consonants = "bcdfghjklmnpqrstvwxyz"
    return "".join(
        [char + "o" + char if char.lower() in consonants else char for char in word]
    )


@tool
def robber_language_a(word: str) -> str:
    """Returns a random string of the input word"""
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)


# Tools Schema for OpenAI API
# =================================================
tools_description = [
    {
        "type": "function",
        "name": "add",
        "description": "A function that adds two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "The first number to add",
                },
                "b": {
                    "type": "number",
                    "description": "The second number to add",
                },
            },
            "required": ["a", "b"],
        },
    },
    {
        "type": "function",
        "name": "subtract",
        "description": "A function that subtracts two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "The first number to subtract",
                },
                "b": {
                    "type": "number",
                    "description": "The second number to subtract",
                },
            },
            "required": ["a", "b"],
        },
    },
    {
        "type": "function",
        "name": "multiply",
        "description": "A function that multiplies two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "The first number to multiply",
                },
                "b": {
                    "type": "number",
                    "description": "The second number to multiply",
                },
            },
            "required": ["a", "b"],
        },
    },
    {
        "type": "function",
        "name": "divide",
        "description": "A function that divides two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "The first number to divide",
                },
                "b": {
                    "type": "number",
                    "description": "The second number to divide",
                },
            },
            "required": ["a", "b"],
        },
    },
    {
        "type": "function",
        "name": "fetch_office_locations",
        "description": "Function fetching a list of office locations for Webstep",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
    {
        "type": "function",
        "name": "fetch_address_and_number_of_employees",
        "description": "Function witch fetches address and number of employees of a Webstep office.",
        "parameters": {
            "type": "object",
            "properties": {
                "office": {
                    "type": "string",
                    "description": "The office to fetch the weather for",
                },
            },
            "required": ["office"],
        },
    },
    {
        "type": "function",
        "name": "robber_language_b",
        "description": "Encrypts a word to 'robber language'.",
        "parameters": {
            "type": "object",
            "properties": {
                "word": {
                    "type": "string",
                    "description": "The word to convert to robber language",
                },
            },
            "required": ["word"],
        },
    },
    {
        "type": "function",
        "name": "robber_language_a",
        "description": "Encodes a word to 'robber language'.",
        "parameters": {
            "type": "object",
            "properties": {
                "word": {
                    "type": "string",
                    "description": "The word to convert to robber language",
                },
            },
            "required": ["word"],
        },
    },
]
