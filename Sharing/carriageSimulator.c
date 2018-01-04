#include "reg52.h"
//#include "desCtrl.h"
#include <intrins.h>
#define UINTLIM 65500

#ifndef __cplusplus
typedef enum { False = 0, True = !False } bool;
#endif
#define TUBE P0

typedef unsigned int u16; //Seriously I don't want to use these abbr
typedef unsigned char u8;


sbit motorFow = P1 ^ 0; //
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
unsigned char shapeFow[] = {0x00, 0x00, 0x00, 0x00, 0x40, 0x40, 0x40, 0x70};
unsigned char shapeRev[] = {0x46, 0x40, 0x40, 0x40, 0x00, 0x00, 0x00, 0x00};
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
	/* Shift the shapeFow array to left */
	char temp = shapeFow[0];
	int iterator;
	shapeFow[0] = shapeFow[7];
	for (iterator = 7; iterator > 1; iterator --)
		shapeFow[iterator] = shapeFow[iterator - 1];
	shapeFow[1] = temp;
}
void digbackwarding(){
	/* Shift the shapeFow array to left */
	char temp = shapeRev[7];
	int iterator;
	shapeRev[7] = shapeRev[0];
	for (iterator = 0; iterator < 7; iterator ++)
		shapeRev[iterator] = shapeRev[iterator + 1];
	shapeRev[6] = temp;
}
void delaySecond(int time_Second) {
	/*Delay the time as the input, unity: second
	Usually have 1 second's err*/
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
	unsigned int delayTime = 65500 - argSpeed;
	if (forward) {
		motorFow = 1; motorRev = 0; motorDirection = 1;
	}
	else {
		motorFow = 0; motorRev = 1; motorDirection = -1;
	}
	delay(delayTime);
}
void motorHalt(){
	motorFow = motorRev = 0;
	motorDirection = 0;
}

//==================================================
//==================================================
void demoMode(){
	//motorHalt();
	unsigned int speed, step, upperBound,lowerBound;
	speed = (int)(UINTLIM / 2); step = 100;
	upperBound = UINTLIM; lowerBound = 100;
	while (True){

		if (scanButton(accelerateButton))
			speed -= step;
		if (scanButton(decreaseButton))
			speed += step;
		if (scanButton(motorFowButton))
			motorForward(True, speed);
		if (scanButton(motorRevButton))
			motorForward(False, speed);

		delay(speed);

		if (speed > upperBound) speed = upperBound;
		if (speed < lowerBound) speed = lowerBound;
	}
}

void classMode(){
	while(! scanButton(startButton))
		digDisplay(shapeHalt, 10);
	while(! scanButton(buttonSQ2)){
		motorForward(True, 65250);
		if (second <= 9){
			digForwarding();
			second = 10;
		}
		digDisplay(shapeFow, 10);
	}
	while(! scanButton(buttonSQ1)){
		motorForward(False, 65250);
		if (second <= 9){
			digbackwarding();
			second = 10;
		}
		digDisplay(shapeRev, 10);
	}
	motorHalt();
	second = 10;
	while(second > 1)
		digDisplay(shapeHalt, 10);
	while(! scanButton(buttonSQ3)){
		motorForward(True, 65250);
		if (second <= 9){
			digForwarding();
			second = 10;
		}
		digDisplay(shapeFow, 10);
	}
	while(! scanButton(buttonSQ1)){
		motorForward(False, 65250);
		if (second <= 9){
			digbackwarding();
			second = 10;
		}
		digDisplay(shapeRev, 10);
	}
	motorHalt();
	while(! scanButton(startButton))
		digDisplay(shapeHalt, 10);
}

void main() {
	//==============Start====================
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
