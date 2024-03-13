from time import sleep
import pygame
import sys
from board import Board
from ai import AI
from constants import *
  
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND)
      
            
class Game:
    def __init__(self):
        self.board = Board()
        self.player = X
        self.running = True
        self.bot = AI(2,1)
        self.draw_board_lines()
        
        
    # DRAWING FUNCTIONS   
        
    def draw_board_lines(self):
        screen.fill(BACKGROUND)
        
        #vertical lines
        pygame.draw.line(screen,LINE,(200,0),(200,600), 5)
        pygame.draw.line(screen,LINE,(400,0),(400,600), 5)
        
        #horizontal lines
        pygame.draw.line(screen,LINE,(0,200),(600,200), 5)
        pygame.draw.line(screen,LINE,(0,400),(600,400), 5)
    
    def draw_symbol(self, row, col):
        if self.board.player_mark(row, col) != 0:
            return
        else:
            if self.player == 1:
                # draw cross
                # desc line
                start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
                end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                pygame.draw.line(screen, SYMCOLOR, start_desc, end_desc, 5)
                # asc line
                start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
                pygame.draw.line(screen, SYMCOLOR, start_asc, end_asc, 5)
                self.board.mark(row, col, self.player)
                self.player = 2
                
            elif self.player == 2:
                # draw circle
                center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
                pygame.draw.circle(screen, SYMCOLOR, center, SQSIZE//4, 5)
                self.board.mark(row, col, self.player)
                self.player = 1
        
    
        
def main():
    game= Game()
    
    while game.running:
        if game.player == 1:
            for event in pygame.event.get(): #REFACTOR
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (row,col)= event.pos
                        game.draw_symbol(col//200, row//200)
                    if event.type == pygame.KEYDOWN and game.board.is_full():  # reset game 
                        if event.key == pygame.K_r:
                            game = Game()    
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        elif game.player == game.bot.player and game.running:
            x,y = game.bot.eval(game.board)
            print(x,y)
            game.board.mark(x,y,2)
            game.draw_symbol(x,y)
            pygame.display.update()
            if game.board.check_board_state() is not None:
                game.running = False
                pygame.display.update()
        winner = game.board.check_board_state()  
        if winner is not None:
            pygame.transform.smoothscale(screen, (WIDTH, HEIGHT), screen)
            pygame.display.set_caption("Winner is {}".format(winner))
            pygame.display.flip()
            sleep(2)
            game.running = False
        else: pygame.display.set_caption("TIE" if game.board.is_full() else "TIC TAC TOE")
        pygame.display.flip()
         
        
        
        
if __name__ == '__main__':
    main()
            