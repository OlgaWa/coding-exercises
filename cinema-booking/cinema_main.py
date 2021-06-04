from classes import User, Card, Seat


name = input("What is your name? ")
seat_id = input("Preferred seat number: ")
card_type = input("Your card type: ")
card_number = input("Your card number: ")
card_cvc = input("Your card cvc: ")
card_holder = input("Card holder name: ")


user = User(name)
card = Card(card_type, card_number, card_cvc, card_holder)
seat = Seat(seat_id)

print(user.buy(seat, card))
