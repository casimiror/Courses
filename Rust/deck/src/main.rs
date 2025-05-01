
#[derive(Debug)]
struct Deck {
    cards: Vec<String>, // Vec is a growable array;
}

fn main() {
    let suits = ["Hearts", "Diamonds", "Clubs", "Spades"];
    let values = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"];
    let mut cards = vec![];
    for suit in suits {
        for value in values {
            let card = format!("{} of {}", value, suit);
            cards.push(card);
        }
    }
    let deck = Deck{ cards };
    println!("Here's your deck {:#?}!", deck);
}
