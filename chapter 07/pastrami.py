sandwich_orders = ["misto", "pastrami", "tuna", "pastrami", "bacon with eggs", "pastrami", "lettuce"]
finished_orders = []
print("We ran out of PASTRAMI\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    completed_order = sandwich_orders.pop()
    print(f"Your order [{completed_order.title()}] is ready.")
    finished_orders.append(completed_order)
print(f"\n{'-' *30}\n{'Orders':^30}\n{'-'*30}")
finished_orders.sort()
for i, order in enumerate(finished_orders):
    print(f"{i+1:<5}{order.title():>25}")
