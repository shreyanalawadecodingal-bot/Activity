# Dictionary mapping countries to codes
country_codes = {
    "United States": "US",
    "India": "IN",
    "Canada": "CA",
    "Australia": "AU",
    "United Kingdom": "UK"
}

# Example: Get country code
country_name = input("Enter country name: ")

code = country_codes.get(country_name, "Country not found")
print(f"Country Code for {country_name}: {code}")
