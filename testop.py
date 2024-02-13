def distribute_shirts_evenly(shirt_count, bag_count):
    # Calculate the base number of shirts per bag
    base_shirts_per_bag = shirt_count // bag_count
    # Calculate the number of bags that will have the base number of shirts
    bags_with_base_shirts = shirt_count % bag_count
    # Calculate the number of bags that will have one additional shirt
    bags_with_extra_shirt = bag_count - bags_with_base_shirts

    # Distribute shirts evenly across bags
    bags = [base_shirts_per_bag] * bags_with_base_shirts + [base_shirts_per_bag + 1] * bags_with_extra_shirt

    # Calculate deviation
    deviation = max(bags) - min(bags)

    return bags, deviation

# Test cases
print(distribute_shirts_evenly(500, 10))
print(distribute_shirts_evenly(101, 10))
print(distribute_shirts_evenly(99, 10))
