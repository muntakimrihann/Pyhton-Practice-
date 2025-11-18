import pygame
import sys
import time
import random
from copy import deepcopy


pygame.init()
WIDTH, HEIGHT = 600, 700
GRID_SIZE = 3
CELL = WIDTH // GRID_SIZE
LINE_COLOR = (30, 30, 30)
BG_COLOR = (245, 245, 245)
X_COLOR = (220, 40, 40)
O_COLOR = (40, 120, 220)
HIGHLIGHT_COLOR = (60, 180, 75)
SCORE_COLOR = (20, 20, 20)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe — Pygame (Smart AI)")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 44)


EMPTY = ' '
PLAYER = 'X'  # human
AI = 'O'      # computer

board = [EMPTY] * 9
scores = {"Player": 0, "Computer": 0, "Draws": 0}
game_over = False
winner = None
winning_combo = None
ai_thinking = False
last_move_time = 0

# UI buttons rects
RESTART_RECT = pygame.Rect(20, HEIGHT-80, 120, 50)
RESET_SCORE_RECT = pygame.Rect(160, HEIGHT-80, 160, 50)
EXIT_RECT = pygame.Rect(WIDTH-140, HEIGHT-80, 120, 50)


def draw_grid():
    gap = CELL
    for i in range(1, GRID_SIZE):
        # vertical
        pygame.draw.line(screen, LINE_COLOR, (i*gap, 0), (i*gap, GRID_SIZE*CELL), 6)
        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, i*gap), (GRID_SIZE*CELL, i*gap), 6)

def index_to_cell(i):
    row = i // GRID_SIZE
    col = i % GRID_SIZE
    x = col * CELL
    y = row * CELL
    return x, y, CELL, CELL

def draw_x(x, y, size, progress=1.0):
    # animate two lines progressively by progress (0..1)
    pad = size // 6
    x1, y1 = x + pad, y + pad
    x2, y2 = x + size - pad, y + size - pad
    x3, y3 = x + size - pad, y + pad
    x4, y4 = x + pad, y + size - pad
    # draw first line
    midx = x1 + (x2 - x1) * min(progress, 0.5) * 2
    midy = y1 + (y2 - y1) * min(progress, 0.5) * 2
    if progress > 0:
        pygame.draw.line(screen, X_COLOR, (x1, y1), (midx, midy), 10)
    # draw second line (starts when progress > 0.5)
    if progress > 0.5:
        p2 = (progress - 0.5) * 2
        midx2 = x3 + (x4 - x3) * p2
        midy2 = y3 + (y4 - y3) * p2
        pygame.draw.line(screen, X_COLOR, (x3, y3), (midx2, midy2), 10)

def draw_o(x, y, size, progress=1.0):
    # draw circle arc according to progress (0..1)
    center = (x + size//2, y + size//2)
    radius = size//2 - size//6
    # approximate arc by drawing many small lines
    segments = int(80 * progress)
    if segments < 2:
        return
    angle_step = 2 * 3.14159 / 80
    points = []
    for s in range(segments + 1):
        angle = s * angle_step
        px = center[0] + radius * pygame.math.cos(angle)
        py = center[1] + radius * pygame.math.sin(angle)
        points.append((px, py))
    if len(points) > 1:
        pygame.draw.lines(screen, O_COLOR, False, points, 8)

def render_board(animate=False, anim_progress_map=None):
    # anim_progress_map: dict idx -> progress (0..1)
    for i, v in enumerate(board):
        x, y, w, h = index_to_cell(i)
        if v == 'X':
            p = 1.0
            if animate and anim_progress_map and i in anim_progress_map:
                p = anim_progress_map[i]
            draw_x(x, y, w, p)
        elif v == 'O':
            p = 1.0
            if animate and anim_progress_map and i in anim_progress_map:
                p = anim_progress_map[i]
            draw_o(x, y, w, p)

def check_winner_state(b):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b2,c in wins:
        if b[a] != EMPTY and b[a] == b[b2] == b[c]:
            return b[a], (a,b2,c)
    if EMPTY not in b:
        return 'Draw', None
    return None, None

# -----------------------
# AI: smart trick moves + minimax fallback
# -----------------------
def available_moves(b):
    return [i for i, v in enumerate(b) if v == EMPTY]

def make_move(b, idx, player):
    nb = b.copy()
    nb[idx] = player
    return nb

def can_win_next(b, player):
    for m in available_moves(b):
        nb = make_move(b, m, player)
        w, _ = check_winner_state(nb)
        if w == player:
            return m
    return None

def count_two_in_row(b, player):
    # count potential lines with 2 player marks and 1 empty
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    cnt = 0
    for a,b2,c in wins:
        line = [b[a], b[b2], b[c]]
        if line.count(player) == 2 and line.count(EMPTY) == 1:
            cnt += 1
    return cnt

def find_fork_move(b, player):
    for m in available_moves(b):
        nb = make_move(b, m, player)
        # after move if player has 2+ winning chances -> fork
        wins = 0
        for m2 in available_moves(nb):
            nb2 = make_move(nb, m2, player)
            w, _ = check_winner_state(nb2)
            if w == player:
                wins += 1
        if wins >= 2:
            return m
    return None

# Classic priority choices (from optimal tic-tac-toe strategy)
def choose_corner_move(b):
    corners = [0,2,6,8]
    avail = [c for c in corners if b[c] == EMPTY]
    return random.choice(avail) if avail else None

def choose_side_move(b):
    sides = [1,3,5,7]
    avail = [s for s in sides if b[s] == EMPTY]
    return random.choice(avail) if avail else None

def choose_center(b):
    return 4 if b[4] == EMPTY else None

def choose_opposite_corner(b, opponent):
    pairs = [(0,8),(2,6),(6,2),(8,0)]
    for a,b2 in pairs:
        if board[a] == opponent and board[b2] == EMPTY:
            return b2
    return None

# Minimax for final fallback and to evaluate positions
def minimax_eval(b, is_max):
    w, _ = check_winner_state(b)
    if w == AI:
        return 1
    elif w == PLAYER:
        return -1
    elif w == 'Draw':
        return 0

    if is_max:
        best = -999
        for m in available_moves(b):
            nb = make_move(b, m, AI)
            score = minimax_eval(nb, False)
            best = max(best, score)
        return best
    else:
        best = 999
        for m in available_moves(b):
            nb = make_move(b, m, PLAYER)
            score = minimax_eval(nb, True)
            best = min(best, score)
        return best

def ai_smart_move(b):
    # 1) Win if possible
    wmove = can_win_next(b, AI)
    if wmove is not None:
        return wmove

    # 2) Block if player can win next
    bmove = can_win_next(b, PLAYER)
    if bmove is not None:
        return bmove

    # 3) Create a fork
    fork = find_fork_move(b, AI)
    if fork is not None:
        return fork

    # 4) Block opponent's fork
    opp_fork = find_fork_move(b, PLAYER)
    if opp_fork is not None:
        # try to block by creating a 2-in-row forcing opponent to block
        # if center available -> take center
        c = choose_center(b)
        if c is not None:
            return c
        # else, play a side
        s = choose_side_move(b)
        if s is not None:
            return s
        # else fallback
        return opp_fork

    # 5) Take center
    c = choose_center(b)
    if c is not None:
        return c

    # 6) Opposite corner
    oc = choose_opposite_corner(b, PLAYER)
    if oc is not None:
        return oc

    # 7) Empty corner
    ec = choose_corner_move(b)
    if ec is not None:
        return ec

    # 8) Empty side
    es = choose_side_move(b)
    if es is not None:
        return es

    # 9) Minimax fallback (safe)
    best = -999
    move = None
    for m in available_moves(b):
        nb = make_move(b, m, AI)
        score = minimax_eval(nb, False)
        if score > best:
            best = score
            move = m
    if move is not None:
        return move
    # Last resort
    return random.choice(available_moves(b))

# -----------------------
# Animation helpers
# -----------------------
def animate_symbol(index, player_char):
    # progressive animation for a newly placed symbol
    start = time.time()
    duration = 0.25  # seconds
    while True:
        t = (time.time() - start) / duration
        t = min(1.0, t)
        screen.fill(BG_COLOR, (0,0, WIDTH, GRID_SIZE*CELL))
        draw_grid()
        # render others fully
        for i, v in enumerate(board):
            if i == index:
                continue
            x,y,w,h = index_to_cell(i)
            if v == 'X':
                draw_x_animated(x, y, w, 1.0)
            elif v == 'O':
                draw_o_animated(x, y, w, 1.0)
        # draw current with progress t
        x,y,w,h = index_to_cell(index)
        if player_char == 'X':
            draw_x_animated(x, y, w, t)
        else:
            draw_o_animated(x, y, w, t)
        pygame.display.flip()
        clock.tick(FPS)
        if t >= 1.0:
            break

# small wrappers using same drawing logic as earlier drawing functions
def draw_x_animated(x,y,size,progress):
    pad = size // 6
    x1, y1 = x + pad, y + pad
    x2, y2 = x + size - pad, y + size - pad
    x3, y3 = x + size - pad, y + pad
    x4, y4 = x + pad, y + size - pad
    midx = x1 + (x2 - x1) * min(progress, 0.5) * 2
    midy = y1 + (y2 - y1) * min(progress, 0.5) * 2
    if progress > 0:
        pygame.draw.line(screen, X_COLOR, (x1, y1), (midx, midy), 10)
    if progress > 0.5:
        p2 = (progress - 0.5) * 2
        midx2 = x3 + (x4 - x3) * p2
        midy2 = y3 + (y4 - y3) * p2
        pygame.draw.line(screen, X_COLOR, (x3, y3), (midx2, midy2), 10)

def draw_o_animated(x,y,size,progress):
    center = (x + size//2, y + size//2)
    radius = size//2 - size//6
    segments = int(80 * progress)
    if segments < 2:
        return
    angle_step = 2 * 3.14159 / 80
    points = []
    for s in range(segments + 1):
        angle = s * angle_step
        px = center[0] + radius * pygame.math.cos(angle)
        py = center[1] + radius * pygame.math.sin(angle)
        points.append((px, py))
    if len(points) > 1:
        pygame.draw.lines(screen, O_COLOR, False, points, 8)

def highlight_win_line(combo):
    a,b2,c = combo
    xa,ya,_,_ = index_to_cell(a)
    xc,yc,_,_ = index_to_cell(c)
    ax = xa + CELL//2
    ay = ya + CELL//2
    cx = xc + CELL//2
    cy = yc + CELL//2
    # animate highlight
    start = time.time()
    dur = 0.6
    while True:
        t = (time.time() - start) / dur
        t = min(1.0, t)
        screen.fill(BG_COLOR, (0,0, WIDTH, GRID_SIZE*CELL))
        draw_grid()
        render_board()
        pygame.draw.line(screen, HIGHLIGHT_COLOR, (ax, ay), (ax + (cx-ax)*t, ay + (cy-ay)*t), 14)
        pygame.display.flip()
        clock.tick(FPS)
        if t >= 1.0:
            break

# -----------------------
# Main loop helpers
# -----------------------
def reset_board():
    global board, game_over, winner, winning_combo
    board = [EMPTY] * 9
    game_over = False
    winner = None
    winning_combo = None

def handle_player_move(pos):
    global board
    idx = pos[1] // CELL * GRID_SIZE + pos[0] // CELL
    if idx < 0 or idx >= 9 or board[idx] != EMPTY or game_over:
        return False
    board[idx] = PLAYER
    animate_symbol(idx, PLAYER)
    return True

def do_ai_move():
    global board
    # compute AI move on current board copy
    move = ai_smart_move(board)
    # place and animate
    board[move] = AI
    animate_symbol(move, AI)

# -----------------------
# Buttons & UI Drawing
# -----------------------
def draw_ui():
    # area below grid
    pygame.draw.rect(screen, BG_COLOR, (0, GRID_SIZE*CELL, WIDTH, HEIGHT - GRID_SIZE*CELL))
    # draw scoreboard
    text = big_font.render("Tic-Tac-Toe", True, SCORE_COLOR)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, GRID_SIZE*CELL + 8))
    sc_text = font.render(f"Player (X): {scores['Player']}   Computer (O): {scores['Computer']}   Draws: {scores['Draws']}", True, SCORE_COLOR)
    screen.blit(sc_text, (20, GRID_SIZE*CELL + 60))

    # buttons
    pygame.draw.rect(screen, (200,200,200), RESTART_RECT, border_radius=6)
    pygame.draw.rect(screen, (200,200,200), RESET_SCORE_RECT, border_radius=6)
    pygame.draw.rect(screen, (200,200,200), EXIT_RECT, border_radius=6)
    screen.blit(font.render("Restart", True, (10,10,10)), (RESTART_RECT.x + 18, RESTART_RECT.y + 16))
    screen.blit(font.render("Reset Score", True, (10,10,10)), (RESET_SCORE_RECT.x + 18, RESET_SCORE_RECT.y + 16))
    screen.blit(font.render("Exit", True, (10,10,10)), (EXIT_RECT.x + 38, EXIT_RECT.y + 16))

def draw_end_message():
    if winner == PLAYER:
        msg = "You Win! 🎉"
        col = X_COLOR
    elif winner == AI:
        msg = "Computer Wins!"
        col = O_COLOR
    else:
        msg = "Draw!"
        col = (100,100,100)
    txt = big_font.render(msg, True, col)
    screen.blit(txt, (WIDTH//2 - txt.get_width()//2, GRID_SIZE*CELL + 110))

# -----------------------
# Main Loop
# -----------------------
def main():
    global game_over, winner, winning_combo, ai_thinking, last_move_time

    reset_board()
    running = True
    player_turn = True  # player always X
    ai_delay = 0.4  # seconds delay before AI moves

    while running:
        screen.fill(BG_COLOR)
        draw_grid()
        render_board()
        draw_ui()

        # show end message if any
        if game_over:
            draw_end_message()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx,my = event.pos
                # check button clicks
                if RESTART_RECT.collidepoint(mx,my):
                    reset_board()
                    player_turn = True
                    ai_thinking = False
                    continue
                if RESET_SCORE_RECT.collidepoint(mx,my):
                    scores["Player"] = scores["Computer"] = scores["Draws"] = 0
                    continue
                if EXIT_RECT.collidepoint(mx,my):
                    running = False
                    break

                # only allow clicks on grid area when not game over
                if my < GRID_SIZE*CELL and not game_over and player_turn:
                    if handle_player_move((mx,my)):  # valid player move
                        player_turn = False
                        last_move_time = time.time()
                        # check winner
                        w, combo = check_winner_state(board)
                        if w == PLAYER:
                            winner = PLAYER
                            winning_combo = combo
                            game_over = True
                        elif w == 'Draw':
                            winner = None
                            winning_combo = None
                            game_over = True
                            scores["Draws"] += 1

        # AI move handling with slight delay to show "thinking"
        if not player_turn and not game_over:
            # ai thinking effect
            if not ai_thinking:
                ai_thinking = True
                last_move_time = time.time()
            else:
                if time.time() - last_move_time > ai_delay:
                    do_ai_move()
                    ai_thinking = False
                    player_turn = True
                    # check winner after AI move
                    w, combo = check_winner_state(board)
                    if w == AI:
                        winner = AI
                        winning_combo = combo
                        game_over = True
                    elif w == 'Draw':
                        winner = None
                        winning_combo = None
                        game_over = True
                        scores["Draws"] += 1

        # if game over, highlight and update scores
        if game_over and winning_combo:
            highlight_win_line(winning_combo)
            if winner == PLAYER:
                scores["Player"] += 1
            elif winner == AI:
                scores["Computer"] += 1
            # reset winning combo to avoid repeated highlight animations
            winning_combo = None

        # draw "computer thinking" small indicator
        if ai_thinking and not player_turn and not game_over:
            text = font.render("Computer is thinking...", True, (80,80,80))
            screen.blit(text, (WIDTH-220, GRID_SIZE*CELL + 60))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
