sandwich_orders = ["misto", "tuna", "bacon with eggs", "lettuce"]
finished_orders = []
while sandwich_orders:
    completed_order = sandwich_orders.pop()
    print(f"Your order [{completed_order.title()}] is finished.")
    finished_orders.append(completed_order)
print(f"\n{'-'*30}\n{'Orders':^30}\n{'-'*30}")
for i, order in enumerate(finished_orders):
    print(f"{i+1:<5}{order:>25}")
