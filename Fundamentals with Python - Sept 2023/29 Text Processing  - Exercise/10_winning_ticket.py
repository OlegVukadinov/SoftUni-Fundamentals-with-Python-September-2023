def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uniterrupted_match_lenght in range(10, 5, -1):
            winning_symbol_repetition = match_symbol * uniterrupted_match_lenght
            if winning_symbol_repetition in left_part and winning_symbol_repetition in right_part:
                if uniterrupted_match_lenght == 10:
                    return f'ticket "{ticket}" - {uniterrupted_match_lenght}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uniterrupted_match_lenght}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))



