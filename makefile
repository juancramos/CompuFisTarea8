a.out: tarea8.o 
	@cc -lm tarea8.o, tarea8_2.o 
	@./a.out
	@python dibujar.py
	@python dibujar2.py
	@rm -f *.dat

main.o: tarea8.c
	@cc -c tarea8.c

main.o: tarea8_2.c
	@cc -c tarea8_2.c


all: a.out

clean: 
	@rm -f *.o
	@rm -f a.out
	@rm -f *.jpg

