# BULLS-EYE-USING-GENETIC-ALGORITHM
https://github.com/AnujSonawane/BULLS-EYE-USING-GENETIC-ALGORITHM/assets/81616419/426b5ba1-7a16-4c50-805d-7f40a8572ef9
### What's happening in the code?
1.The code sets up the game window, initializes the Pygame module, and creates the screen with the specified width and height.<br>
2.The create_population function is called to generate an initial population of genomes.<br>
3.The done variable is initially set to False. This variable controls the main game loop and determines when to stop the simulation.<br>
4.The main game loop starts with a while not done loop. This loop continues until the done variable is set to True.<br>
5.Inside the game loop, the code processes any events, such as mouse clicks or window close events, by iterating through the pygame.event.get() list.<br>
6.The code evaluates the fitness scores for each genome in the population using the evaluate_fitness function. The fitness scores are stored in the fitness_scores list.<br>
7.The code finds the best genome in the population by finding the maximum fitness score using the max function and storing the best fitness score and its position.<br>
8.The code checks if the stopping condition is met. If the best fitness score is greater than or equal to the FITNESS_THRESHOLD or the distance between the best position and the target is less than or equal to the DISTANCE_THRESHOLD, the done variable is set to True, and the game loop will exit.<br>
9.The code creates a new population by preserving the best genome from the previous generation in the new_population list.<br>
10.Offspring genomes are generated through selection, crossover, and mutation. Parents are selected based on their fitness scores, and their genetic information is combined to create new offspring genomes. The select_parents, crossover, and mutate functions are used for these operations.<br>
11.The population is replaced with the new population, and the generation counter is incremented.<br>
12.The screen is cleared with a black color using screen.fill((0, 0, 0)).<br>
13.A subset of individuals (specified by DRAWN_INDIVIDUALS) is randomly selected from the population, and their positions are drawn on the screen as white circles using the pygame.draw.circle function.<br>
14.The target is drawn as a red circle at the center of the screen using pygame.draw.circle.<br>
15.The best genome is highlighted as a green circle by drawing a circle at its position using pygame.draw.circle.<br>
16.Finally, the screen is updated with pygame.display.flip(), and the frame rate is limited to 60 frames per second using clock.tick(60).<br>
17.The Pygame module is unloaded and the program exits.<br>
