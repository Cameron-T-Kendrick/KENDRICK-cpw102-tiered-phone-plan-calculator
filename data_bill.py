"""Extend your phone bill lab with premium membership and tiered pricing."""


def exceeds_data_limit(data_used):
    return data_used > 10


def get_overage_rate(data_used, has_premium):
    """Return the numeric rate for every overage GB.

    data_used is total usage in GB; has_premium is a Boolean.

    Total data used           Regular    Premium
    10 GB or less                0          0
    More than 10, up to 20       2          1
    More than 20                3          2

    Use if-elif-else for tiers and a nested decision for membership.
    Return the rate rather than printing it.
    """ 
    if data_used <= 10:
        return 0
    elif data_used <= 20:
        if has_premium:
            return 1
        else:
            return 2
    else:
        if has_premium:
            return 2
        else:
            return 3


    
def main():
   

    """Add the premium input and convert it to a Boolean.
    Call exceeds_data_limit() in a decision.
    Use get_overage_rate() instead of the fixed $2 rate.
    Add the premium recommendation described in the README.
    """
    user_gb = float(input("Enter GB used: "))
    user_membership_cost = float(input("Enter Base Plane cost: "))
    user_plan = input("Do you have premium membership? (yes or no): ")

    membership = user_membership_cost
    data_used = user_gb
    has_premium = user_plan.strip().lower() == "yes"


    rate = get_overage_rate(data_used, has_premium)

    overage_gb = max(0, data_used - 10)
    overage_cost = overage_gb * rate
    total_bill = membership + overage_cost

    if not has_premium:
           if not exceeds_data_limit(data_used):
               print("You are within your data limit.")
               print(f"Total Bill: ${membership}") 
           elif overage_gb <= 5:
               print(f"You are {overage_gb} GB over your limit")
               print("Moderate Extra GB Usage")
               print(f"Overage rate: ${rate}") 
               print(f"Overage cost: ${overage_cost}")
               print("Consider premium membership to reduce your overage rate.")
               print(f"Total Bill: ${total_bill}")
           else:
               print(f"You are {overage_gb} GB over your limit")
               print("High Extra GB Usage")
               print(f"Overage rate: ${rate}") 
               print(f"Overage cost: ${overage_cost}")
               print("Consider premium membership to reduce your overage rate.")
               print(f"Total Bill: ${total_bill}")
   
    else:
   
           if not exceeds_data_limit(data_used):
               print("You are within your data limit.")
               print(f"Total Bill: ${membership}") 
           elif overage_gb <= 5:
               print(f"You are {overage_gb} GB over your limit")
               print("Moderate Extra GB Usage")
               print(f"Overage rate: ${rate}") 
               print(f"Overage cost: ${overage_cost}")
               print(f"Total Bill: ${total_bill}")
           else:
               print(f"You are {overage_gb} GB over your limit")
               print("High Extra GB Usage")
               print(f"Overage rate: ${rate}") 
               print(f"Overage cost: ${overage_cost}")
               print(f"Total Bill: ${total_bill}")
   


# Keep this guard: importing functions for tests must not prompt for input.
if __name__ == "__main__":
    main()