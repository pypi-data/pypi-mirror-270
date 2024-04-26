from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_book_currency_quote = publicGetBookCurrencyQuote = Entry('book/{currency}/{quote}', 'public', 'GET', {'cost': 1})
    public_get_chart_week = publicGetChartWeek = Entry('chart/week', 'public', 'GET', {'cost': 1})
    public_get_chart_week_currency_quote = publicGetChartWeekCurrencyQuote = Entry('chart/week/{currency}/{quote}', 'public', 'GET', {'cost': 1})
    public_get_currency = publicGetCurrency = Entry('currency', 'public', 'GET', {'cost': 1})
    public_get_currency_available = publicGetCurrencyAvailable = Entry('currency/available', 'public', 'GET', {'cost': 1})
    public_get_currency_quotes = publicGetCurrencyQuotes = Entry('currency/quotes', 'public', 'GET', {'cost': 1})
    public_get_currency_currency = publicGetCurrencyCurrency = Entry('currency/{currency}', 'public', 'GET', {'cost': 1})
    public_get_pair = publicGetPair = Entry('pair', 'public', 'GET', {'cost': 1})
    public_get_pair_available = publicGetPairAvailable = Entry('pair/available', 'public', 'GET', {'cost': 1})
    public_get_ticker = publicGetTicker = Entry('ticker', 'public', 'GET', {'cost': 1})
    public_get_ticker_base_quote = publicGetTickerBaseQuote = Entry('ticker/{base}/{quote}', 'public', 'GET', {'cost': 1})
    public_get_time = publicGetTime = Entry('time', 'public', 'GET', {'cost': 1})
    public_get_trade_history_currency_quote = publicGetTradeHistoryCurrencyQuote = Entry('trade/history/{currency}/{quote}', 'public', 'GET', {'cost': 1})
    public_get_trade_fee_currency_quote = publicGetTradeFeeCurrencyQuote = Entry('trade/fee/{currency}/{quote}', 'public', 'GET', {'cost': 1})
    public_get_trade_feelevels = publicGetTradeFeeLevels = Entry('trade/feeLevels', 'public', 'GET', {'cost': 1})
    public_get_transaction_bindings = publicGetTransactionBindings = Entry('transaction/bindings', 'public', 'GET', {'cost': 1})
    private_get_auth_account = privateGetAuthAccount = Entry('auth/account', 'private', 'GET', {'cost': 1})
    private_get_auth_account_currency_currency_type = privateGetAuthAccountCurrencyCurrencyType = Entry('auth/account/currency/{currency}/{type}', 'private', 'GET', {'cost': 1})
    private_get_auth_order = privateGetAuthOrder = Entry('auth/order', 'private', 'GET', {'cost': 1})
    private_get_auth_order_getorder_id = privateGetAuthOrderGetOrderId = Entry('auth/order/getOrder/{id}', 'private', 'GET', {'cost': 1})
    private_get_auth_order_pair_currency_quote = privateGetAuthOrderPairCurrencyQuote = Entry('auth/order/pair/{currency}/{quote}', 'private', 'GET', {'cost': 1})
    private_get_auth_order_pair_currency_quote_active = privateGetAuthOrderPairCurrencyQuoteActive = Entry('auth/order/pair/{currency}/{quote}/active', 'private', 'GET', {'cost': 1})
    private_get_auth_stoporder = privateGetAuthStopOrder = Entry('auth/stopOrder', 'private', 'GET', {'cost': 1})
    private_get_auth_stoporder_getorder_id = privateGetAuthStopOrderGetOrderId = Entry('auth/stopOrder/getOrder/{id}', 'private', 'GET', {'cost': 1})
    private_get_auth_stoporder_pair_currency_quote = privateGetAuthStopOrderPairCurrencyQuote = Entry('auth/stopOrder/pair/{currency}/{quote}', 'private', 'GET', {'cost': 1})
    private_get_auth_stoporder_pair_currency_quote_active = privateGetAuthStopOrderPairCurrencyQuoteActive = Entry('auth/stopOrder/pair/{currency}/{quote}/active', 'private', 'GET', {'cost': 1})
    private_get_auth_trade = privateGetAuthTrade = Entry('auth/trade', 'private', 'GET', {'cost': 1})
    private_get_auth_trade_pair_currency_quote = privateGetAuthTradePairCurrencyQuote = Entry('auth/trade/pair/{currency}/{quote}', 'private', 'GET', {'cost': 1})
    private_get_auth_trade_fee_currency_quote = privateGetAuthTradeFeeCurrencyQuote = Entry('auth/trade/fee/{currency}/{quote}', 'private', 'GET', {'cost': 1})
    private_get_auth_transaction = privateGetAuthTransaction = Entry('auth/transaction', 'private', 'GET', {'cost': 1})
    private_get_auth_transaction_bindings = privateGetAuthTransactionBindings = Entry('auth/transaction/bindings', 'private', 'GET', {'cost': 1})
    private_get_auth_transaction_bindings_currency = privateGetAuthTransactionBindingsCurrency = Entry('auth/transaction/bindings/{currency}', 'private', 'GET', {'cost': 1})
    private_get_auth_transaction_id = privateGetAuthTransactionId = Entry('auth/transaction/{id}', 'private', 'GET', {'cost': 1})
    private_get_auth_transfer = privateGetAuthTransfer = Entry('auth/transfer', 'private', 'GET', {'cost': 1})
    private_post_auth_order_cancel = privatePostAuthOrderCancel = Entry('auth/order/cancel', 'private', 'POST', {'cost': 1})
    private_post_auth_order_cancelall = privatePostAuthOrderCancelAll = Entry('auth/order/cancelAll', 'private', 'POST', {'cost': 1})
    private_post_auth_order_cancelall_currency_quote = privatePostAuthOrderCancelAllCurrencyQuote = Entry('auth/order/cancelAll/{currency}/{quote}', 'private', 'POST', {'cost': 1})
    private_post_auth_order_place = privatePostAuthOrderPlace = Entry('auth/order/place', 'private', 'POST', {'cost': 1})
    private_post_auth_spot_deposit = privatePostAuthSpotDeposit = Entry('auth/spot/deposit', 'private', 'POST', {'cost': 1})
    private_post_auth_spot_withdraw = privatePostAuthSpotWithdraw = Entry('auth/spot/withdraw', 'private', 'POST', {'cost': 1})
    private_post_auth_stoporder_cancel = privatePostAuthStopOrderCancel = Entry('auth/stopOrder/cancel', 'private', 'POST', {'cost': 1})
    private_post_auth_stoporder_cancelall = privatePostAuthStopOrderCancelAll = Entry('auth/stopOrder/cancelAll', 'private', 'POST', {'cost': 1})
    private_post_auth_stoporder_cancelall_currency_quote = privatePostAuthStopOrderCancelAllCurrencyQuote = Entry('auth/stopOrder/cancelAll/{currency}/{quote}', 'private', 'POST', {'cost': 1})
    private_post_auth_stoporder_place = privatePostAuthStopOrderPlace = Entry('auth/stopOrder/place', 'private', 'POST', {'cost': 1})
    private_post_auth_transaction_depositaddress = privatePostAuthTransactionDepositAddress = Entry('auth/transaction/depositAddress', 'private', 'POST', {'cost': 1})
    private_post_auth_transaction_withdraw = privatePostAuthTransactionWithdraw = Entry('auth/transaction/withdraw', 'private', 'POST', {'cost': 1})
    private_post_auth_transaction_withdraw_cancel = privatePostAuthTransactionWithdrawCancel = Entry('auth/transaction/withdraw/cancel', 'private', 'POST', {'cost': 1})
    private_post_auth_transaction_withdraw_confirm = privatePostAuthTransactionWithdrawConfirm = Entry('auth/transaction/withdraw/confirm', 'private', 'POST', {'cost': 1})
    private_post_auth_transaction_withdraw_resendcode = privatePostAuthTransactionWithdrawResendCode = Entry('auth/transaction/withdraw/resendCode', 'private', 'POST', {'cost': 1})
    private_post_auth_transfer_email = privatePostAuthTransferEmail = Entry('auth/transfer/email', 'private', 'POST', {'cost': 1})
    private_post_auth_transfer_id = privatePostAuthTransferId = Entry('auth/transfer/id', 'private', 'POST', {'cost': 1})
    private_post_auth_transfer_phone = privatePostAuthTransferPhone = Entry('auth/transfer/phone', 'private', 'POST', {'cost': 1})
