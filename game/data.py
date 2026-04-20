# data.py

# Currency
CURRENCY = "SC"

# Fuel conversion
ZJ_PER_AU = 23

# Regions and travel distances
regions = {
    "Nyx": {
        "fuel_price": 0.15,
        "routes": {
            "Barak": 3,
            "Azrael": 4,
            "Abaddon": 6
        }
    },
    "Barak": {
        "fuel_price": 0.18,
        "routes": {
            "Nyx": 3,
            "Azrael": 5,
            "Abaddon": 8
        }
    },
    "Azrael": {
        "fuel_price": 0.12,
        "routes": {
            "Nyx": 4,
            "Barak": 5,
            "Abaddon": 3
        }
    },
    "Abaddon": {
        "fuel_price": 0.22,
        "routes": {
            "Nyx": 6,
            "Barak": 8,
            "Azrael": 3
        }
    }
}

# Item prices per region
items = {
    "Water": {
        "Nyx": 10,
        "Barak": 14,
        "Azrael": 8,
        "Abaddon": 16
    },
    "Food Rations": {
        "Nyx": 20,
        "Barak": 18,
        "Azrael": 25,
        "Abaddon": 30
    },
    "Medical Supplies": {
        "Nyx": 50,
        "Barak": 65,
        "Azrael": 55,
        "Abaddon": 80
    },
    "Electronics": {
        "Nyx": 120,
        "Barak": 100,
        "Azrael": 140,
        "Abaddon": 170
    },
    "Rare Minerals": {
        "Nyx": 200,
        "Barak": 260,
        "Azrael": 180,
        "Abaddon": 300
    }
}