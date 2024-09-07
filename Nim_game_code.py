import random

def print_piles(red, blue):
    print(f"Current piles: {red} red, {blue} blue")

def get_player_move(max_red, max_blue):
    while True:
        try:
            move = input(f"Enter your move (1-{max_red} red, 1-{max_blue} blue): ").strip()
            red_move, blue_move = move.split()
            red_move = int(red_move)
            blue_move = int(blue_move)

            if 1 <= red_move <= max_red and 1 <= blue_move <= max_blue:
                return red_move, blue_move
            else:
                print(f"Invalid move. Please enter numbers within the valid range: 1-{max_red} red, 1-{max_blue} blue.")
        except ValueError:
            print("Invalid input. Please enter your move in the format: <red> red, <blue> blue.")

def get_computer_move(red, blue):
    # Computer strategy: Randomly remove 1 or 2 marbles from either pile
    if red > 0:
        red_remove = random.randint(1, min(2, red))
    else:
        red_remove = 0

    if blue > 0:
        blue_remove = random.randint(1, min(2, blue))
    else:
        blue_remove = 0

    return red_remove, blue_remove

def main():
    # Initialize the piles
    max_red = 10
    max_blue = 15
    
    red = max_red
    blue = max_blue
    
    # Game loop
    while red > 0 or blue > 0:
        print_piles(red, blue)
        
        # Human's turn
        red_move, blue_move = get_player_move(red, blue)
        red -= red_move
        blue -= blue_move
        
        # Check for human win condition
        if red <= 0 and blue <= 0:
            print("You win!")
            break
        
        # Computer's turn
        if red > 0 or blue > 0:
            print("Computer's turn:")
            red_remove, blue_remove = get_computer_move(red, blue)
            red -= red_remove
            blue -= blue_remove
            print(f"Computer removes {red_remove} red and {blue_remove} blue marbles.")
        
            # Check for computer win condition
            if red <= 0 and blue <= 0:
                print("Computer wins!")
                break

if __name__ == "__main__":
    main()
