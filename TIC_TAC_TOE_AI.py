import pygame
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 10
SPACE = SQUARE_SIZE // 4
WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
RED = (200, 0, 0)
GRAY = (180, 180, 180)
BLUE = (0, 102, 204)
LIGHT_GRAY = (220, 220, 220)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI")
screen.fill(WHITE)

# Board
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 'X'
ai_player = 'O'
winner = None

def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)

def draw_buttons():
    font = pygame.font.Font(None, 40)
    restart_text = font.render("Restart", True, WHITE)
    pygame.draw.rect(screen, BLUE, (110, HEIGHT - 80, 180, 50), border_radius=15)
    screen.blit(restart_text, (150, HEIGHT - 70))

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_board_full():
    return all(cell != ' ' for row in board for cell in row)

def minimax(is_maximizing):
    result = check_winner()
    if result == ai_player:
        return 10
    if result == player:
        return -10
    if is_board_full():
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai_player
                    score = minimax(False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = minimax(True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = ai_player
                score = minimax(False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = ai_player

def reset_game():
    global board, player, ai_player, winner
    board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    winner = None

def handle_click(x, y):
    global winner
    if 110 <= x <= 290 and HEIGHT - 80 <= y <= HEIGHT - 30:
        reset_game()
    elif not winner:
        row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
        if row < 3 and board[row][col] == ' ':
            board[row][col] = player
            winner = check_winner()
            if not winner and not is_board_full():
                best_move()
                winner = check_winner()

def draw_winner():
    if winner or is_board_full():
        font = pygame.font.Font(None, 60)
        text = "Draw!" if is_board_full() and not winner else f"{winner} Wins!"
        text_render = font.render(text, True, BLUE)
        pygame.draw.rect(screen, LIGHT_GRAY, (WIDTH // 2 - 150, HEIGHT // 2 - 40, 300, 80), border_radius=15)
        screen.blit(text_render, (WIDTH // 2 - text_render.get_width() // 2, HEIGHT // 2 - 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(*event.pos)
    screen.fill(WHITE)
    draw_grid()
    draw_figures()
    draw_buttons()
    draw_winner()
    pygame.display.update()