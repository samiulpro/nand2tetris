// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// Samiul Islam Sami


@SCREEN
D=A
@addr
M=D


(REFRESH)
	@KBD
	D=M
	@LOOP_BLACK
	D;JNE
	@LOOP_WHITE
	D;JEQ

(LOOP_BLACK)
	@addr
	A=M
	M=-1

	@INCREMENT_ADDR
	0;JMP

(LOOP_WHITE)
	@addr
	A=M
	M=0

	@INCREMENT_ADDR
	0;JMP

(INCREMENT_ADDR)
	@addr      // Load the current screen address
    D=M        // D = addr
    @24575     // The last screen address
    D=D-A      // Check if addr == 24575
    @RESET_ADDR
    D;JEQ      // If addr == 24575, reset to SCREEN base

    @addr
    M=M+1      // Increment the addr to the next screen register
    @REFRESH   // Return to REFRESH loop
    0;JMP

(RESET_ADDR)
    @SCREEN    // Load SCREEN base address
    D=A        // D = SCREEN
    @addr      // Reset addr to SCREEN
    M=D        // addr = SCREEN
    @REFRESH   // Return to REFRESH loop
    0;JMP