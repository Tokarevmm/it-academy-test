def transaction_success(deal_success, current_pos):

    num_success = len([i for i in deal_success if i > 0])

    total_transactions = len(deal_success) + 1
    success_probability = (num_success / total_transactions) * 100

    net_income = sum(deal_success) + current_pos - 1000

    roi = (net_income / 1000) * 100

    print(f"вероятность успеха сделки: {success_probability:.2f}%")
    print(f"Чистый доход инвестора: {net_income:.2f} единиц")
    print(f"ROI: {roi:.2f}%")

deal_success = [-107, -521, -107, -126, 352, -58, 221, 193, -38, 454, -12, -211, 129, 85, 342]
current_pos = 500

transaction_success(deal_success, current_pos)
