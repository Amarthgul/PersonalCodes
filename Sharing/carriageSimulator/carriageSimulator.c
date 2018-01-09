#include "reg52.h"
#include <string.h>
#ifndef __cplusplus
typedef enum { False = 0, True = !False } bool;
#endif
#define TUBE P0

typedef unsigned int u16; //Seriously I don't want to use these abbr
typedef unsigned char u8;


sbit motorFow = P1 ^ 0; //Pins that outputs signal for the motor
sbit motorRev = P1 ^ 1;
sbit LSA = P1 ^ 2; //Digital tube bit-wise selection
sbit LSB = P1 ^ 3;
sbit LSC = P1 ^ 4;

sbit startButton = P2 ^ 7; //SQ1 in diagram
sbit buttonSQ1 = P2 ^ 6; //SQ1 in diagram
sbit buttonSQ2 = P2 ^ 5; //SQ2 in diagram
sbit buttonSQ3 = P2 ^ 4; //SQ3 in diagram

sbit accelerateButton = P2 ^ 3; //Deluxe button
sbit decreaseButton = P2 ^ 2; //Deluxe button
sbit motorFowButton = P2 ^ 1; //Deluxe button
sbit motorRevButton = P2 ^ 0; //Deluxe button

unsigned int second = 10;
unsigned char digit[] = {0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f,
	0x6f, 0x77, 0x7c, 0x39, 0x5e, 0x79, 0x71}; // 1, 2, 3 ... D, E, F
unsigned char shapeFow[] = {0x00, 0x40, 0x40, 0x70, 0x00, 0x40, 0x40, 0x70};
unsigned char shapeRev[] = {0x46, 0x40, 0x40, 0x00, 0x46, 0x40, 0x40, 0x00};
unsigned char shapeHalt[] = {0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40};
char motorDirection = 0;

void delay(unsigned int i) {
	while(i --);
}
void timerInit() {
	TMOD = 0X10; TR1 = 1;
	TH1 = 0XFC; TL1 = 0X18;
	ET1 = 1; EA = 1;
}

void digDisplay(unsigned char * diplayArray, unsigned int delayTime) {
	unsigned char i;
	for(i=0;i<8;i++) {
		switch(i) {
			case 0: {
				LSA = LSB = LSC = 0;
				break; }
			case 1: {
				LSA = 1; LSB = LSC = 0;
				break; }
			case 2: {
				LSB = 1; LSC = LSA = 0;
				break; }
			case 3: {
				LSA = LSB = 1; LSC = 0;
				break; }
			case 4: {
				LSA = LSB = 0; LSC = 1;
				break; }
			case 5: {
				LSA = LSC = 1; LSB = 0;
				break; }
			case 6: {
				LSA = 0; LSB = LSC = 1;
				break; }
			case 7: {
				LSA = LSB = 1; LSC = 1;
				break; }
		}
		TUBE = diplayArray[i];
		delay(delayTime);
		TUBE = 0x00;
	}
}
void digForwarding(){
	/* Shift the shapeFow array right */
	char temp = shapeFow[0];
	int iterator;
	shapeFow[0] = shapeFow[7];
	for (iterator = 7; iterator > 1; iterator --)
		shapeFow[iterator] = shapeFow[iterator - 1];
	shapeFow[1] = temp;
}
void digbackwarding(){
	/* Shift the shapeRev array left */
	char temp = shapeRev[7];
	int iterator;
	shapeRev[7] = shapeRev[0];
	for (iterator = 0; iterator < 7; iterator ++)
		shapeRev[iterator] = shapeRev[iterator + 1];
	shapeRev[6] = temp;
}
void delaySecond(int time_Second) {
	/*Delay the time as the input, unity: second
	Usually have 1 second's err, and deprives evething else*/
	second = time_Second + 1;
	while (True){
		if (second < 1){
			break;
		}
	}
}

int scanButton(button) {
	/* Detect if that button is pressed */
	if (! button) {
		delay(100);
		if (! button)
			return True;
	}
	else return False;
}
void motorForward(bool forward, unsigned int argSpeed){
	/* Should work either in loop or simply switch direction */
	unsigned int delayTime = 65535 - argSpeed;
	if (forward) {
		motorFow = 1; motorRev = ~motorFow; motorDirection = 1;
	}
	else {
		motorFow = 0; motorRev = ~motorFow; motorDirection = -1;
	}
	delay(delayTime);
}
void motorHalt(){
	motorFow = motorRev = 0;
	motorDirection = 0;
}


void classMode(){
	/* As the assignment asked */
	bool digFlag = False;
	unsigned char digDup[8];
	//=====================Waiting startButton========================
	memcpy(digDup, shapeHalt, sizeof(shapeHalt));
	digDup[4] = digDup[5] = digDup[6] = digDup[7] = 0;
	while(! scanButton(startButton)) {
		if (second <= 9) {
			digFlag = ~digFlag; second = 10; }
		if (digFlag) {digDup[4] = 0x00; }
		else {digDup[4] = digit[5]; }
		digDisplay(digDup, 1);
	}
	//==============startButton Pressed, waiting buttonSQ2==========
	while(! scanButton(buttonSQ2)) {
		memcpy(digDup, shapeFow, sizeof(shapeFow));
		digDup[4] = digit[5]; digDup[6] = digit[2]; digDup[5] = digDup[7] = 0;
		motorForward(True, 65500);
		if (second <= 9) {
			digForwarding();
			second = 10; digFlag = ~digFlag; }
		if (digFlag) {digDup[6] = 0; }
		else {digDup[6] = digit[2]; }
		digDisplay(digDup, 1);
	}
	//==============buttonSQ2 Pressed, waiting buttonSQ1==========
	while(! scanButton(buttonSQ1)) {
		memcpy(digDup, shapeRev, sizeof(shapeRev));
		digDup[4] = digDup[7] = 0; digDup[5] = digit[1]; digDup[6] = digit[2];
		motorForward(False, 65500);
		if (second <= 9) {
			digbackwarding();
			second = 10; digFlag = ~ digFlag; }
		if (digFlag) {digDup[5] = 0; }
		else {digDup[5] = digit[1]; }
		digDisplay(digDup, 1);
	}
	//==============buttonSQ1 Pressed, waiting buttonSQ3==========
	motorHalt();
	second = 10;
	while(second > 1){
		digDisplay(shapeHalt, 1);
	}
	while(! scanButton(buttonSQ3)){
		memcpy(digDup, shapeFow, sizeof(shapeFow));
		digDup[4] = digDup[6] = 0; digDup[5] = digit[1]; digDup[7] = digit[3];
		motorForward(True, 65500);
		if (second <= 9) {
			digForwarding();
			second = 10; digFlag = ~digFlag; }
		if (digFlag) {digDup[7] = 0; }
		else {digDup[7] = digit[3]; }
		digDisplay(digDup, 1);
	}
	//==============buttonSQ3 Pressed, waiting buttonSQ1==========
	while(! scanButton(buttonSQ1)){
		memcpy(digDup, shapeRev, sizeof(shapeRev));
		digDup[4] = digDup[6] = 0; digDup[5] = digit[1]; digDup[7] = digit[3];
		motorForward(False, 65500);
		if (second <= 9) {
			digbackwarding();
			second = 10; digFlag = ~ digFlag; }
		if (digFlag) {digDup[5] = 0; }
		else {digDup[5] = digit[1]; }
		digDisplay(digDup, 1);
	}
	//Ended, RIP
	motorHalt();
	while(! scanButton(startButton)){
		digDisplay(shapeHalt, 1);
	}
}

void main() {
	//==============Start====================
	int i;
	TUBE = 0x00;
	timerInit();
	motorHalt();
	second = 10;

	classMode();
	//===============End=====================
}


//================Minor================
void timer() interrupt 3 {
	static unsigned int i;
	TH1 = 0XFC; TL1 = 0X18;
	i++;
	if (i >= 1000) {
		i = 0;
		second --; }
}
