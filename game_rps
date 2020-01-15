/*

	TITLE : ROCK, PAPER SCISSORS v.1

	DESCRIPTION :
		A sample game to figure out mechanics of the Dart language.

	HOW TO USE :
		User selects option (0-2) representing Rocks, Paper, Scissors. Computer
		generates random number of the same (0-2) representation and displays winner.

	WIN CONDITION : Rock beats Scissors, Scissors beats Paper, Paper beats Rock.

	ISSUES :
		Displays in wrong order player choice , win / lose , cpu choice; should be fixed
		to read player choice, cpu choice, win / lose.

	SIDE NOTE : This version will be left as is until further notice b/c of time constraints and
		was meant as a practice test of the Dart language.

	IMPROVEMENTS :
		Graphical Interface for further practice.
		Online Capabilites for further practice.

*/



import 'dart:math';
import 'dart:io';

class Win_Condition {
	win_logic (choice, rock_paper_scissor) {
		if (choice == "0") { print("PLAYER : ROCK"); }
		if (choice == "1") { print("PLAYER : PAPER"); }
		if (choice == "2") { print("PLAYER : SCISSORS"); }

///////////////////////////////////////////////////////////////////////// [DRAW]
		if (choice == "0" && rock_paper_scissor == 0) { print("DRAW"); }
		if (choice == "1" && rock_paper_scissor == 1) { print("DRAW"); }
		if (choice == "2" && rock_paper_scissor == 2) { print("DRAW"); }

///////////////////////////////////////////////////////////////// [ROCK v. Var.]
		if (choice == "0" && rock_paper_scissor == 1) { print("LOSE"); }
		if (choice == "0" && rock_paper_scissor == 2) { print("WIN"); }

//////////////////////////////////////////////////////////////// [PAPER v. Var.]
		if (choice == "1" && rock_paper_scissor == 0) { print("WIN"); }
		if (choice == "1" && rock_paper_scissor == 2) { print("LOSE"); }

///////////////////////////////////////////////////////////// [SCISSORS v. Var.]
		if (choice == "2" && rock_paper_scissor == 0) { print("LOSE"); }
		if (choice == "2" && rock_paper_scissor == 1) { print("WIN"); }
	}//// [win_logic ()]
} ////////////////////////////////////////////////////////////// [Win_Condition]

///////////////////////////////////////////////////////////////////////// [Main]
void main() {
	Win_Condition frame = new Win_Condition ();
	var random = new Random ();
	var rock_paper_scissor = random.nextInt(3);

	print("0 : ROCK \n1 : PAPER \n2 : SCISSORS");

	var choice = stdin.readLineSync();
	frame.win_logic(choice, rock_paper_scissor);

	switch (rock_paper_scissor) {
		case 0: { print("CPU : ROCK"); }
		break;
		case 1: { print("CPU : PAPER"); }
		break;
		case 2:	{ print("CPU : SCISSORS"); }
		break;
		default:{ print("nah"); }
	} //// [Switch]
} /////////////////////////////////////////////////////////////////////// [Main]
