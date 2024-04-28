class UnknownPaymentMethodException(Exception):
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def __str__(self):
        return "尚不支持的还款方式:{}".format(self.payment_method)


def k_term_factory(payment_method):
    if payment_method == "等额本息":
        return get_k_term_equal_loan_payment
    elif payment_method == "等额本金":
        return get_k_term_equal_principal_payment
    else:
        raise UnknownPaymentMethodException(payment_method)


def get_k_term_equal_loan_payment(principal, monthly_rate, periods, k):
    p = principal * (monthly_rate * (1 + monthly_rate) ** (k - 1)) / ((1 + monthly_rate) ** periods - 1)
    i = principal * (monthly_rate * ((1 + monthly_rate) ** periods - (1 + monthly_rate) ** (k - 1))) / ((1 + monthly_rate) ** periods - 1)
    return round(round(p, 2) + round(i, 2), 2), round(p, 2), round(i, 2)


def get_k_term_equal_principal_payment(principal, monthly_rate, periods, k):
    p = principal / periods
    i = (principal - (k - 1) * principal / periods) * monthly_rate
    return round(round(p, 2) + round(i, 2), 2), round(p, 2), round(i, 2)


def get_repay_plan(principal, monthly_rate, periods, payment_method="等额本息"):
    term_list = []
    get_k_term = k_term_factory(payment_method)
    for k in range(1, periods + 1):
        term_list.append(get_k_term(principal, monthly_rate, periods, k))
    return term_list


def get_duration(principal_list):
    p_cum = 0
    p = 0
    N = len(principal_list)
    for principal in principal_list[::-1]:
        p_cum += principal * N
        p += principal
        N -= 1
    return p_cum / p


def profit(price, share, tax, lost, ftp):
    profit = price * (1 - share) / tax - lost - ftp
    print("定价:{},分润比例:{},税率:{},年损:{},ftp:{},利润:{}".format(price, share, tax, lost, ftp, round(profit, 4)))
    return round(profit, 4)


def lost(price, share_pct, tax, profit, ftp):
    lost = price * (1 - share_pct) / tax - profit - ftp
    print("定价:{},分润比例:{},税率:{},年损:{},ftp:{},利润:{}".format(price, share_pct, tax, round(lost, 4), ftp, profit))
    return round(lost, 4)
