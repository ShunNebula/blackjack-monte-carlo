from deck import Deck
from hand import Hand

def strategy(hand_value: int) -> bool:
    """
    Возвращает True, если нужно брать карту (Hit).
    Возвращает False, если нужно остановиться (Stand).
    Стратегия: Брать, пока меньше 17.
    """
    return hand_value < 17

def play_game(strategy) -> int:
    """
    Симулирует одну партию.
    Никаких print()! Никаких input()!
    Возвращает:
     1 - победа игрока
     0 - ничья
    -1 - поражение
    """
    # 1. Создать колоду, перемешать
    deck = Deck()
    deck.shuffle()

    # 2. Раздать карты
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    initial_sum = player.get_value()

    # 3. Цикл хода игрока:
    #    Вместо input() вызываем strategy_func(player.get_value())
    while player.get_value() < 21:
        choice = strategy(player.get_value())
        if not choice:
            break
        new_card = deck.deal_card()
        player.add_card(new_card)
        
    did_bust = player.get_value() > 21

    # 4. Если перебор -> return -1
    if did_bust:
        return {
            "start_sum": initial_sum,
            "did_bust": True,
            "result": -1
        }

    # 5. Ход дилера
    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())

    # 6. Сравнение -> return 1, 0 или -1
    p_score = player.get_value()
    d_score = dealer.get_value()

    if d_score > 21: result = 1
    elif p_score > d_score: result = 1
    elif p_score == d_score: result = 0
    else: result = -1

    return {
        "start_sum": initial_sum,
        "did_bust": False,
        "result":result
    }

# if __name__ == "__main__":
#     N_GAMES = 10000
#     results = {1: 0, 0: 0, -1: 0}

#     print(f"Запуск симуляции {N_GAMES} игр ...")

#     for _ in range(N_GAMES):
#         res = play_game(strategy)
#         results[res] += 1
    
#     win_rate = (results[1] / N_GAMES) * 100
#     loss_rate = (results[-1] / N_GAMES) * 100
#     draw_rate = (results[0] / N_GAMES) * 100

#     print(f"--- Результаты ---")
#     print(f"Побед: {results[1]} ({win_rate:.2f}%)")
#     print(f"Поражений: {results[-1]} ({loss_rate:.2f}%)")
#     print(f"Ничьих: {results[0]} ({draw_rate:.2f}%)")
    
#     print(f"Преимущество казино: {loss_rate - win_rate:.2f}%")