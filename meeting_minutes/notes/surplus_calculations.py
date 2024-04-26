########################
# Surplus Calculation:
#
########################


def calculate_surplus(total_revenue, costs, reserve_allocation):
    surplus = total_revenue - costs
    allocated_reserves = surplus * reserve_allocation
    distributable_surplus = surplus - allocated_reserves
    return distributable_surplus

# Example usage
total_revenue = 5_000_000
costs = 750_000
reserve_allocation = 0.1

distributable_surplus = calculate_surplus(total_revenue, costs, reserve_allocation)
print(f"Distributable Surplus: {distributable_surplus}")

########################
# Membership Buy-in Fee Calculation:
#
########################



def calculate_buy_in_fee(total_assets, total_members, fee_percentage):
    buy_in_fee = (total_assets * fee_percentage) / total_members
    return buy_in_fee

# Example usage
total_assets = 100_000
total_members = 5
fee_percentage = 0.05

buy_in_fee = calculate_buy_in_fee(total_assets, total_members, fee_percentage)
print(f"Membership Buy-in Fee: {buy_in_fee}")


########################
# Patronage-based Dividend Distribution:
#
########################



def patronage_dividend_distribution(distributable_surplus, member_contributions):
    total_contributions = sum(member_contributions.values())
    member_dividends = {}
    for member, contribution in member_contributions.items():
        member_dividends[member] = distributable_surplus * (contribution / total_contributions)
    return member_dividends

# Example usage
distributable_surplus = 200_000
member_contributions = {
    "Member1": 5_000,
    "Member2": 7_500,
    "Member3": 10_000,
    "Member4": 6_000
}

member_dividends = patronage_dividend_distribution(distributable_surplus, member_contributions)
print("Patronage-based Dividend Distribution:")
for member, dividend in member_dividends.items():
    print(f"{member}: {dividend}")




########################
# Equal Dividend Distribution:
#
########################


def equal_dividend_distribution(distributable_surplus, total_members):
    dividend_per_member = distributable_surplus / total_members
    return dividend_per_member

# Example usage
distributable_surplus = 200_000
total_members = 5

dividend_per_member = equal_dividend_distribution(distributable_surplus, total_members)
print(f"Equal Dividend Distribution: {dividend_per_member} per member")


########################
# Combination of Patronage and Equal Distribution:
#
########################

def combined_dividend_distribution(distributable_surplus, member_contributions, patronage_percentage):
    patronage_surplus = distributable_surplus * patronage_percentage
    equal_surplus = distributable_surplus * (1 - patronage_percentage)
    total_contributions = sum(member_contributions.values())
    member_dividends = {}
    for member, contribution in member_contributions.items():
        patronage_dividend = patronage_surplus * (contribution / total_contributions)
        equal_dividend = equal_surplus / len(member_contributions)
        member_dividends[member] = patronage_dividend + equal_dividend
    return member_dividends

# Example usage
distributable_surplus = 200_000
member_contributions = {
    "Member1": 5_000,
    "Member2": 7_500,
    "Member3": 10_000,
    "Member4": 6_000
}
patronage_percentage = 0.7

member_dividends = combined_dividend_distribution(distributable_surplus, member_contributions, patronage_percentage)
print("Combined Dividend Distribution:")
for member, dividend in member_dividends.items():
    print(f"{member}: {dividend}")


########################
# Royalties-based Dividend Distribution:
#
########################

def royalties_dividend_distribution(distributable_surplus, member_royalties):
    total_royalties = sum(member_royalties.values())
    member_dividends = {}
    for member, royalty in member_royalties.items():
        member_dividends[member] = distributable_surplus * (royalty / total_royalties)
    return member_dividends

# Example usage
distributable_surplus = 200_000
member_royalties = {
    "Member1": 10_000,
    "Member2": 15_000,
    "Member3": 20_000,
    "Member4": 12_000
}
member_dividends = royalties_dividend_distribution(distributable_surplus, member_royalties)
print("Royalties-based Dividend Distribution:")
for member, dividend in member_dividends.items():
    print(f"{member}: {dividend}")

########################
# Combination of Royalties and Equal Distribution:
#
########################

def combined_dividend_distribution(distributable_surplus, member_royalties, royalties_percentage):
    royalties_surplus = distributable_surplus * royalties_percentage
    equal_surplus = distributable_surplus * (1 - royalties_percentage)
    total_royalties = sum(member_royalties.values())
    member_dividends = {}
    for member, royalty in member_royalties.items():
        royalties_dividend = royalties_surplus * (royalty / total_royalties)
        equal_dividend = equal_surplus / len(member_royalties)
        member_dividends[member] = royalties_dividend + equal_dividend
    return member_dividends

# Example usage
distributable_surplus = 200_000
member_royalties = {
    "Member1": 10_000,
    "Member2": 15_000,
    "Member3": 20_000,
    "Member4": 12_000
}
royalties_percentage = 0.7
member_dividends = combined_dividend_distribution(distributable_surplus, member_royalties, royalties_percentage)
print("Combined Dividend Distribution:")
for member, dividend in member_dividends.items():
    print(f"{member}: {dividend}")