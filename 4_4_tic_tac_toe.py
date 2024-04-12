import pygame
import sys

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
SQUARE_SIZE = WIDTH // COLS
PADDING = 10
PIECE_RADIUS = SQUARE_SIZE // 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game States
PLAYING = "playing"
RED_WON = "red_won"
BLUE_WON = "blue_won"
DRAW = "draw"

# Initialize Pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4 X 4 Tic_Tac_Toe")

# Game Board
board = [[0]*COLS for _ in range(ROWS)]

# Player Turn
current_player = RED

# Game State
game_state = PLAYING

# Draw the game board
def draw_board():
    WIN.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(WIN, BLACK, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

# Draw pieces on the board
def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == RED:
                pygame.draw.circle(WIN, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS)
            elif board[row][col] == BLUE:
                pygame.draw.circle(WIN, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS)

# Check for winning condition
def check_win():
    # Check rows and columns
    for i in range(ROWS):
        if all([board[i][j] == current_player for j in range(COLS)]) or \
           all([board[j][i] == current_player for j in range(ROWS)]):
            return True

    # Check diagonals
    if all([board[i][i] == current_player for i in range(ROWS)]) or \
       all([board[i][ROWS - i - 1] == current_player for i in range(ROWS)]):
        return True

    return False

# Main game loop
def main():
    global current_player, game_state

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if game_state == PLAYING and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE

                if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == 0:
                    board[row][col] = current_player
                    if check_win():
                        if current_player == RED:
                            game_state = RED_WON
                        else:
                            game_state = BLUE_WON
                    elif all(board[i][j] != 0 for i in range(ROWS) for j in range(COLS)):
                        game_state = DRAW
                    else:
                        current_player = BLUE if current_player == RED else RED

        draw_board()
        draw_pieces()
        pygame.display.update()

        if game_state != PLAYING:
            font = pygame.font.Font(None, 36)
            if game_state == RED_WON:
                text = font.render("Red player won!", True, RED)
            elif game_state == BLUE_WON:
                text = font.render("Blue player won!", True, BLUE)
            elif game_state == DRAW:
                text = font.render("It's a draw!", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            WIN.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(3000)
            run = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
